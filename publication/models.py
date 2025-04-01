from django.db import models

# Create your models here.
class Publication(models.Model):
    name=models.CharField(max_length=255,blank=True)
    rating=models.IntegerField()
    book_name=models.CharField(max_length=255)
    description=models.TextField(max_length=500)
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()