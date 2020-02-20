from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse

from search.models import Company


def index(request):
    return render(request, 'index.html', {})


def search(request):  # AJAX View
    if request.GET:
        data = request.GET.copy()
        company_title = data.get('company_title')
        company_address = data.get('company_address')
        if company_title and company_address:
            qs_companies = Company.objects.filter(title__icontains=company_title, address__icontains=company_address)
            if qs_companies:
                return JsonResponse({
                    'success': 1,
                    'message': 'Отчет успешно составлен',
                    'html': render_to_string('table.html', {'companies': qs_companies})
                })
            else:
                return JsonResponse({
                    'success': 0,
                    'message': 'Данных не найдено',
                })
        return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)
