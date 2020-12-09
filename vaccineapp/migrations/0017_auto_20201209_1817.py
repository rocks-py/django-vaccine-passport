# Generated by Django 3.1.3 on 2020-12-09 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vaccineapp', '0016_auto_20201208_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userperson',
            name='person',
        ),
        migrations.RemoveField(
            model_name='userperson',
            name='user',
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserPerson',
        ),
    ]
