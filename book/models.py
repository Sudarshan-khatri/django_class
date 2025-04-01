from django.db import models
from authors.models import Author
from volume.models import Volume
from publication.models import Publication
from reviews.models import Reviews
from django.utils import timezone
import uuid
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    Type_choice=(
         ('hardcopy','Hardcopy'),
         ('pdf','Pdf')
    )
    book_name=models.CharField(max_length=255,null=True)
    book_type=models.CharField(max_length=255,choices=Type_choice)

    slug=models.SlugField(max_length=25,unique=True,null=True)

    author=models.ForeignKey('authors.Author',on_delete=models.CASCADE,null=True,blank=True)
    vol=models.ForeignKey('volume.Volume',on_delete=models.CASCADE,null=True,blank=True)
    book_publication=models.ForeignKey('publication.Publication',on_delete=models.CASCADE,null=True,blank=True)
    book_review=models.ForeignKey('reviews.Reviews',on_delete=models.CASCADE,default=1)

    isbn=models.PositiveIntegerField()
    language=models.CharField(max_length=255,null=False)

    date=models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.book_name
    


    # slug and public id 
    def save(self,*args,**kwargs):
        self.slug=f"{slugify(self.book_name)}"
        super().save(*args,**kwargs)

    
