# Generated by Django 5.1.7 on 2025-03-31 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('book_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
            ],
        ),
    ]
