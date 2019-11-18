from .models import Image, User, Tag, Image2tag
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from django.http import JsonResponse
import heapq
import base64
import io
from PIL import Image as PImage, ImageSequence, ImageDraw


def upload_img(request):
    try:
        if request.method == 'POST':
            email = request.POST.get("email")
            classification = request.POST.get("classification")
            tagstr = request.POST.get("tags")
            img = request.POST.get("img")
            state = request.POST.get("state")
            user = User.objects.get(email=email)
            # print("ok")
            img = Image.objects.create(classification=classification, img=img, owner=user)
            # print("okk")
            tags = tagstr.split('#')
            tags.remove('')
            for tag in tags:
                taginfo = Tag.objects.filter(content=tag)
                if taginfo.exists():
                    tagobj = taginfo.first()
                    tagobj.frequency += 1
                    tagobj.save()
                else:
                    Tag.objects.create(content=tag)
                tagobj = Tag.objects.get(content=tag) #再取一遍为了让数据库添加default项目
                imgobj = Image.objects.get(id=img.id)
                Image2tag.objects.create(image=imgobj, tag=tagobj)
            # state = True
            if state == True:
                print("ok")
                add_watermark(img.id, user.username)
            return HttpResponse("SUCCESS")
        else:
            return HttpResponse("不是POST")
    except:
        return HttpResponse("上传图片失败")


def create_user(request):
    try:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        userinfo = User.objects.filter(email=email)
        if userinfo:
            return HttpResponse("Exist")
        else:
            User.objects.create(username=username, email=email, password=password)
            return HttpResponse("SUCCESS")
    except:
        return HttpResponse("未收到数据")


def login(request):
    try:
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)

            if user.password == password:
                response = {}
                response['msg'] = 'SUCCESS'
                response['username'] = user.username
                return JsonResponse(response)
            else:
                return HttpResponse("密码错误")
        except:
            return HttpResponse("用户名错误")
    except:
        return HttpResponse("未收到数据")


#收藏图片
def like_image(request):
    try:
        email = request.POST.get("email")
        print(email)
        image_id = request.POST.get("id")
        print(image_id)
        #email = request.POST.get("email")
        state = request.POST.get("state")
        image = Image.objects.get(id=image_id)
        user = User.objects.get(email=email)
        print(image_id, email, state)
        if state == "true":
            image.total_likes += 1
            user.like_images += '#' + image_id + '#'
            image.save()
            user.save()
            return HttpResponse("SUCCESS")
        else:
            image.total_likes -= 1
            user.like_images = user.like_images.replace('#' + image_id + '#', '')
            image.save()
            user.save()
            return HttpResponse("SUCCESS")
    except:
        return HttpResponse("未收到数据")


#主页按照类别获取图片
def get_images(request):
    try:
        data = []
        email = request.POST.get('email')
        number = request.POST.get('number')
        classification_list = get_classification()
        for index in range(len(classification_list)):
            certain_classification = get_number_image(classification_list[index], number)
            images = []
            for image in certain_classification:
                images.append(get_image_info(image, email))
            data.append({classification_list[index]: images})
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponse('Not received')


#删除图片
def delete_image(request):
    try:
        image_id = request.POST.get("id")
        Image.objects.get(id=image_id).delete()
        return HttpResponse("SUCCESS")
    except:
        return HttpResponse("Image not Received")


