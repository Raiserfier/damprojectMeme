<template>
  <div>
    <div class="main_window">
      <div class="pic_inf">
        <div class="pic_window">
          <div class="pic_show">
            <img :src="img" alt="" :style="{width:650+'px', height:'auto'}">
          </div>
        </div>
        <div class="info_window">
          <div class="Uploader">
            <div class="Userpic_window">
              <a class="User_pic" :src="portrait" @click="to_owner_channel"
                 :style="{'background-image':'url'+'(\'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3900046848,1834418761&fm=26&gp=0.jpg\')'}"></a>
              <h2 class="User_name" @click="to_owner_channel">{{name}}</h2>
              <h5 style="font-size: 10px;padding-top: 10px;color: gray;">上传于：{{up_time}}</h5>
            </div>
            <div>
              <p class="user_introduction">
                {{profile}}
              </p>
            </div>
          </div>
          <!--          <div class="info_line"><i class="icon fa-clock-o"></i><span>{{up_time}}</span></div>-->
          <!--          <div class="info_line"><i class="icon fa-heart"></i><span>{{favorites}}</span></div>-->
          <!--          <div class="info_line"><i class="icon fa-star"></i><span>{{collects}}</span></div>-->
          <!--          <div class="info_line"><i class="icon fa-star"></i><span>-->
          <!--            <li @click="report">-->
          <!--              <p>举报</p>-->
          <!--            </li>-->
          <!--          </span></div>-->
          <div><a href="#" class="hvr-sweep-to-right button11" :class="{Liked_b:isLike}" @click="thumb_click($event)"><i class="icon fa-thumbs-up"></i>{{favorites}}</a></div>
          <div><a href="#" class="hvr-sweep-to-right button11" :class="{Collected_b:isCollect}" @click="fav_click($event)"><i class="icon fa-star"></i>{{collects}}</a></div>
          <div><a href="#" class="hvr-sweep-to-right button11" @click="download" style="padding-top: 10px;">下载</a></div>
          <div><a href="#" class="hvr-sweep-to-right button11" @click="report" style="padding-top: 10px;">举报</a></div>
        </div>
      </div>
    </div>
    <div>
      <div>
        <div class="tags">
          <div class="taglist">
            <a v-for="tag in JSON.parse(tags)" class="TAG" href=""><h3 class="TAG_title">{{'#'+tag}}</h3></a>
          </div>
        </div>
        <div class="commend_title">
          <span>相似推荐</span>
        </div>
        <!-- 推荐图片瀑布流-->
        <details-recommend></details-recommend>
      </div>
    </div>
  </div>
</template>

