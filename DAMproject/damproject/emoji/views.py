from .models import Image, User, Tag, Image2tag, Report
from django.http import HttpResponse
import json
from django.http import JsonResponse
import base64
import io
from PIL import Image as PImage, ImageSequence, ImageDraw
import random
import json
import datetime


def upload_img(request):
    try:
        if request.method == 'POST':
            email = request.POST.get("email")
            classification = request.POST.get("classification")
            tagstr = request.POST.get("tags")
            tags = json.loads(tagstr)
            img = request.POST.get("img")
            state = request.POST.get("state")
            private = request.POST.get("private")
            if private == "true":
                pri = 1
            else:
                pri = 0
            user = User.objects.get(email=email)
            img = Image.objects.create(classification=classification, img=img, private=pri, owner=user)
            for tag in tags:
                taginfo = Tag.objects.filter(content=tag)
                if taginfo.exists():
                    tagobj = taginfo.first()
                    tagobj.frequency += 1
                    tagobj.save()
                else:
                    Tag.objects.create(content=tag)
                tagobj = Tag.objects.get(content=tag)  # 再取一遍为了让数据库添加default项目
                imgobj = Image.objects.get(id=img.id)
                Image2tag.objects.create(image=imgobj, tag=tagobj)
            if state == "true":
                add_watermark(img.id, user.username)
            return HttpResponse("SUCCESS")
        else:
            return HttpResponse("不是POST")
    except:
        return HttpResponse("上传图片失败")


def download(request):
    try:
        img_id = request.POST.get("id")
        image = Image.objects.get(id=img_id)
        type = img_type(image.img)
        nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S') #添加时间戳防止命名重复
        print(str(nowTime) + '.' + type)
        data = {
            'filename': str(nowTime) + '.' + type
         }
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse("没有此图片")


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
                response['manager'] = user.manager
                return JsonResponse(response)
            else:
                return HttpResponse("密码错误")
        except:
            return HttpResponse("用户名错误")
    except:
        return HttpResponse("未收到数据")


# 收藏图片
def like_image(request):
    try:
        email = request.POST.get("email")
        # print(email)
        image_id = request.POST.get("id")
        state = request.POST.get("state")
        image = Image.objects.get(id=image_id)
        user = User.objects.get(email=email)
        # print(image_id, email, state)
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


# 主页按照类别获取图片
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
                if image.private:
                    continue
                images.append(get_image_info(image, email))
            data.append({classification_list[index]: images})
        return HttpResponse(json.dumps(data), content_type="application/json")
    except:
        return HttpResponse('Not received')


# 删除图片
def delete_image(request):
    print("delete")
    try:
        print("here")
        image_id = request.POST.get("id")
        Image.objects.get(id=int(image_id)).delete()
        users = User.objects.all()
        deletech = '#' + image_id + '#'
        for user in users:
            if deletech in user.like_images:
                user.like_images = user.like_images.replace('#' + image_id + '#', '')
                user.save()
        return HttpResponse('SUCCESS')
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
                for frame in ImageSequence.Iterator(image_origin):
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
                print("gifok")
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


# 获取单张图片对应的全部信息 包括喜欢状态 另，用户有可能没有喜欢自己上传的图片
def get_all_info(image, email):
    # print("xxx")
    if email == "99":
        print("99")
        state = False
        tagsobj = image.image2tag_set.all()
        tags = []
        for tagobj in tagsobj:
            tags.append(tagobj.tag.content)
        return {
            'id': image.id,
            'img': image.img,
            'upload_time': str(image.upload_time),
            'classification': image.classification,
            'tags': json.dumps(tags),
            'likes': str(image.total_likes),
            'thumbs': str(image.total_thumbs),
            'name': image.owner.username,
            'portrait': image.owner.portrait,
            'profile': image.owner.profile,
            'state': state
        }
    else:
        user = User.objects.get(email=email)
        if str(image.id) in user.like_images:
            state = True
        else:
            state = False
        tagsobj = image.image2tag_set.all()
        tags = []
        for tagobj in tagsobj:
            tags.append(tagobj.tag.content)
        return {
             'id': image.id,
             'img': image.img,
             'upload_time': str(image.upload_time),
             'classification': image.classification,
             'tags': json.dumps(tags),
             'likes': str(image.total_likes),
             'thumbs': str(image.total_thumbs),
             'name': image.owner.username,
             'portrait': image.owner.portrait,
             'profile': image.owner.profile,
             'state': state
        }


