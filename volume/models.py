from django.db import models

# Create your models here.
class Volume(models.Model):
    v_name=models.CharField(max_length=255)
    created_date=models.DateTimeField()
    update_date=models.DateTimeField()


    def __str__(self):
        return self.v_name

