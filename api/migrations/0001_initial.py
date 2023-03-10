# Generated by Django 4.1.4 on 2022-12-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='countryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_link', models.CharField(max_length=300)),
                ('capital', models.CharField(max_length=300)),
                ('largest_city', models.CharField(max_length=300)),
                ('official_languages', models.CharField(max_length=300)),
                ('area_total', models.CharField(max_length=300)),
                ('Population', models.CharField(max_length=300)),
                ('GDP_nominal', models.CharField(max_length=300)),
            ],
        ),
    ]
