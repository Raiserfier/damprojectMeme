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
    path('get_user_info', views.get_user_info),
    path('modify_user_info', views.modify_user_info),
    path('decide_password', views.decide_password),
    path('detail_recommend', views.detail_recommend),
    path('get_recommend', views.get_recommend)
]
