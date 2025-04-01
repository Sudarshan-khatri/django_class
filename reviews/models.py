from django.db import models

# Create your models here.
class Reviews(models.Model):
    name=models.CharField(max_length=255,null=False)
    rating=models.IntegerField()
    book_name=models.CharField(max_length=255,null=False)
    description=models.TextField(max_length=500)
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()
