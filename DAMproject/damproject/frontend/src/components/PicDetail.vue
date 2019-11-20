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
                 :style="{'background-image':'url'+'(\'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3900046848,1834418761&fm=26&gp=0.jpg\')'}"></a>
              <h2 class="User_name"><a href="">TESTER</a></h2>
            </div>
            <div>
              <p class="user_introduction">
                这是用户简介
              </p>
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
        </div>

        <!-- 推荐图片瀑布流-->
        <details-recommend></details-recommend>

<!--        <section id="main" style="align-content: center;align-items: center">-->
<!--          <div>-->
<!--            <h2 class="Title">相似表情包</h2>-->
<!--          </div>-->
<!--          &lt;!&ndash; Thumbnails 使用poptrox&ndash;&gt;-->
<!--          <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">-->
<!--            <div class="v-waterfall-content" id="v-waterfall">-->
<!--              <div v-for="img in waterfallList"-->
<!--                   class="v-waterfall-item"-->
<!--                   :style="{top:img.top+'px',left:img.left+'px',width:waterfallImgWidth+'px',height:img.height+20+'px'}">-->
<!--                <div class="icons">&lt;!&ndash; 三个icon按钮 &ndash;&gt;-->
<!--                  <ul @mouseover="enterul($event)" @mouseout="leaveul($event)" :style="{right: 25+'%'}">-->
<!--                    <li><p class="icon style2 fa-star" @click="clickCollect($event)"-->
<!--                           v-bind:class="{ Collected:isCollect }"><span class="label">Collect</span></p></li>-->
<!--                    <li><p class="icon style2 fa-thumbs-up" @click="clickLike($event)"-->
<!--                           v-bind:class="{ Likeded:isLike }"><span class="label">Like</span></p></li>-->
<!--                    <li><a href="" class="icon style2 fa-info" data-poptrox="iframe,1200x800"><span-->
<!--                      class="label">ForMore</span></a></li>-->
<!--                  </ul>-->
<!--                </div>-->
<!--                <div class="labels">&lt;!&ndash; labels链接 &ndash;&gt;-->
<!--                  <ul @mouseover="enterul_la($event)" @mouseout="leaveul_la($event)" class="KSVul"-->
<!--                      :style="{top:img.height*0.8-10+'px'}">-->
<!--                    <a class="" href="#">#AAA</a>-->
<!--                    <a class="" href="#">#AAA</a>-->
<!--                    <a class="" href="#">#AAA</a>-->
<!--                  </ul>-->
<!--                </div>-->
<!--                <a>-->
<!--                  <img @mouseenter="enterpic($event)" @mouseleave="leavepic($event)" :src="img.src" alt="">-->
<!--                </a>-->
<!--              </div>-->
<!--            </div>-->
<!--          </section>-->
<!--        </section>-->
      </div>
    </div>
  </div>
</template>

<script>
    import ImageStream from './ImagePage/ImageStream'
    export default {
        name: "PicDetail",
        components:{
            'details-recommend': ImageStream
        },
        data() {
            return {
                // isCollect: false,
                // isLike: false,
                test_path: require('../assets/test/1.jpg'),
                // waterfallList: [],
                // imgArr: [
                //     require('../assets/test/1.jpg'),
                //     require('../assets/test/2.jpg'),
                //     require('../assets/test/3.jpg'),
                //     require('../assets/test/4.jpg'),
                //     require('../assets/test/5.jpg'),
                //     require('../assets/test/6.jpg'),
                //     require('../assets/test/7.jpg'),
                //     require('../assets/test/8.jpg')
                // ],
                // waterfallImgWidth: 350,
                // waterfallImgCol: 3,
                // waterfallImgRight: 10,
                // waterfallImgBottom: 10,
                // waterfallDeviationHeight: [],
                // imgList: [],
            }
        },
        created() {

        },
        mounted() {

        },
        methods:{

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

  .Title {
    font-size: 16px;
    font-weight: 600;
    line-height: 1.1;
    width: 100%;
    margin-left: 200px;
    margin-bottom: 15px;
  }
  .user_introduction{
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

</style>
