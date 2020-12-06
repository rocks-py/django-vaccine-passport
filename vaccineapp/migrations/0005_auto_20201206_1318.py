# Generated by Django 3.1.3 on 2020-12-06 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccineapp', '0004_auto_20201206_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='diseases',
            field=models.ManyToManyField(blank=True, through='vaccineapp.PersonVaccine', to='vaccineapp.Disease', verbose_name='болезни'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='diseases',
            field=models.ManyToManyField(blank=True, to='vaccineapp.Disease', verbose_name='заболевания'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='vaccines',
            field=models.ManyToManyField(blank=True, to='vaccineapp.Vaccine', verbose_name='вакцины'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccineapp.user', verbose_name='пользователь'),
        ),
        migrations.RemoveField(
            model_name='person',
            name='vaccines',
        ),
        migrations.AddField(
            model_name='person',
            name='vaccines',
            field=models.ManyToManyField(blank=True, through='vaccineapp.PersonVaccine', to='vaccineapp.Vaccine', verbose_name='вакцины'),
        ),
    ]