# 获取单张图片的信息
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
    tags = []
    for tagobj in tagsobj:
        tags.append(tagobj.tag.content)
    return {
        'id': image.id,
        'img': image.img,
        'tags': json.dumps(tags),
        'state': state,
        'classification': image.classification
    }


def get_by_classification(request):
    data = []
    class_ch = request.POST.get("classification")
    classification = int(class_ch)
    images = Image.objects.filter(classification=classification)
    if images:
        for i in images:
            if i.private:
                continue
            data.append(i.img.url)
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("暂无图片")


# 从全部图片中每一类别获取一张图片
def get_classification():
    classfication_list = []
    images = Image.objects.all()
    for image in images:
        if image.private:
            continue
        if image.classification not in classfication_list:
            classfication_list.append(image.classification)
    return classfication_list


# 获取某一类别的指定数目的图片
def get_number_image(classification, number):
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.private:
            continue
        if image.classification == classification and len(certain_classification) < int(number):
            certain_classification.append(image)
    return certain_classification


# 从用户上传的图片中每一类别获取一张图片
def get_user_classification(email):
    classfication_list = []
    user = User.objects.get(email=email)
    images = Image.objects.all()
    for image in images:
        if image.classification not in classfication_list and image.owner == user:
            classfication_list.append(image.classification)
    return classfication_list


