from .models import Image, User
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from django.http import JsonResponse


def upload_img(request):
    try:
        if request.method == 'POST':
            email = request.POST.get("email")
            classification = request.POST.get("classification")
            tags = request.POST.get("tags")
            img = request.POST.get("img")
            print(email, classification, tags)
            # try:
            user = User.objects.get(email=email)
            print(img)
            Image.objects.create(classification=classification, tags=tags, img=img, owner=user)
            # img = Image(classification=classification, tags=tags, img=img, owner=user)
            # img.save()
            print("hdewjkhdek")
            return HttpResponse("SUCCESS")
            # except:
            # return HttpResponse("找不到该用户")
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
            return HttpResponse("SUCCEESS")
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
                # response.set_signed_cookie("login", 'yes', salt="DAM", max_age=60 * 60 * 12)
                # response.set_signed_cookie("username", user.username, salt="DAM", max_age=60 * 60 * 12)
                # response.set_signed_cookie("email address", email, salt="DAM", max_age=60 * 60 * 12)
                response['msg'] = 'SUCCESS'
                response['username'] = user.username
                return JsonResponse(response)
            else:
                return HttpResponse("密码错误")
        except:
            return HttpResponse("用户名错误")
    except:
        return HttpResponse("未收到数据")


def like_image(request):
    try:
        image_id = request.POST.get("id")
        email = request.POST.get("email")
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


def get_images(request):
    try:
        data = []
        email = request.POST.get('email')
        number = request.POST.get('number')
        print(email, number)
        classification_list = get_classification()
        print("1")
        for index in range(len(classification_list)):
            certain_classification = get_number_image(classification_list[index], number)
            images = []
            print("2")
            for image in certain_classification:
                images.append(get_image_info(image, email))
                print("3")
            data.append({classification_list[index]: images})
            print(classification_list[index])
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponse('Not received')


def get_all_info(image, email):
    print("xxx")
    if email == "99":
        print("99")
        state = False
        return {
            'id': image.id,
            'img': image.img,
            'classification': image.classification,
            'tags': image.tags,
            'state' : state
        }
    else:
        user = User.objects.get(email=email)
        # print(type(user.like_images))
        if str(image.id) in user.like_images:
            state = True
        else:
            state = False
        # print("ttt")
        return {
            'id': image.id,
            'img': image.img,
            'classification': image.classification,
            'tags': image.tags,
            'state': state
        }


def get_image_info(image, email):
    try:
        user = User.objects.get(email=email)
        if str(image.id) in user.like_images:
            state = True
        else:
            state = False
    except:
        state = False
    return {
        'id': image.id,
        'img': image.img,
        'tags': image.tags,
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


def get_classification():
    classfication_list = []
    images = Image.objects.all()
    for image in images:
        if image.classification not in classfication_list:
            classfication_list.append(image.classification)
    return classfication_list


def get_number_image(classification, number):
    images = Image.objects.all()
    certain_classification = []
    # print("ok")
    for image in images:
        # print(image.classification, classification, type(number), len(certain_classification))
        if image.classification == classification and len(certain_classification) < int(number):
            # print(image)
            certain_classification.append(image)
    return certain_classification


def get_user_classification(email):
    classfication_list = []
    print("x", email)
    user = User.objects.get(email=email)
    images = Image.objects.all()
    for image in images:
        if image.classification not in classfication_list and image.owner == user:
            classfication_list.append(image.classification)
    return classfication_list


def get_like_image(classification, email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        print(image.id)
        if image.classification == classification and image.id in user.like_images:
            certain_classification.append(image)
    return certain_classification


def get_certain_image(classification):
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.classification == classification:
            certain_classification.append(image)
    return certain_classification


def get_user_upload(classification, email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.classification == classification and image.owner == user:
            certain_classification.append(image)
    return certain_classification

def get_classification_images(classification, email):
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.classification == classification:
            certain_classification.append(get_all_info(image, email))
    return certain_classification

def get_user_liked_image(email):
    user = User.objects.get(email=email)
    #print(user)
    images = Image.objects.all()
    #print(images)
    like_image = []
    for image in images:
        imgid = '#' + str(image.id) + '#'
        if imgid in user.like_images:
            like_image.append(get_all_info(image, email))

    return like_image


def get_key_search(key, email):
    images = Image.objects.all()
    data = []
    for image in images:
        if key == "all":
            data.append(get_all_info(image, email))
            continue
        if image.classification == key or key in image.tags:
            print(key)
            data.append(get_all_info(image, email))
        print("done")
    print(data)
    return data


def get_user_image(request):
    try:
        data = []
        type = request.POST.get('type')
        email = request.POST.get('email', default='')
        email_user = request.POST.get('email_user')
        key = request.POST.get('key', default='all')
        print(type)
        if type == '0':
            data = get_key_search(key, email_user)
            print(data)
            return HttpResponse(json.dumps(data))
        elif type == '1':
            print("1ok")
            data = get_user_liked_image(email_user)
            print(data)
            return HttpResponse(json.dumps(data))
        elif type == '2':
            images = Image.objects.all()
            user = User.objects.get(email=email_user)
            for image in images:
                if image.owner == user:
                    print("x")
                    data.append(get_all_info(image, email_user))
                #print(data)
            return HttpResponse(json.dumps(data))
        elif type == '3':
            print("3ok")
            data = get_classification_images(key, email_user)
           # data.append({key: images})
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse('No data')
    except:
        return HttpResponse('Not received')


#search by tag 不知道穿上来的字符串是什么样的


# Create your views here.
