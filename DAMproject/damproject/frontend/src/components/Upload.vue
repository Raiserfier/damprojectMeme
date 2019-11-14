<template>
  <div class="upload-page">
    <section id="banner2" data-video="images/banner">
      <div class="inner">
        <header>
          <h1>Upload</h1>
          <p>Upload your GIF collection to share on Facebook, Twitter,<br/>
            Instagram, text message, email, and everywhere else.</p>
        </header>
      </div>
    </section>

    <!-- Main -->
    <section id="main">
      <!---->
      <div style="display: flex">
        <div class="UploadDIV">
          <div class="UploadInnerDIV">
            <div class="UploadBG"></div>
            <div class="UploadWords">
              <div class="Words">Browse Your Files</div>
              <span class="Words2">Uploads one or more Expression pack</span>
            </div>
          </div>
          <input id="Upfile" multiple type="file" accept="image/jpeg,image/png,image/gif"
                 ref="file" @change="choose_img($event)">
        </div>

        <div class="addTag">
          <div>
            <h2 class="addTagTit">添加分类</h2>
            <select class="selectTT" v-model="cate">
              <option v-for="op in options" v-bind:value="op.id">
                {{ op.name }}
              </option>
            </select>

          </div>

          <div>
            <h2 class="addTagTit addtag00">添加标签</h2>
            <div class="inputbox">
              <div class="arrbox">
                <div v-for="(item,index) in labelarr" :key="index" class="spanbox">
                  <span>{{item}}</span>
                  <i class="spanclose" @click="removeitem(index,item)"></i>
                </div>
                <input placeholder="输入标签" size="4" v-model="currentval" @keyup.enter="addlabel" class="input"
                       type="text"/>
              </div>
            </div>
          </div>


          <div class="uuppp"><!--上传按钮-->
            <form action="" method="post">
              <a class="uploadBT" @click="upload"><span>上传</span></a>
            </form>
          </div>
        </div>
      </div>

      <div class="UploadDDDD">
        <div v-for="imgs in up_img" class="Img-Upload">
          <div class="img_UploadBox">
            <!--            接受预览的img container-->
            <img :src="imgs" alt="user image" class="img-inputer">
          </div>
        </div>
        <!-- Footer -->
        <div>
          <footer id="footer">
            <p>&copy; Group 2. All rights reserved. Design: TEMPLATED.</p>
          </footer>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
    export default {
        name: "Upload",
        props: {
            parentarr: {
                type: Array,
                default() {
                    return []
                }
            }
        },
        data() {
            //select选中的值
            return {
                cate: 'chrome',
                options: [
                    {name: '动物', id: 'chrome'},
                    {name: '食物', id: 'safari'},
                    {name: '动画', id: 'Edge'},
                    {name: '游戏', id: 'firefox'},
                    {name: '人物', id: 'ie8'}
                ],
                currentval: '',
                labelarr: ["动物", "食物"],
                up_img: [],
                img_num: 0,
            }
        },
        created() {
            // this.get_op();
        },
        watch: {
            labelarr(old, cur) {
                this.$emit('on-change', this.labelarr)
            },
            parentarr() {
                if (this.parentarr.length > 0) {
                    this.labelarr = [];
                    for (let i = 0; i < this.parentarr.length; i++) {
                        this.labelarr.push(this.parentarr[i])
                    }
                } else {
                    this.labelarr = []
                }
            }
        },
        methods: {
            get_op() {

            },
            // 移除标签
            removeitem(index, item) {
                this.labelarr.splice(index, 1)
            },
            //添加标签
            // input回车加入labelarr中
            addlabel() {
                let count = this.labelarr.indexOf(this.currentval);
                if (count === -1) {
                    this.labelarr.push('#' + this.currentval)
                }
                this.currentval = ''
            },
            //选择图片
            choose_img(e) {
                this.img_num += e.target.files.length;
                for (let i = 0; i < e.target.files.length; i++) {
                    let reader = new FileReader();
                    let that = this;
                    console.log(e.target.files[i].type);
                    if (e.target.files[i].type === 'image/gif') {
                        reader.readAsDataURL(e.target.files[i]);
                        reader.onload = function (e) {
                            if (this.result.length > 5000000) {
                                that.$message.warning("图片 \"" + this.name + "\" 太大无法上传")
                            }
                            that.up_img.push(this.result);
                        }
                    } else {
                        reader.readAsDataURL(e.target.files[i]);
                        reader.onload = function (e) {
                            // console.log(this.result);
                            let image = new Image(); //新建一个img标签（还没嵌入DOM节点)
                            image.src = this.result;
                            image.onload = function () {
                                let canvas = document.createElement('canvas'), // 新建canvas
                                    context = canvas.getContext('2d');
                                let imageHeight = image.height, imageWidth = image.width, data = '';
                                if (image.height > image.width) {
                                    if (image.height > 250) {
                                        imageHeight = 250;
                                        imageWidth = image.width / image.height * 250;
                                    }
                                } else {
                                    if (image.width > 250) {
                                        imageWidth = 250;
                                        imageHeight = image.height / image.width * 250;
                                    }
                                }
                                canvas.width = imageWidth;
                                canvas.height = imageHeight;
                                context.drawImage(image, 0, 0, imageWidth, imageHeight);
                                data = canvas.toDataURL('image/jpeg'); // 输出压缩后的base64
                                // console.log(data);
                                that.up_img.push(data);
                            }
                        }
                    }
                    //这里push进去的东西应该还要再改？
                }
                console.log('共' + this.img_num + '张图片');
                // console.log(this.up_img);
            },
            //选择类别（这里是自动绑定的）
            choose_cate(e) {
                console.log("选中了", this.cate);
            },
            upload() {
                console.log(this.labelarr);
                let tags = '';
                for (let i = 0; i < this.labelarr.length; i++) {
                    tags += '#' + this.labelarr[i];
                }
                for (let i = 0; i < this.up_img.length; i++) {
                    this.$api.post('/upload_image', {
                        img: this.up_img,
                        email: this.$store.state.user_id,
                        tags: tags,
                        classification: this.cate
                    }).then(response => {
                        //console.log(response.data);
                        if (response.data === 'SUCCESS') {
                            this.$message.success('上传成功！');
                            //跳转到个人上传页
                            this.$route.replace({path: '/channel/' + this.my_id + '/all'});
                        }
                    }), (response) => {
                        //console.log("error");
                        this.$message.err('上传失败！');
                    }
                }
                this.up_img = [];
                this.labelarr = [];
            }

        }
    }
