from django.db import models

# Create your models here.

class Blog(models.Model):
    author_name=models.CharField(max_length=300)
    title=models.CharField(max_length=300)
    content=models.TextField(blank=True,null=True)
    updated_up=models.DateTimeField(auto_now=True,blank=True,null=True)
    created_up=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title

# >>> total_price=Product.objects.annotate(total_price=Coalesce(F("price")-F("discount_price"),0,output_field=FloatField())).values("total_price")
# >>> total_price
# <QuerySet [{'total_price': 25.0}, {'total_price': 21.0}, {'total_price': 32.0}]>