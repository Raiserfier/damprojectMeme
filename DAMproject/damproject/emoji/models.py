from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, default='')
    password = models.CharField(max_length=20)
    like_images = models.TextField(default='')


class Image(models.Model):
    classification = models.CharField(default='', max_length=200)
    total_likes = models.IntegerField(default=0)
    total_thumbs = models.IntegerField(default=0)
    upload_time = models.DateTimeField(auto_now_add=True)
    img = models.CharField(default='', max_length=5000000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='')


class Tag(models.Model):
    content = models.CharField(default='', max_length=20)
    frequency = models.IntegerField(default=1)


#为多对多关系设置更加灵活的中间表结构
class Image2tag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default='')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default='')


# Create your models here.
