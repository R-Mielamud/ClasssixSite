# Generated by Django 3.0 on 2020-01-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_month_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='number_in_semester',
            field=models.IntegerField(default=1),
        ),
    ]