# Generated by Django 4.0.5 on 2022-06-26 20:01

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(validators=[accounts.validators.validate_birth], verbose_name='birthday'),
        ),
    ]