# 按照类别获取用户喜欢的图片
def get_like_image(classification, email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        imgid = '#' + str(image.id) + '#'
        if image.classification == classification and imgid in user.like_images:
            certain_classification.append(get_all_info(image, email))
    return certain_classification


# 获取用户上传的某一类别图片
def get_user_upload(classification, email):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.private:
            continue
        if image.classification == classification and image.owner == user:
            certain_classification.append(image)
    return certain_classification


# 按照给定类别查找所有图片
def get_classification_images(classification, email):
    images = Image.objects.all()
    certain_classification = []
    for image in images:
        if image.private:
            continue
        if image.classification == classification:
            certain_classification.append(get_all_info(image, email))
    return certain_classification


# 获取用户喜欢的图片
def get_user_liked_image(email,key):
    user = User.objects.get(email=email)
    images = Image.objects.all()
    data = []
    for image in images:
        imgid = '#' + str(image.id) + '#'
        if imgid in user.like_images:
            if key == "all":
                data.append(get_all_info(image, email))
                continue
            if image.classification == key:
                data.append(get_all_info(image, email))
                continue
            tagsobj = image.image2tag_set.all()
            for tagobj in tagsobj:
                if tagobj.tag.content == key:
                    data.append(get_all_info(image, email))
                    break
    # print(user, like_image)
    return data


# 全站搜索 同时搜索标签和类别
def get_key_search(key, email):
    images = Image.objects.all()
    data = []
    for image in images:
        if image.private:
            continue
        if key == "all":
            data.append(get_all_info(image, email))
            continue
        if image.classification == key:
            data.append(get_all_info(image, email))
            continue
        tagsobj = image.image2tag_set.all()
        for tagobj in tagsobj:
            if tagobj.tag.content == key:
                data.append(get_all_info(image, email))
                break
    return data


def get_user_image(request):
    try:
        data = []
        type = request.POST.get('type')
        email = request.POST.get('email')
        email_user = request.POST.get('email_user')
        key = request.POST.get('key', default='all')
        print(type)
        # 全站搜索 同时搜索标签和类别
        if type == '0':
            data = get_key_search(key, email_user)
            return HttpResponse(json.dumps(data))
        # 用户收藏图片
        elif type == '1':
            data = get_user_liked_image(email_user,key)
            return HttpResponse(json.dumps(data))
        # 用户上传图片
        elif type == '2':
            user = User.objects.get(email=email)
            if user.manager:
                reports = Report.objects.all()
                for report in reports:
                    data.append(get_all_info(report.image, "99"))
            else:
                images = Image.objects.all()
                for image in images:
                    if image.owner == user:
                        data.append(get_all_info(image, email_user))
            return HttpResponse(json.dumps(data))
        # 搜索某类别图片
        elif type == '3':
            data = get_classification_images(key, email_user)
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse('No data')
    except:
        return HttpResponse('Not received')


# 堆排序，找出最受欢迎的图片（目前只支持收藏）
def most_popular(request):
    try:
        data = []
        email = request.POST.get('email')
        number = request.POST.get('number')
        popular = []
        id_list = []
        images = Image.objects.all()
        for image in images:
            if image.private:
                continue
            id_list.append(image.id)
            popular.append(image.total_likes + image.total_thumbs)  # 可以在此修改算法
        temp = []
        for i in range(int(number)):
            temp.append(popular.index(max(popular)))
            popular[popular.index(max(popular))] = -1
        index = []
        for i in temp:
            index.append(id_list[i])
        for i in index:
            image = Image.objects.get(id=i)
            data.append(get_all_info(image, email))
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse('Not received')


# 点赞
def thumb_image(request):
    try:
        # print(email)
        image_id = request.POST.get("id")
        # print(image_id)
        state = request.POST.get("state")
        image = Image.objects.get(id=image_id)
        # print(image_id, email, state)
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


def image_detail(request):
    try:
        image_id = request.POST.get("id")
        email = request.POST.get("email")
        image = Image.objects.get(id=image_id)
        user = User.objects.get(email=email)
        tagsobj = image.image2tag_set.all()
        tags = []
        for tagobj in tagsobj:
            tags.append(tagobj.tag.content)
        like = '#' + image_id + '#'
        if like in user.like_images:
            state = 1
        else:
            state = 0
        info = {
            'name': image.owner.username,
            'portrait': image.owner.portrait,
            'profile': image.owner.profile,
            'img': image.img,
            'upload_time': str(image.upload_time)[0:19],
            'likes': str(image.total_likes),
            'thumbs': str(image.total_thumbs),
            'tags': json.dumps(tags),
            'classfication': image.classification,
            'owner_email': image.owner.email,
            'state': state
        }
        return HttpResponse(json.dumps(info))
    except:
        return HttpResponse("没有这张图片")


# 猜你喜欢 从用户数据库里随机几个表情包 拿出它的推荐图片
def get_recommend(request):
    print("get_recommend")
    try:
        email = request.POST.get("email_user")
        user = User.objects.get(email=email)
        like_str = user.like_images
        like_list = like_str.split('#')
        for x in range(like_list.count('')):
            if '' in like_list:
                like_list.remove('')
        chosen = random.sample(like_list, round(len(like_list) * 0.3))
        recom_list = []
        num = 5
        for i in chosen:
            recom_list += recommend(int(i), num)
        recom_list = list(set(recom_list))
        data = []
        for img_id in recom_list:
            image = Image.objects.get(id=img_id)
            data.append(get_all_info(image, email))
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse("没有此用户")


# 表情包详情页推荐
def detail_recommend(request):
    try:
        data = []
        img_id = request.POST.get("id")
        number = request.POST.get("number")
        email = request.POST.get("email")
        image = Image.objects.get(id=img_id)
        recom_list = recommend(img_id, int(number))
        for i in recom_list:
            img = Image.objects.get(id=i)
            data.append(get_all_info(img, email))
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse("没有此图片")


# 推荐算法 通过一张图片推荐num张图片id
def recommend(img_id, num):
    image = Image.objects.get(id=img_id)
    image_url = image.img
    image_type = img_type(image_url)
    pic_path_target = './emoji/images/' + 'target.' + image_type
    with open(pic_path_target, 'wb') as f:
        f.write(base64.b64decode(image_url.split(',')[1]))
    img_all = Image.objects.all()
    similarity = []
    id_list = []
    Inf = 100000
    for img_com in img_all:
        if img_com.private:
            continue
        if img_com.id == img_id:
            similarity.append(1000)  # 绝对选不到我自己
            id_list.append(img_com.id)
        else:
            #print(img_com.id)
            id_list.append(img_com.id)
            image_url = img_com.img
            image_type = img_type(image_url)
            pic_path_com = './emoji/images/' + 'compare.' + image_type
            with open(pic_path_com, 'wb') as f:
                f.write(base64.b64decode(image_url.split(',')[1]))
            p_similarity = get_similarity(pic_path_target, pic_path_com)
            #print(p_similarity)
            tags_target = image.image2tag_set.all()
            tags_com = image.image2tag_set.all()
            p_tag = 0
            for tag_c in tags_com:
                for tag_t in tags_target:
                    if tag_t.tag.content == tag_c.tag.content:
                        p_tag += 1
                        break
            p_tag = len(tags_target) - p_tag
            similarity.append(p_tag * 5 + p_similarity) # 配比随便写的
    temp = []
    for i in range(num):
        temp.append(similarity.index(min(similarity)))
        similarity[similarity.index(min(similarity))] = Inf
    index = []
    for i in temp:
        index.append(id_list[i])
    return index


# 判断url类型
def img_type(image_url):
    if 'jpeg' in image_url:
        return 'jpeg'
    elif 'gif' in image_url:
        return 'gif'
    elif 'png' in image_url:
        return 'png'
    elif 'jpg' in image_url:
        return 'jpg'


#计算两张图片的相似度 差异值哈希算法 支持gif相互比较或者gif与其他图片比较
def get_similarity(target, compare):
    image_target = PImage.open(target)
    image_com = PImage.open(compare)
    return DHash.hamming_distance(image_target, image_com)


# 一般来说，汉明距离小于5，基本就是同一张图片
class DHash(object):
    @staticmethod
    def calculate_hash(image):
        difference = DHash.__difference(image)
        decimal_value = 0
        hash_string = ""
        for index, value in enumerate(difference):
            if value:
                decimal_value += value * (2 ** (index % 8))
            if index % 8 == 7:
                hash_string += str(hex(decimal_value)[2:].rjust(2, "0"))  # 不足2位以0填充。0xf=>0x0f
                decimal_value = 0
        return hash_string

    @staticmethod
    def hamming_distance(first, second):
        if isinstance(first, str):
            return DHash.__hamming_distance_with_hash(first, second)

        hamming_distance = 0
        image1_difference = DHash.__difference(first)
        image2_difference = DHash.__difference(second)
        for index, img1_pix in enumerate(image1_difference):
            img2_pix = image2_difference[index]
            if img1_pix != img2_pix:
                hamming_distance += 1
        return hamming_distance

    @staticmethod
    def __difference(image):
        resize_width = 9
        resize_height = 8
        smaller_image = image.resize((resize_width, resize_height))
        grayscale_image = smaller_image.convert("L")
        pixels = list(grayscale_image.getdata())
        difference = []
        for row in range(resize_height):
            row_start_index = row * resize_width
            for col in range(resize_width - 1):
                left_pixel_index = row_start_index + col
                difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])
        return difference

    @staticmethod
    def __hamming_distance_with_hash(dhash1, dhash2):
        difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
        return bin(difference).count("1")


