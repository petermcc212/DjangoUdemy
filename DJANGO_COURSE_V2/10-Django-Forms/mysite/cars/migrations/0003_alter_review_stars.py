# Generated by Django 4.0 on 2022-01-09 06:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
