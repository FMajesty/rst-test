# Generated by Django 2.2.10 on 2020-02-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название компании')),
                ('address', models.CharField(max_length=352, verbose_name='Адрес компании')),
            ],
        ),
    ]
