# Generated by Django 2.2.16 on 2022-03-25 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20220324_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_published'),
        ),
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='single_review_per_user'),
        ),
    ]
