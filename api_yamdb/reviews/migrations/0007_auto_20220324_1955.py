# Generated by Django 2.2.16 on 2022-03-24 16:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.PositiveSmallIntegerField(default=None, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка'),
        ),
    ]
