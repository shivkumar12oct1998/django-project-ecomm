from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=100)
    specs=models.CharField(max_length=100)
    rating= models.DecimalField(max_digits=10,decimal_places=1)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    bio=models.CharField(max_length=100)
    image=models.ImageField()
    stock=models.IntegerField(default=0)

    def __str__(self):
        return self.name