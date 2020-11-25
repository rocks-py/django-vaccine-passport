# Generated by Django 3.1.3 on 2020-11-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccineapp', '0004_remove_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='vaccines',
            field=models.ManyToManyField(blank=True, null=True, to='vaccineapp.Vaccine'),
        ),
    ]
