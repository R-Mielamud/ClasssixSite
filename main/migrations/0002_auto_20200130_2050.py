# Generated by Django 3.0 on 2020-01-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingset',
            name='rating1',
        ),
        migrations.RemoveField(
            model_name='ratingset',
            name='rating2',
        ),
        migrations.RemoveField(
            model_name='ratingset',
            name='rating3',
        ),
        migrations.RemoveField(
            model_name='ratingset',
            name='rating4',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AlterField(
            model_name='user',
            name='ratings',
            field=models.ManyToManyField(blank=True, related_name='students', to='diary.RatingSet'),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingSet',
        ),
    ]
