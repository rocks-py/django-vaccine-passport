# Generated by Django 3.1.3 on 2020-12-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccineapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='is_hidden',
        ),
        migrations.AddField(
            model_name='disease',
            name='vaccines',
            field=models.ManyToManyField(to='vaccineapp.Vaccine'),
        ),
    ]