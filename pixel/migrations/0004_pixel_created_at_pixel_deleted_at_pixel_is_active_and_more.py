# Generated by Django 5.1 on 2024-09-16 20:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0003_pixel_titulo_alter_pixel_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pixel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='pixel',
            name='is_active',
            field=models.BooleanField(default=True, editable=False),
        ),
        migrations.AddField(
            model_name='pixel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
