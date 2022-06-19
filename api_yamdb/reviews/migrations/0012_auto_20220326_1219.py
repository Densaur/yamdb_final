# Generated by Django 2.2.16 on 2022-03-26 09:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20220326_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('pub_date',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Категория произведения'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Жанр произведения'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Значение не может быть менее 1'), django.core.validators.MaxValueValidator(10, message='Значение не может быть более 10')], verbose_name='Оценка отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_title', to='reviews.Title', verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_titles', to='reviews.Category', verbose_name='Категория произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(to='reviews.Genre', verbose_name='Жанр произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.TextField(db_index=True, max_length=50, verbose_name='Наименование произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Рейтинг произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)], verbose_name='Год выпуска'),
        ),
    ]
