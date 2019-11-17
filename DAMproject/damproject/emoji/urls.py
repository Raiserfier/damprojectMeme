from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'emoji'

urlpatterns = [
    path('create_user', views.create_user),
    path('login', views.login),
    path('get_by_classification', views.get_by_classification),
    path('get_images', views.get_images),
    path('get_user_image', views.get_user_image),
    path('upload_image', views.upload_img),
    path('get_image_info', views.get_image_info),
    path('get_image_info', views.get_image_info),
    path('like_image', views.like_image),
    path('get_image_info', views.get_image_info),
    path('thumb_image', views.thumb_image),
    path('add_watermark', views.add_watermark)
]