</script>

<style scoped>
    /*upload.css*/
    .UploadDDDD {
        padding-left: 19.5%;
        padding-right: 24%;
        padding-top: 100px;
    }

    .Img-Upload {
        padding-bottom: 120px;
        height: 230px;
        width: 25%;
        padding-right: 20px;
        float: left;
        top: 0;
        /*margin-top: 60px;*/
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        /*width: 250px;*/
        /*height: 250px;*/
        border-radius: 5px;
        /*background-color: rgba(26, 25, 29, 0.84);*/
    }

    .img_UploadBox {
        height: 200px;
        position: relative;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        width: 250px;
        /*height: 250px;*/
        border-radius: 5px;
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .img-inputer {
        position: relative;
        top: 0;
        z-index: 0;
        width: auto;
        height: 100%;
    }

    /* Banner */
    #banner2 {
        padding: 42.5px 1em 0 4em;
        min-height: 50vh;
        /*padding-top: 30px;*/
        -moz-align-items: center;
        -webkit-align-items: center;
        -ms-align-items: center;
        align-items: center;
        display: -moz-flex;
        display: -webkit-flex;
        display: -ms-flex;
        display: flex;
        -moz-justify-content: center;
        -webkit-justify-content: center;
        -ms-justify-content: center;
        justify-content: center;
        /*padding: 30px 1em 0 4em;*/
        border-top: 0;
        /*min-height: 35vh;*/
        background-image: url("../assets/images/Cage.jpg");
        background-position: center;
        background-size: cover;
        background-repeat: no-repeat;
        position: relative;
        text-align: center;
        overflow: hidden;
    }

    #banner2 .inner {
        padding-top: 4.25em;
        text-align: center;
        position: relative;
        z-index: 2;
    }

    #banner2 .inner p {
        box-shadow: none;
        background-color: rgba(255, 255, 255, 0);
    }

    #banner2 h1 {
        color: #fff;
        font-size: 5em;
        font-weight: 400;
        /*font-family: 'Passion One', cursive;*/
        margin: 0;
    }

    @media screen and (max-width: 980px) {

        #banner2 h1 {
            font-size: 5em;
        }

    }

    @media screen and (max-width: 736px) {

        #banner2 h1 {
            font-size: 3em;
        }

    }

    #banner2 p {
        color: rgba(255, 255, 255, 0.85);
        font-size: 1.5em;
        font-weight: 300;
    }

    @media screen and (max-width: 980px) {

        #banner2 p {
            font-size: 1.5em;
        }

    }

    @media screen and (max-width: 480px) {

        #banner2 p {
            font-size: 1.25em;
        }

    }

    #banner2 a {
        color: rgba(255, 255, 255, 0.75);
        text-decoration: none;
        border-bottom: 1px dotted;
    }

    #banner2 a:hover {
        color: #FFF;
        border: none;
    }

    #banner2 video {
        -moz-transform: translateX(50%) translateY(50%);
        -webkit-transform: translateX(50%) translateY(50%);
        -ms-transform: translateX(50%) translateY(50%);
        transform: translateX(50%) translateY(50%);
        position: absolute;
        bottom: 50%;
        right: 50%;
        width: auto;
        height: auto;
        min-width: 100%;
        min-height: 100%;
        overflow: hidden;
    }

    #banner2:before {
        -moz-transition: opacity 3s ease;
        -webkit-transition: opacity 3s ease;
        -ms-transition: opacity 3s ease;
        transition: opacity 3s ease;
        -moz-transition-delay: 1s;
        -webkit-transition-delay: 1s;
        -ms-transition-delay: 1s;
        transition-delay: 1s;
        content: '';
        background-color: #42424f;
        display: block;
        height: 100%;
        left: 0;
        opacity: 0.45;
        position: absolute;
        top: 0;
        width: 100%;
        z-index: 1;
    }

    #banner2 .avatar {
        border-radius: 100%;
        display: inline-block;
        margin: 0 0 2em 0;
        padding: 0.5em;
        border: solid 0px rgba(255, 255, 255, 0.25);
        background-color: rgba(255, 255, 255, 0.075);
    }

    #banner2 .avatar img {
        border-radius: 100%;
        display: block;
        width: 10em;
    }

    @media screen and (max-width: 1280px) {

        #banner2 video {
            display: none;
        }

    }

    @media screen and (max-width: 980px) {

        #banner2 br {
            display: none;
        }

    }

    @media screen and (max-width: 736px) {

        #banner2 {
            min-height: 0;
            padding: 6em 2em 4em 2em;
        }

        #banner2 br {
            display: none;
        }

    }

    body.is-loading #banner2:before {
        opacity: 1;
    }


    /*uploadDIV*/
    input.UploadDIV {
        width: 100%;
        height: 40px;
        font-size: 14px;
        font-weight: 400;
        line-height: normal;
        color: rgb(0, 0, 0);
        margin: 0 0 10px;
        padding: 0 10px;
        outline: none;
    }

    .UploadDIV {
        border-radius: 6px;
        min-height: 155px;
        max-width: 32em;
        background: rgba(152, 152, 152, 0.1);
        margin-left: 20em;
        margin-right: 5em;
        position: relative;
        -webkit-box-flex: 1;
        -webkit-flex: 1;
        -ms-flex: 1;
        flex: 1;
        display: flex;
    }

    .UploadDIV:hover {
        background: rgba(102, 102, 102, 0.4);
        box-shadow: inset 0 0 0 1px rgba(122, 122, 122, 0.25), 0 0 0.5em 0 #FF6382;
    }

    .UploadDIV input[type=file] {
        height: 100%;
        left: 0;
        opacity: 0;
        position: absolute;
        top: 0;
        width: 100%;
    }

    .UploadInnerDIV {
        display: flex;
        -webkit-box-align: center;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        margin: 45px 0;
    }

    .UploadBG {
        margin: 0 3em;
        flex-shrink: 0;
        width: 54px;
        height: 55px;
        background: url("../assets/images/add.png") no-repeat;
    }

    .UploadWords {
        align-self: center;
        margin-right: 60px;
        vertical-align: baseline;
    }

    .Words {
        font-weight: 700;
        font-size: 18px;
        text-transform: uppercase;
        padding-bottom: 4px;
    }

    .Words2 {
        font-size: 15px;
        letter-spacing: .3px;
        line-height: 20px;
    }

    /*AddLabel*/
    h2 {
        display: block;
        font-size: 1.5em;
        margin-block-start: 0.83em;
        margin-block-end: 0.83em;
        margin-inline-start: 0;
        margin-inline-end: 0;
        font-weight: bold;
        padding-bottom: 5px;
    }

    .addTag {
        text-align: left;
        opacity: 1;
        pointer-events: auto;
        box-sizing: border-box;
        vertical-align: top;
        padding-right: 30px;
        margin-left: 0;
        margin-right: 10px;
        position: relative;
        -webkit-box-flex: 1;
        -ms-flex: 1;
    }

    .addTag p {
        display: block;
        box-shadow: none;
        background: transparent;
        margin-block-start: 0;
        margin-block-end: 0;
        margin-inline-start: 0;
        margin-inline-end: 0;

    }

    .addTagTit {
        font-size: 16px;
        font-weight: 400;
        margin: 0;
        text-transform: none;
        font-family: nexablack, sans-serif;
        line-height: 1.45;
    }

    .addtag00 {
        margin-top: 20px;
    }

    .input_tags {
        border: 0;
        margin-top: 5px;
        font-size: 14px;
        border-bottom: solid 1px;
        text-shadow: none;
        border-radius: 6px;
        background: #ffffff;
        color: #343232;
        outline: none;
    }

    /*Upload_Button*/
    .uploadBT {
        border: none;
        outline: none;
        right: 9%;
        background: rgb(238, 106, 132);
        color: white;
        border-radius: 5px 5px 5px 5px;
        height: 33px;
        width: 300px;
        cursor: pointer;
        position: absolute;
        margin: 0;
        padding: 0 1em 0 1em;
        font-weight: 500;
        font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
        transition: all 0.3s;
        transition-duration: 0.2s;
        text-align: center;
        display: inline-block;
        font-size: 15px;

    }

    .uploadBT:hover {
        background: #ffffff;
        color: rgb(238, 106, 132);
    }

    .uuppp {
        display: flex;
        -webkit-box-align: center;
        -webkit-align-items: center;
        -ms-flex-align: center;
        align-items: center;
        margin: 30px 0;
    }

    /*Select*/
    select.selectTT {
        font-family: "微软雅黑", serif;
        background: rgba(44, 44, 47, 1);
        width: 300px;
        height: 40px;
        font-size: 14px;
        color: white;
        text-align: center;
        border: none;
        border-radius: 5px;
    }

    option {
        color: black;
        background: #ffffff;
        line-height: 20px;
        border-radius: 5px;
    }

    select:hover {
        box-shadow: 0 0 5px 1px #ffbec3;
        background-color: #2f2f2f;
    }

    select:focus {
        outline: none;
    }

    option:hover {
        background: #EBCCD1;
    }

    .inputbox {
        background-color: #2c2c2f;
        font-size: 12px;
        border-radius: 6px;
        margin-bottom: 18px;
        padding: 3px 1px 1px 3px;
        text-align: left;
        width: 300px;
        height: auto;
    }

    .inputbox:hover {
        box-shadow: 0 0 5px 1px #ffbec3;
        background-color: #2f2f2f;
    }

    .input {
        font-size: 14px;
        border: none;
        box-shadow: none;
        outline: none;
        background-color: transparent;
        padding: 0;
        width: auto !important;
        max-width: inherit;
        min-width: 80px;
        vertical-align: top;
        height: auto;
        color: rgba(207, 205, 205, 0.73);
        margin: 2px;
        line-height: 30px;
    }

    .arrbox {
        border-radius: 6px;
        margin-bottom: 10px;
        padding: 6px 1px 1px 6px;
        text-align: left;
        font-size: 0;
    }

    .spanbox {
        line-height: 30px;
        margin: 2px;
        padding: 0 10px;
        background-color: #4b4b4b;
        color: white;
        border-radius: 6px;
        font-size: 13px;
        cursor: pointer;
        display: inline-block;
        position: relative;
        vertical-align: middle;
        overflow: hidden;
        transition: 0.25s linear;
    }

    .spanbox:hover {
        padding: 0px 17px 0 3px;
    }

    .spanclose {
        color: white;
        padding: 0 10px 0 0;
        cursor: pointer;
        font-size: 12px;
        position: absolute;
        right: -3px;
        text-align: right;
        text-decoration: none;
        top: 0;
        width: 100%;
        bottom: 0;
        z-index: 2;
        opacity: 0;
        filter: "alpha(opacity=0)";
        transition: opacity 0.25s linear;
        font-style: normal;
    }

    .spanbox:hover .spanclose {
        padding: 0 10px 5px 0;
        opacity: 1;
        -webkit-filter: none;
        filter: none;
    }

    .spanclose:after {
        content: "x";
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        line-height: 27px;
    }
</style>