def get_user_data(user):
    profile = user.profile
    if user.portrait == '':
        pic_path = './emoji/images/default.jpg'
        with open(pic_path, 'rb') as f:
            image_byte = f.read()
            image_base64 = str(base64.b64encode(image_byte), encoding='utf-8')
        portrait = 'data:image/jpg;base64' + ',' + image_base64

    else:
        portrait = user.portrait
    return {
        'username': user.username,
        'email': user.email,
        'profile': profile,
        'portrait': portrait,
        'private': user.private
    }


def get_user_info(request):
    try:
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        data = get_user_data(user)
        return HttpResponse(json.dumps(data))
    except:
        return HttpResponse("Email not received")


def modify_user_info(request):
    try:
        email = request.POST.get("email")
        username = request.POST.get("username")
        profile = request.POST.get("profile")
        portrait = request.POST.get("portrait")
        private = request.POST.get("private")
        user = User.objects.get(email=email)
        try:
            user.username = username
            user.profile = profile
            user.portrait = portrait
            user.private = private
            user.save()
            return HttpResponse("success")
        except:
            return HttpResponse("error")
    except:
        return HttpResponse("Email not received")


def decide_password(request):
    try:
        email = request.POST.get("email")
        password_old = request.POST.get("password_old")
        password_new = request.POST.get("password_new")
        user = User.objects.get(email=email)
        if user.password == password_old:
            user.password = password_new
            user.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    except:
        return HttpResponse("Data not received")


def report_image(request):
    try:
        img_id = request.POST.get("id")
        reason = request.POST.get("reason")
        image = Image.objects.get(id=int(img_id))
        img = Report.objects.create(image=image, reason=reason)
        return HttpResponse("SUCCESS")
    except:
        return HttpResponse("没有此图片")


def delete_report(request):
    try:
        reports = Report.objects.all()
        for report in reports:
            report.delete()
        return HttpResponse("SUCCESS")
    except:
        return HttpResponse("没删着啊大兄弟")


def is_private(request):
    try:
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        return HttpResponse(user.private)
    except:
        return HttpResponse("no such user")


def get_username(request):
    try:
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        return HttpResponse(user.username)
    except:
        return HttpResponse("no such user")


# Create your views here.