<script>

    import ImageStream from './ImagePage/ImageStream'

    export default {
        name: "PicDetail",
        components: {
            'details-recommend': ImageStream
        },
        data() {
            return {
                img_id: 0,
                img: '',
                tags: [],
                up_time: '',
                collects: 0,
                favorites: 0,
                test_path: require('../assets/test/1.jpg'),
                name: '游客',
                profile: '',
                portrait: '',

                isLike: false,
                isCollect: false,

                path: '',
                filename: '',
                owner_email: '',
            }
        },
        created() {
            if (this.$route.params.pic !== undefined) {
                this.img_id = this.$route.params.pic;
                this.$api.post('/image_detail', {id: this.$route.params.pic}).then(response => {
                    console.log(response.data);
                    if (response.data !== '没有这张图片') {
                        this.up_time = response.data.upload_time;
                        this.collects = response.data.likes;
                        this.favorites = response.data.thumbs;
                        this.tags = response.data.tags;
                        this.img = response.data.img;
                        this.name = response.data.name;
                        this.portrait = response.data.portrait;
                        this.profile = response.data.profile;
                        this.owner_email = response.data.owner_email;
                        console.log(this.owner);
                    } else {
                        this.$message.warning('图片信息获取失败');
                    }
                }), (response) => {
                    this.$message.error('图片信息获取失败');
                }
            }//用户页
        },
        methods: {
            download() {
                let FileSaver = require('file-saver');
                this.$api.post('/download', {
                    id: this.$route.params.pic,
                }).then(response => {
                    this.filename = response.data.filename;
                    const regex = new RegExp('^data:([^/]+/([^;]+));base64');
                    const b64Data = this.img.replace(regex, '$1,$2').split(',');
                    const contentType = b64Data[0];
                    // 解码
                    const raw = window.atob(b64Data[2]);
                    const rawLength = raw.length;
                    //const fileName = `文件名.${b64Data[1]}`;
                    let uInt8Array = new Uint8Array(rawLength);
                    console.log("hello");
                    for (let i = 0; i < rawLength; ++i)
                        uInt8Array[i] = raw.charCodeAt(i);
                    const blob = new Blob([uInt8Array], {type: contentType});
                    console.log(this.filename, contentType)
                    FileSaver.saveAs(blob, this.filename);
                    this.$message.success('下载成功！');
                }), (response) => {
                    this.$message.error('下载失败！');
                }
            },
            //点赞
            thumb_click(e) {
                let flag = true;
                if (!this.isLike) {
                    this.isLike = true;
                    this.favorites = parseInt(this.favorites) + 1;
                } else {
                    this.isLike = false;
                    this.favorites = parseInt(this.favorites) - 1;
                    flag = false;
                }
                this.$api.post('/thumb_image', {
                    id: this.$route.params.pic,
                    state: flag,
                }).then(response => {
                    console.log('1111111' + response.data);
                    if (response.data === 'SUCCESS') {
                        this.$message.success('点赞成功！');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('点赞失败！');
                }
            },
            //收藏
            fav_click(e) {
                let flag = true;
                if (!this.isCollect) {
                    this.isCollect = true;
                    this.collects = parseInt(this.collects) + 1;
                } else {
                    this.isCollect = false;
                    this.collects = parseInt(this.collects) - 1;
                    flag = false;
                }
                this.$api.post('/like_image ', {
                    id: this.$route.params.pic,
                    state: flag,
                }).then(response => {
                    console.log('2222222' + response.data);
                    if (response.data === 'SUCCESS') {
                        //改变按钮状态
                        this.$message.success('收藏成功！');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('收藏失败！');
                }
            },
            to_owner_channel() {
                console.log("router", this.owner_email);
                this.$api.post('/is_private', {
                    email: this.owner_email
                }).then(response => {
                    if (response.data !== "no such user") {
                        if (response.data !== 1)
                            this.$router.replace({path: '/channel/' + this.owner_email + '/all' + '/hot'});
                        else
                            this.$message.error('对方主页不开放');
                    }
                }), (response) => {
                    this.$message.error('举报失败！');
                }
            },
            report() {
                this.$api.post('/report_image', {
                    id: this.$route.params.pic,
                    reason: ""
                }).then(response => {
                    if (response.data === 'SUCCESS') {
                        this.$message.success('举报成功！');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('举报失败！');
                }
            }
        }
    }
</script>

<style scoped>
  .main_window {
    /*float: left;*/
    margin-left: 200px;
    margin-top: 100px;
    /*position: relative;*/
    display: flex;
  }

  .pic_inf {
    color: #fff;
    margin: 0 25px 16px;
    padding-top: 24px;
    position: relative;
    text-align: left;
    vertical-align: baseline;
    border-width: 0px;
    border-style: initial;
    border-color: initial;
    border-image: initial;
    font: inherit;
  }

  .pic_window {
    float: left;
    margin: 0 0 16px;
    position: relative;
    width: 650px;
    vertical-align: top;
  }

  .pic_show {
    position: relative;
    width: 650px;
    height: auto;
    left: 0px;
    top: 0px;
    display: block;
  }

  .info_window {
    float: right;
    margin-left: 100px;
    margin-bottom: 16px;
    vertical-align: top;
    width: 248px;
  }

  .info_line {
    cursor: text;
    display: block;
    font-size: 14px;
    font-weight: 400;
    height: 36px;
    line-height: 36px;
  }

  .icon {
    display: inline-block;
    line-height: 40px;
    margin-right: 10px;
    float: none;
  }

  .tags {
    margin-bottom: 60px;
  }

  .taglist {
    text-align: left;
    margin-left: 225px;
  }

  .TAG {
    display: inline-block;
    padding: 0 16px;
    background-color: #313131;
    border-radius: 20px;
    margin: 0 8px 8px 0;
    line-height: 38px;
    height: 40px;
    overflow: visible;
    -webkit-animation-name: _3iN4SuT6M9MsNeKsTT3PbQ;
    animation-name: _3iN4SuT6M9MsNeKsTT3PbQ;
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    font-style: italic;
    font-size: 15px;
    letter-spacing: .04em;
    text-decoration: none;
    color: white;
  }

  .TAG:hover {
    color: #00E6CC;
    background-color: #55534f;
  }

  .TAG_title {
    margin: 0;
    font-size: 15px;
    text-transform: lowercase;
    text-align: left;
    font-weight: 700;
  }

  .Uploader {
    margin: 0 0 10px;
  }

  .Userpic_window {
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -webkit-flex-direction: column;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-pack: center;
    -webkit-justify-content: center;
    -ms-flex-pack: center;
    justify-content: center;
    min-height: 50px;
    padding-left: 60px;
    position: relative;
    text-align: left;
    -webkit-font-smoothing: antialiased;
  }

  .User_pic {
    background-position: 50%;
    background-repeat: no-repeat;
    background-size: cover;
    width: 50px;
    height: 50px;
    position: absolute;
    left: 0;
    top: 0;
    -webkit-box-flex: 0;
    -webkit-flex: 0;
    -ms-flex: 0;
    flex: 0;
  }

  .User_name {
    font-size: 16px;
    font-weight: 900;
    line-height: 1.1;
    width: 100%;
    cursor: pointer;
  }

  .User_name a {
    text-decoration: none;
  }

  .Liked {
    color: rgb(238, 106, 132);
    transition: all 0.2s ease-in-out;
  }

  .Liked_b {
    background: rgb(238, 106, 132);
    transition: all 0.5s ease-in-out;
  }

  .Collected {
    color: rgb(238, 203, 106);
    transition: all 0.2s ease-in-out;
  }

  .Collected_b {
    background: rgb(238, 203, 106);
    transition: all 0.5s ease-in-out;
  }

  .LabelsOver {
    visibility: visible;
    opacity: 1;
    -webkit-transform: translateY(100%);
    transform: translate(0, 25%) !important;
    transition: all 0.3s ease-in-out;
  }

  .LabelsOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(100%);
    -webkit-transform: translateY(100%);
    -ms-transform: translateY(100%);
    transform: translateY(20px) !important;
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out;
  }

  .IconOver {
    visibility: visible;
    opacity: 1;
    -webkit-transform: translate(0, -100%);
    transform: translate(0, 25%) !important;
    transition: all 0.3s ease-in-out;
  }

  .IconOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(-100%);
    -webkit-transform: translateY(-100%);
    -ms-transform: translateY(-100%);
    transform: translateY(-10%) !important;
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out
  }

  .thumbnails .v-waterfall-content {
    width: 90%;
    height: 90%;
    position: absolute;
  }

  .thumbnails .v-waterfall-content .v-waterfall-item {
    float: left;
    position: absolute;
  }

  .v-waterfall-item img {
    width: 90%;
    height: auto;
  }

  .icons .icon {
    float: right;
    margin-right: 0;
  }

  .Title {
    font-size: 16px;
    font-weight: 600;
    line-height: 1.1;
    width: 100%;
    margin-left: 200px;
    margin-bottom: 15px;
  }

  .user_introduction {
    color: #b2b2b2;
    font-size: 12px;
    line-height: 19px;
    -webkit-transition: max-height .5s cubic-bezier(0.165, 0.84, 0.44, 1);
    transition: max-height .5s cubic-bezier(0.165, 0.84, 0.44, 1);
    padding-top: 20px;
    background-color: #202024;
    cursor: default;
    box-shadow: none;
    text-align: left;
    margin: 0 0 15%;
  }

  a.hvr-sweep-to-right {
    border-radius: 0 5px 5px 0;
    font-family: inherit;
    font-size: 14px;
    font-weight: bold;
    display: inline-block;
    vertical-align: middle;
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
    box-shadow: 0 0 1px rgba(0, 0, 0, 0);
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    -moz-osx-font-smoothing: grayscale;
    position: relative;
    -webkit-transition-property: color;
    transition-property: color;
    -webkit-transition-duration: 0.3s;
    transition-duration: 0.3s;
    /*background: #3598dc;*/
    /*background: #202024;*/
    color: #fff;
  }

  a.button11 {
    /* display: inline-block; */
    /* vertical-align: middle; */
    border-radius: 0 5px 5px 0;
    margin-right: 6px;
    padding: 0.4em 1em 1em 1em;
    cursor: pointer;
    text-decoration: none;
    font-size: 1.2em;
    color: #fff;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    height: 50px;
    width: 160px;
    text-align: center;
  }

  a.hvr-sweep-to-right:hover:before {
    -webkit-transform: scaleX(1);
    transform: scaleX(1);
  }

  a.hvr-sweep-to-right:hover, a.hvr-sweep-to-right:focus, a.hvr-sweep-to-right:active {
    color: white;
  }

  a.hvr-sweep-to-right:before {
    border-radius: 0 5px 5px 0;
    content: "";
    position: absolute;
    z-index: -1;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(97, 87, 255, 0.8);
    -webkit-transform: scaleX(0);
    transform: scaleX(0);
    -webkit-transform-origin: 0 50%;
    transform-origin: 0 50%;
    -webkit-transition-property: transform;
    transition-property: transform;
    -webkit-transition-duration: 0.3s;
    transition-duration: 0.3s;
    -webkit-transition-timing-function: ease-out;
    transition-timing-function: ease-out;
  }

  .commend_title {
    margin-left: 225px;
    font-family: inherit;
    font-size: 20px;
    font-weight: 500;
    margin-bottom: 15px;
  }

</style>
