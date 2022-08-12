# Generated by Django 3.2.7 on 2022-08-12 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airflow', '0003_rename_currency_exchangerate'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchData',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID поиска')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('FAILED', 'FAILED')], default='PENDING', max_length=9, verbose_name='Статус')),
                ('data', models.JSONField(blank=True, null=True, verbose_name='Результат поиска')),
            ],
            options={
                'verbose_name': 'Результат поиска',
                'verbose_name_plural': 'Результаты поиска',
            },
        ),
        migrations.DeleteModel(
            name='SearchResult',
        ),
    ]
