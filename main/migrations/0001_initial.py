# Generated by Django 3.0 on 2020-01-29 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=12)),
                ('color', models.CharField(default='', max_length=100)),
                ('status', models.CharField(choices=[('1', 'Звичайна'), ('2', 'Самостійна'), ('3', 'Зошит'), ('4', 'Контрольна'), ('5', 'Тематична'), ('6', 'Семестрова'), ('7', 'Річна'), ('8', 'Залік'), ('9', 'Екзамен')], default='Звичайна', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RatingSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('1', 'Укр. мова'), ('2', 'Математика')], default='Укр. мова', max_length=100)),
                ('day', models.IntegerField(default=1)),
                ('month', models.IntegerField(default=1)),
                ('rating1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets1', to='main.Rating')),
                ('rating2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets2', to='main.Rating')),
                ('rating3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets3', to='main.Rating')),
                ('rating4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets4', to='main.Rating')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_rating', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('ratings', models.ManyToManyField(blank=True, related_name='students', to='main.RatingSet')),
            ],
        ),
    ]
