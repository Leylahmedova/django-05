from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name

# >>> total_price=Product.objects.annotate(total_price=Coalesce(F("price")-F("discount_price"),0,output_field=FloatField())).values("total_price")
# >>> total_price
# <QuerySet [{'total_price': 25.0}, {'total_price': 21.0}, {'total_price': 32.0}]>