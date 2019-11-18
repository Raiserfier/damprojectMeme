<template>
  <!--  <div>-->
  <!--    <h2>pic_path</h2>-->
  <!--    <p>{{pic_path}}</p>-->
  <!--  </div>-->

  <div>
    <div class="main_window">
      <div class="pic_inf">
        <div class="pic_window">
          <div class="pic_show">
            <img :src="test_path" alt="" :style="{width:650+'px', height:'auto'}">
          </div>
        </div>
        <div class="info_window">
          <div class="Uploader">
            <div class="Userpic_window">
              <a href="" class="User_pic"
                 :style="{'border-radius':100+'%','background-image':'url'+'(\'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3900046848,1834418761&fm=26&gp=0.jpg\')'}"></a>
              <h2 class="User_name"><a href="">TESTER</a></h2>
            </div>
          </div>
          <div class="info_line"><i class="icon fa-clock-o"></i><span>Upload time</span></div>
          <div class="info_line"><i class="icon fa-heart"></i><span>Favorite</span></div>
          <div class="info_line"><i class="icon fa-star"></i><span>Collection</span></div>
        </div>
      </div>
    </div>
    <div>
      <div>
        <div class="tags">
          <div class="taglist">
            <a class="TAG" href=""><h3 class="TAG_title">#aaa</h3></a>
            <a class="TAG" href=""><h3 class="TAG_title">#aaa</h3></a>
            <a class="TAG" href=""><h3 class="TAG_title">#aaa</h3></a>
          </div>
        </div><!-- 推荐图片瀑布流-->
        <section id="main" style="align-content: center;align-items: center">
          <!-- Thumbnails 使用poptrox-->
          <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
            <div class="v-waterfall-content" id="v-waterfall">
              <div v-for="img in waterfallList"
                   class="v-waterfall-item"
                   :style="{top:img.top+'px',left:img.left+'px',width:waterfallImgWidth+'px',height:img.height+20+'px'}">
                <div class="icons"><!-- 三个icon按钮 -->
                  <ul @mouseover="enterul($event)" @mouseout="leaveul($event)" :style="{right: 25+'%'}">
                    <li><p class="icon style2 fa-star" @click="clickCollect($event)"
                           v-bind:class="{ Collected:isCollect }"><span class="label">Collect</span></p></li>
                    <li><p class="icon style2 fa-thumbs-up" @click="clickLike($event)"
                           v-bind:class="{ Likeded:isLike }"><span class="label">Like</span></p></li>
                    <li><a href="" class="icon style2 fa-info" data-poptrox="iframe,1200x800"><span
                      class="label">ForMore</span></a></li>
                  </ul>
                </div>
                <div class="labels"><!-- labels链接 -->
                  <ul @mouseover="enterul_la($event)" @mouseout="leaveul_la($event)" class="KSVul"
                      :style="{top:img.height*0.8-10+'px'}">
                    <a class="" href="#">#AAA</a>
                    <a class="" href="#">#AAA</a>
                    <a class="" href="#">#AAA</a>
                  </ul>
                </div>
                <a>
                  <img @mouseenter="enterpic($event)" @mouseleave="leavepic($event)" :src="img.src" alt="">
                </a>
              </div>
            </div>
          </section>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "PicDetail",
        data() {
            return {
                isCollect: false,
                isLike: false,
                test_path: require('../assets/test/1.jpg'),
                waterfallList: [],
                imgArr: [
                    require('../assets/test/1.jpg'),
                    require('../assets/test/2.jpg'),
                    require('../assets/test/3.jpg'),
                    require('../assets/test/4.jpg'),
                    require('../assets/test/5.jpg'),
                    require('../assets/test/6.jpg'),
                    require('../assets/test/7.jpg'),
                    require('../assets/test/8.jpg')
                ],
                waterfallImgWidth: 350,
                waterfallImgCol: 3,
                waterfallImgRight: 10,
                waterfallImgBottom: 10,
                waterfallDeviationHeight: [],
                imgList: [],
            }
        },
        created() {
            for (let i = 0; i < 8; i++) {
                this.imgList.push(this.imgArr[i]);
            }
        },
        mounted() {
            this.calculationWidth();
        },
        methods:{
            enterpic(e){
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOver";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOver";
                }
            },
            leavepic(e){
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOut";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOut";
                }
            },
            enterul(e){
                e.currentTarget.className = "IconOver";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOver";
                }
            },
            leaveul(e){
                e.currentTarget.className = "IconOut";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOut";
                }
            },
            enterul_la(e){
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOver";
            },
            leaveul_la(e){
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for(var i=0;i<label_number;i++){
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOut";
            },
            clickCollect(e){
                if(e.currentTarget.className === "icon style2 fa-star"){
                    e.currentTarget.className = "icon style2 fa-star Collected";
                }
                else{
                    e.currentTarget.className = "icon style2 fa-star";
                }
            },
            clickLike(e){
                 if(e.currentTarget.className === "icon style2 fa-thumbs-up"){
                    e.currentTarget.className = "icon style2 fa-thumbs-up Liked";
                }
                else{
                    e.currentTarget.className = "icon style2 fa-thumbs-up";
                }
            },
            //计算每个图片的宽度或者是列数
            calculationWidth(){
                let domWidth = document.getElementById("v-waterfall").offsetWidth;
                if (!this.waterfallImgWidth && this.waterfallImgCol){
                    this.waterfallImgWidth = (domWidth-this.waterfallImgRight*this.waterfallImgCol)/this.waterfallImgCol;
                }else if(this.waterfallImgWidth && !this.waterfallImgCol){
                    this.waterfallImgCol = Math.floor(domWidth/(this.waterfallImgWidth+this.waterfallImgRight))
                }
                //初始化偏移高度数组
                this.waterfallDeviationHeight = new Array(this.waterfallImgCol);
                for (let i = 0;i < this.waterfallDeviationHeight.length;i++){
                this.waterfallDeviationHeight[i] = 0;
                }
                this.imgPreloading()
            },
            //图片预加载
            imgPreloading(){
                for (let i = 0;i < this.imgList.length;i++){
                    let aImg = new Image();
                    aImg.src = this.imgList[i];
                    aImg.onload = aImg.onerror = (e)=>{
                        let imgData = {};
                        imgData.height = this.waterfallImgWidth/aImg.width*aImg.height;
                        imgData.src = this.imgList[i];
                        this.waterfallList.push(imgData);
                        this.rankImg(imgData);
                    }
                }
            },
            //瀑布流布局
            rankImg(imgData){
                let {waterfallImgWidth,waterfallImgRight,waterfallImgBottom,waterfallDeviationHeight,waterfallImgCol} = this;
                //for (let i = 0;i < this.waterfallList.length;i++){
                let minIndex = this.filterMin();
                imgData.top = waterfallDeviationHeight[minIndex];
                imgData.left = minIndex*(waterfallImgRight+waterfallImgWidth);
                waterfallDeviationHeight[minIndex] += imgData.height + waterfallImgBottom;
                //}
                console.log(imgData);
            },
            /**
             * 找到最短的列并返回下标
             * @returns {number} 下标
             */
            filterMin(){
                const min = Math.min.apply(null, this.waterfallDeviationHeight);
                return this.waterfallDeviationHeight.indexOf(min);
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
    margin: 0 0 16px;
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
    cursor: pointer;
    display: block;
    font-size: 14px;
    font-weight: 700;
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
    margin-bottom: 26px;
  }

  .taglist {
    text-align: left;
    margin-left: 200px;
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
  }

  .User_name a {
    text-decoration: none;
  }


  .Liked {
    color: rgb(238, 106, 132);
  }

  .Collected {
    color: rgb(238, 203, 106);
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
  .icons .icon{
    float: right;
    margin-right: 0;
  }

</style>
