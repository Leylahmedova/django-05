from django.db import models
from ckeditor.fields import RichTextField
import os
from django.utils.text import slugify

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


def upload_to(instance,filename):
    
    return f"products/{instance.name.lower().replace(' ','-')}/{filename}"
def upload_to2(instance,filename):
    return f"companies/{instance.name.upper().replace(' ','@')}/{filename}"

class ProductImage(models.Model):
    name=models.CharField(max_length=200)
    description=RichTextField(blank=True,null=True)
    price = models.FloatField()
    image=models.ImageField(upload_to=upload_to)
    company_image=models.ImageField(upload_to=upload_to2)

    def _str_(self):
        return self.name
    

# image yukleneme pathi avtomatik olaraq bele olmalidir --> products/product obyektinin adi ama lowercase olaraq ve aralarda bosluq yerine tire/faylin adi
# company_logo yuklenme pathi avtomatik olaraq bele olmalidir --> companies/product obyektinin adi ama uppercase olaraq ve aralarda bosluq yerine @/faylin adi
