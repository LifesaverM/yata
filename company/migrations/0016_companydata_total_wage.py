# Generated by Django 3.1.2 on 2020-11-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20201122_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydata',
            name='total_wage',
            field=models.IntegerField(default=0),
        ),
    ]
