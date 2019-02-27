from django.db import models
from imagekit.models import ImageSpecField # 썸네일 생성
from imagekit.processors import ResizeToFill # 크기조정
from .models import image
class Blog(models.Model):
    text = models.TextField()
# # Create your models here.

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    objects = models.Manager()

     # image에 해당하는 이미지 소스를 썸네일로 삼겠다. 바로 위 image 변수
    image_thumbnail = ImageSpecField(source='image/', processors=[ResizeToFill(120, 60)])