# Generated by Django 5.1.7 on 2025-04-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_book_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