def add_watermark(image_id, username):
    try:
        if username == '':
            return HttpResponse("Username not received")
        else:
            image = Image.objects.get(id=image_id)
            image_url = image.img
            if 'jpeg' in image_url:
                image_type = 'jpeg'
            elif 'gif' in image_url:
                image_type = 'gif'
            elif 'png' in image_url:
                image_type = 'png'
            elif 'jpg' in image_url:
                image_type = 'jpg'
            else:
                return HttpResponse("Unresolved image type")
            pic_path = './emoji/images/' + str(image_id) + '.' + image_type
            with open(pic_path, 'wb') as f:
                f.write(base64.b64decode(image_url.split(',')[1]))
            image_origin = PImage.open(pic_path)
            if image_type == 'gif':
                frames = []
                for frame in ImageSequence.Iterator(image):
                    text = '@' + username
                    layer = frame.convert('RGBA')
                    text_overlayer = PImage.new('RGBA', layer.size, (255, 255, 255, 0))
                    image_draw = ImageDraw.Draw(text_overlayer)
                    text_size_x, text_size_y = image_draw.textsize(text)
                    text_xy = (layer.size[0] - text_size_x, layer.size[1] - text_size_y)
                    image_draw.text(text_xy, text, fill=(0, 0, 0, 50))
                    temp = PImage.alpha_composite(layer, text_overlayer)
                    frame = temp.convert('RGB')
                    b = io.BytesIO()
                    frame.save(b, format="GIF")
                    frame = PImage.open(b)
                    frames.append(frame)
                frames[0].save(pic_path, save_all=True, append_images=frames[1:])
                with open(pic_path, 'rb') as f:
                    image_byte = f.read()
                    image_base64 = str(base64.b64encode(image_byte), encoding='utf-8')
                image.img = image_url.split(',')[0] + ',' + image_base64
                image.save()
            else:
                text = '@' + username
                layer = image_origin.convert('RGBA')
                text_overlayer = PImage.new('RGBA', layer.size, (255, 255, 255, 0))
                image_draw = ImageDraw.Draw(text_overlayer)
                text_size_x, text_size_y = image_draw.textsize(text)
                text_xy = (layer.size[0] - text_size_x, layer.size[1] - text_size_y)
                image_draw.text(text_xy, text, fill=(0, 0, 0, 50))
                result = PImage.alpha_composite(layer, text_overlayer)
                result = result.convert('RGB')
                result.save(pic_path)
                with open(pic_path, 'rb') as f:
                    image_byte = f.read()
                    image_base64 = str(base64.b64encode(image_byte), encoding='utf-8')
                # print(image_url.split(',')[0], "ttt")
                image.img = image_url.split(',')[0] + ',' + image_base64
                image.save()
            return HttpResponse(image.img)
    except:
        return HttpResponse("Data not received")


#获取单张图片对应的全部信息 包括喜欢状态 另，用户有可能没有喜欢自己上传的图片
def get_all_info(image, email):
    print("xxx")
    if email == "99":
        print("99")
        state = False
        tagsobj = image.image2tag_set.all()
        tags = ''
        for tagobj in tagsobj:
            tags += '#' + tagobj.tag.content
        return {
            'id': image.id,
            'img': image.img,
            'classification': image.classification,
            'tags': tags,
            'state': state
        }
    else:
        user = User.objects.get(email=email)
        if str(image.id) in user.like_images:
            state = True
        else:
            state = False
        tagsobj = image.image2tag_set.all()
        tags = ''
        for tagobj in tagsobj:
            tags += '#' + tagobj.tag.content
        return {
            'id': image.id,
            'img': image.img,
            'classification': image.classification,
            'tags': tags,
            'state': state
        }


#获取单张图片的信息
def get_image_info(image, email):
    try:
        user = User.objects.get(email=email)
        if str(image.id) in user.like_images:
            state = True
        else:
            state = False
    except:
        state = False
    tagsobj = image.image2tag_set.all()
    tags = ''
    for tagobj in tagsobj:
        tags += '#' + tagobj.tag.content
    return {
        'id': image.id,
        'img': image.img,
        'tags': tags,
        'state': state
    }


def get_by_classification(request):
    data = []
    class_ch = request.POST.get("classification")
    classification = int(class_ch)
    images = Image.objects.filter(classification=classification)
    if images:
        for i in images:
            data.append(i.img.url)
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("暂无图片")


