# Generated by Django 5.0.4 on 2024-04-28 03:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0)]),
        ),
    ]
