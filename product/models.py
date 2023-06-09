from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField( blank = True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def _str_(self):
        return self.name