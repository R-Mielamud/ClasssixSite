# Generated by Django 3.0 on 2020-01-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_month_number_in_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='number_in_year',
            field=models.IntegerField(default=1),
        ),
    ]
