from django.db import models
from datetime import datetime
# Create your models here.

x = [

    ('phone','phone'),
    ('laptop','laptop')

]



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    content = models.TextField(null=True, blank=True, verbose_name='description')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', default='product_images/2026/09/28/samsung23fe.png')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=100, null=True, blank=True, choices=x)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']


class Test(models.Model):
    name = models.DateField()
    time = models.TimeField(null=True)
    created_at = models.DateTimeField(default=datetime.now)