#从全部图片中每一类别获取一张图片
def get_classification():
    classfication_list = []
    images = Image.objects.all()
    for image in images:
        if image.classification not in classfication_list:
            classfication_list.append(image.classification)
    return classfication_list


#获取某一类别的指定数目的图片
def get_number_image(classification, number):
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.classification == classification and len(certain_classification) < int(number):
            certain_classification.append(image)
    return certain_classification


#从用户上传的图片中每一类别获取一张图片
def get_user_classification(email):
    classfication_list = []
    print("x", email)
    user = User.objects.get(email=email)
    images = Image.objects.all()
    for image in images:
        if image.classification not in classfication_list and image.owner == user:
            classfication_list.append(image.classification)
    return classfication_list


#按照类别获取用户喜欢的图片
def get_like_image(classification, email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        imgid = '#' + str(image.id) + '#'
        if image.classification == classification and imgid in user.like_images:
            certain_classification.append(get_all_info(image, email))
    return certain_classification


#获取用户上传的某一类别图片
def get_user_upload(classification, email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.classification == classification and image.owner == user:
            certain_classification.append(image)
    return certain_classification


#按照给定类别查找所有图片
def get_classification_images(classification, email):
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.classification == classification:
            certain_classification.append(get_all_info(image, email))
    return certain_classification


#获取用户喜欢的图片
def get_user_liked_image(email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    like_image = []
    for image in images:
        imgid = '#' + str(image.id) + '#'
        if imgid in user.like_images:
            like_image.append(get_all_info(image, email))
    print(user, like_image)
    return like_image


#全站搜索 同时搜索标签和类别
def get_key_search(key, email):
    images = Image.objects.all()
    data = []
    for image in images:
        if key == "all":
            data.append(get_all_info(image, email))
            continue
        if image.classification == key or key in image.tags:
            data.append(get_all_info(image, email))
    return data


def get_user_image(request):
    try:
        data = []
        type = request.POST.get('type')
        email = request.POST.get('email', default='')
        email_user = request.POST.get('email_user')
        key = request.POST.get('key', default='all')
        print(type)
        #全站搜索 同时搜索标签和类别
        if type == '0':
            data = get_key_search(key, email_user)
            return HttpResponse(json.dumps(data))
        #用户收藏图片
        elif type == '1':
            data = get_user_liked_image(email_user)
            return HttpResponse(json.dumps(data))
        #用户上传图片
        elif type == '2':
            images = Image.objects.all()
            user = User.objects.get(email=email_user)
            for image in images:
                if image.owner == user:
                    data.append(get_all_info(image, email_user))
            return HttpResponse(json.dumps(data))
        #搜索某类别图片
        elif type == '3':
            data = get_classification_images(key, email_user)
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse('No data')
    except:
        return HttpResponse('Not received')


#堆排序，找出最受欢迎的图片（目前只支持收藏）
def most_popular(request):
    try:
        data = []
        email = request.POST.get('email')
        number = request.POST.get('number')
        popular = []
        images = Image.objects.all()
        for image in images:#按照id将流行度存入 注意id从1开始 列表从0开始
            popular += image.total_likes + image.total_thumbs #可以在此修改算法
        #堆排序获得最大的number张图片并获得id
        max_index = map(popular.index, heapq.nlargest(number, popular))
        for i in list(max_index):
            image = Image.objects.get(id=i+1)
            data.append(get_all_info(image, email))
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse('Not received')


#点赞
def thumb_image(request):
    try:
        email = request.POST.get("email")
        print(email)
        image_id = request.POST.get("id")
        print(image_id)
        state = request.POST.get("state")
        image = Image.objects.get(id=image_id)
        user = User.objects.get(email=email)
        print(image_id, email, state)
        if state == "true":
            image.total_thumbs += 1
            image.save()
            return HttpResponse("SUCCESS")
        else:
            image.thumbs -= 1
            image.save()
            return HttpResponse("SUCCESS")
    except:
        return HttpResponse("未收到数据")

# Create your views here.