# Generated by Django 5.2 on 2025-04-09 02:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_feedback_alter_tours_options_alter_tours_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(max_length=800, verbose_name='Отзыв'),
        ),
    ]
