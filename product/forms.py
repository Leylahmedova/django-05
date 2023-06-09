from django import forms
from .models import Product
# class BlogForm(forms.Form):
#     author_name=forms.CharField()
#     title=forms.CharField()
#     content=forms.Textarea()


class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields=("name","description")