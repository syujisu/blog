from django.shortcuts import render
from .models import blog
from .models import Pictures

def home2(request):
    blog = Pictures.objects
    return render(request, 'home2.html', {'blog :blog'})
# Create your views here.
