# Generated by Django 2.2.7 on 2019-11-19 15:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizz_nbq'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='moyenne_generale',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]
