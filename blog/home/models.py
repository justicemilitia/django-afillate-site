from django.db import models

class Product(models.Model):

    content = models.TextField(verbose_name='Content')
    title = models.CharField(max_length=500,verbose_name='Title')
    link = models.CharField(max_length=2000,verbose_name='Link')
    image = models.CharField(max_length=200,verbose_name='Image')
    slug = models.CharField(max_length=200,verbose_name='Slug')
    published = models.DateTimeField(verbose_name='Published Date')
    price = models.CharField(max_length=30,verbose_name='Price')
    sort = models.CharField(max_length=15,verbose_name='Sort')
    urli = models.CharField(max_length=250,verbose_name='Urli')
    

def __str__(self):
    return self.title


