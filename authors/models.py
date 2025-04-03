from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255,null=False,blank=True)
    address=models.CharField(max_length=255,null=True)
    contact=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    book_published=models.DateTimeField(null=False)
    bio=models.TextField()
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()



    def _str_(self):
        return self.name
