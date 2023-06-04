from django import forms
from .models import Blog
# class BlogForm(forms.Form):
#     author_name=forms.CharField()
#     title=forms.CharField()
#     content=forms.Textarea()


class BlogForm(forms.ModelForm):
    
    class Meta:
        model=Blog
        fields=("author_name","title","content")