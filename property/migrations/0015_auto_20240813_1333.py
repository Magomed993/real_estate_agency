# Generated by Django 2.2.24 on 2024-08-13 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20240812_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
