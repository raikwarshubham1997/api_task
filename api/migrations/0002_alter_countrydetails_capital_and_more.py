# Generated by Django 4.1.4 on 2022-12-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrydetails',
            name='capital',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='countrydetails',
            name='flag_link',
            field=models.ImageField(blank=True, null=True, upload_to='productimage'),
        ),
    ]
