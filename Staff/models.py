from django.db import models

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=30)
    ph_no=models.CharField(max_length=10)
    mail=models.EmailField()
    place=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='static/pics')
    def __str__(self):
        return self.name

