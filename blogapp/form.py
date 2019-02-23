# Blog class를 기반으로 만들 것이기 때문에 blog 안에 form.py를 만들어준 것! models.py 여기 있자너
from django import forms
from .models import Blog 

# 모델기반이 아니면 forms.Form
class BlogPost(forms.Form): 
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])



    #    class Meta:
    #     model = Blog
    #     fields = ['title', 'body']