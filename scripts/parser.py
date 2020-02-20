import os
import sys
import django
BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rst.settings")
django.setup()

import mechanicalsoup as MS
from bs4 import BeautifulSoup as BS

from search.models import Company


link = 'https://www.rusprofile.ru/codes/721000'  # Ссылка на страницу, которую необходимо спарсить.
UA = 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P)'


def get_address(soup):
    return soup.find("address").text.strip()


def get_title(soup):
    return soup.find("div", attrs={'class': 'company-item__title'}).text.strip()


def parse(uri):
    browser =  MS.StatefulBrowser(user_agent=UA, soup_config={
        'features': 'lxml',
    })
    page = browser.open(uri)
    html = page.text.encode('utf-8')
    soup = BS(html, 'lxml')
    for company in soup.findAll("div", attrs={'class': 'company-item'}):
        new_company = Company(
            title = get_title(company),
            address = get_address(company),
        )
        new_company.save()


if __name__ == '__main__':
    parse(link)