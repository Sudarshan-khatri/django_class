# Generated by Django 5.1.7 on 2025-03-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='contact',
            field=models.PositiveIntegerField(),
        ),
    ]
