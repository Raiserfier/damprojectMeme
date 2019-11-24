<template>
  <section id="main" style="align-content: center;align-items: center">
    <header>
    </header>
    <!--TOP10 GRID -->
    <div>
      <div>
        <h2 class="Titleeeee" style="padding:0px 0px 2% 12.5%">
          {{'流行表情包Top'+pop_num}}</h2>
      </div>
      <div align="center">
        <div class="gallery">
          <figure v-for="(img, index) in popList" class="gallery__item" :class="classList[index]" style="overflow: hidden">
            <img :id="img.id" :src="img.img" class="gallery__img Scale" alt=""
                                                       style="z-index:-2">
            <router-link :to="'/details/'+img.id">
              <div class="BKW label_Toppp" @mouseenter="imgScale($event)" @mouseleave="imgScale_la($event)"><!-- labels链接 -->
                <div class="label_Top">
                  <router-link :to="'/category/'+img.classification">{{'#'+img.classification}}</router-link>
                  <router-link v-for="tag in JSON.parse(img.tags)" :to="'/search/'+tag">{{'#'+tag}}</router-link>
                </div>
              </div>
            </router-link>
          </figure>
        </div>
      </div>
    </div>
    <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
      <div class="v-waterfall-content" id="v-waterfall1" style="padding-top: 50px;">
        <div>
          <section v-for="count in cate_num">
            <div class="Cat">
            <div v-if="count === 1">
                <h2 class="Titleeeee" @click="tocate(classname[count-1])" :style="{'padding-top':0+'px'}">
                  {{classname[count-1][0]}}</h2>
              </div>
              <div v-else>
                <h2 class="Titleeeee" @click="tocate(classname[count-1])" :style="{'padding-top':340+'px'}">
                  {{classname[count-1][0]}}</h2>
              </div>
            <div class="Line">
              <div v-for="(img, index) in imgList[count-1]"
                 class="v-waterfall-item"
                 :style="{top:140+ (count-1)*400+ 'px',left:30+(index)*300+'px',width:250+'px',height:250+'px','padding-right':10+'px'}">
              <div class="icons"> <!-- 三个icon按钮 -->
                <ul @mouseout="leaveul($event)" @mouseover="enterul($event)"
                    :style="{top:imgheight-395+'px',right:3+'%'}">
                  <li><p @click="fav_click($event)" class="icon style2 fa-star" v-bind:class="{ Collected:img.state }"><span class="label">Collect</span></p>
                  </li>
                  <li><p @click="thumb_click($event)" class="icon style2 fa-thumbs-up" v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p>
                  </li>
                  <li><router-link :to="'/details/'+img.id" class="icon style2 fa-info" data-poptrox="iframe,1200x800"><span class="label">ForMore</span></router-link></li>
                </ul>
              </div>
              <div class="labels"><!-- labels链接 -->
                <ul :style="{top:imgheight-185+'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)"
                    class="KSVul">
                    <router-link :to="'/category/'+img.classification">{{'#'+img.classification}}</router-link>
                    <router-link v-for="tag in JSON.parse(img.tags)" :to="'/search/'+tag">{{'#'+tag}}</router-link>
                </ul>
              </div>
              <div class="Img-Iput">
                <div class="img_inputBox">
                  <img :id="img.id" :src="img.img" alt="" class="img-inputer" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)">
                </div>
              </div>
            </div>
            </div>
          </div>
          </section>
<!--          &lt;!&ndash;点赞数最高的十张图&ndash;&gt;-->
<!--            <div class="Cat">-->
<!--            <div>-->
<!--              <h2 class="Titleeeee" :style="{'padding-top':340+'px'}">{{'流行表情包Top'+pop_num}}</h2>-->
<!--            </div>-->
<!--            <div class="Line">-->
<!--              <div v-for="(img, index) in popList"-->
<!--                 class="v-waterfall-item"-->
<!--                 :style="{top:140+(cate_num)*400+index/4+ 'px',left:30+(index%4)*300+'px',width:250+'px',height:250+'px','padding-right':10+'px'}">-->
<!--              <div class="icons"> &lt;!&ndash; 三个icon按钮 &ndash;&gt;-->
<!--                <ul @mouseout="leaveul($event)" @mouseover="enterul($event)"-->
<!--                    :style="{top:imgheight-395+'px',right:3+'%'}">-->
<!--                  <li><p @click="fav_click($event)" class="icon style2 fa-star" v-bind:class="{ Collected:img.state }"><span class="label">Collect</span></p>-->
<!--                  </li>-->
<!--                  <li><p @click="thumb_click($event)" class="icon style2 fa-thumbs-up" v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p>-->
<!--                  </li>-->
<!--                  <li><router-link :to="'/details/'+img.id" class="icon style2 fa-info"><span class="label">ForMore</span></router-link>-->
<!--                  </li>-->
<!--                </ul>-->
<!--              </div>-->
<!--              <div class="labels">&lt;!&ndash; labels链接 &ndash;&gt;-->
<!--                <ul :style="{top:imgheight-185+'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)"-->
<!--                    class="KSVul">-->
<!--                  <router-link :to="'/category/'+img.classification">{{'#'+img.classification}}</router-link>-->
<!--                  <router-link v-for="tag in JSON.parse(img.tags)" :to="'/search/'+tag">{{'#'+tag}}</router-link>-->
<!--                </ul>-->
<!--              </div>-->
<!--              <div class="Img-Iput">-->
<!--                <div class="img_inputBox">-->
<!--                  <img :id="img.id" :src="img.img" alt="" class="img-inputer" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)">-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            </div>-->
<!--          </div>-->
        </div>
      </div>

    </section>
  </section>
</template>

<script>
    export default {
        name: "Home",
        data() {
            return {
                imgList: [],
                cate_num: 5,
                each_num: 4,
                my_id: '',
                imgheight: 400,
                classname: [],
                pop_num: 10,
                popList: [],
                classList: {
                    0: 'gallery__item--1',
                    1: 'gallery__item--2',
                    2: 'gallery__item--3',
                    3: 'gallery__item--4',
                    4: 'gallery__item--5',
                    5: 'gallery__item--6',
                    6: 'gallery__item--7',
                    7: 'gallery__item--8',
                    8: 'gallery__item--9',
                    9: 'gallery__item--10',
                },
            }
        },
        created() {
            this.my_id = this.$store.state.user_id;
        },
        mounted() {
            this.getcate();
            this.getpop();
        },

        methods: {
            imgScale(e){
                e.currentTarget.parentElement.previousElementSibling.className="gallery__img Scale_enter";
            },
            imgScale_la(e){
                e.currentTarget.parentElement.previousElementSibling.className="gallery__img Scale";
            },
            tocate(k){
              this.$router.replace({path:'/category/' + k});
            },
            enterpic(e) {
                //icon
                e.currentTarget.parentElement.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOver";
                var label_number = e.currentTarget.parentElement.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.className="img_inputBox imgBox"
            },
            leavepic(e) {
                //icon
                e.currentTarget.parentElement.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOut";
                var label_number = e.currentTarget.parentElement.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.className="img_inputBox"
            },
            enterul(e) {
                e.currentTarget.className = "IconOver";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.nextElementSibling.nextElementSibling.firstElementChild.className="img_inputBox imgBox"
            },
            leaveul(e) {
                e.currentTarget.className = "IconOut";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.nextElementSibling.nextElementSibling.firstElementChild.className="img_inputBox"
            },
            enterul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOver";
                e.currentTarget.parentElement.nextElementSibling.firstElementChild.className="img_inputBox imgBox"
            },
            leaveul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOut";
                e.currentTarget.parentElement.nextElementSibling.nextElementSibling.firstElementChild.className="img_inputBox"
            },
            getcate() {
                this.$api.post('/get_images', {number: this.each_num, email: this.my_id}).then(response => {
                    if(response.data !== 'Not received'){
                        // console.log(response.data)
                        this.cate_num = response.data.length;
                        for (let i = 0; i < this.cate_num; i++) {
                            this.classname.push(Object.keys(response.data[i]));
                            let list = response.data[i][this.classname[i]];
                            // this.imgList.left = i * 300;
                            // list.left = i * 300;
                            this.imgList.push(list)
                            // console.log(list);
                            // for (let j = 0; j < 4; j++) {
                            //     list[j].left = 300 * i;
                            //     console.log(list[j]);
                            // }
                        // console.log('classname : '+(this.classname[i][0]))
                        // console.log('imgs' +this.imgList[i])
                        }
                    }
                        // // for (let key in keys) {
                        //     console.log(keys)
                        //     this.imgList.images = response.data[0][keys]
                        // }
                      // console.log(response.data[0], this.imgList);


                      // this.imgList = response.data;
                      // console.log('imglist'+this.imgList)
                      // console.log('num'+this.cate_num)

                }), (response) => {
                    console.log("error");
                    this.$message.error('获取图片失败');
                }
            },
            getpop(){
                this.$api.post('/most_popular', {number: this.pop_num, email: this.my_id}).then(response => {
                    if(response.data !== 'Not received'){
                        console.log(response.data)
                        this.popList = response.data;
                        console.log(this.popList);
                    }
                    else{
                        console.log('emmmm?')
                    }
                }), (response) => {
                    console.log("error");
                    this.$message.error('获取图片失败');
                }
            },
            //点赞
            thumb_click(e) {
                let flag = true;
                if (e.currentTarget.className === "icon style2 fa-thumbs-up") {
                    e.currentTarget.className = "icon style2 fa-thumbs-up Liked";
                } else {
                    e.currentTarget.className = "icon style2 fa-thumbs-up";
                    flag = false;
                }
                console.log(e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.firstElementChild.getAttribute('id'));
                console.log(this.my_id);
                this.$api.post('/thumb_image ', {
                    id: e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.firstElementChild.getAttribute('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    //console.log(response.data);
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
                if (e.currentTarget.className === "icon style2 fa-star") {
                    e.currentTarget.className = "icon style2 fa-star Collected";
                } else {
                    e.currentTarget.className = "icon style2 fa-star";
                    flag = false;
                }
                console.log("hh")
                console.log(e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.firstElementChild.getAttribute('id'))
                this.$api.post('/like_image', {
                    id: e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.firstElementChild.getAttribute('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    console.log("home1")
                    console.log(response.data);
                    if (response.data === 'SUCCESS') {
                        //改变按钮状态
                        this.$message.success('收藏成功！');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('收藏失败！');
                }
            },
        }
    }


</script>

<style scoped>
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
  .v-waterfall-content {
    padding-top: 20px;
  }
  .Titleeeee {
    cursor: pointer;
    text-decoration: none;
    /*font-family: Serif, serif;*/
    font-family: "Source Sans Pro", sans-serif;
    font-size: 35px;
    font-weight: 300;
    margin: 0;
    z-index: 100;
  }

  .Img-Iput {
    top: 0;
    border: none;
    /*margin-top: 60px;*/
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 250px;
    height: 250px;
    border-radius: 5px;
    /*background-color: rgba(26, 25, 29, 0.84);*/
  }

  .img_inputBox {
    border: none;
    position: relative;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 250px;
    height: 250px;
    border-radius: 5px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .img_inputBox:hover{
    transition: all 0.2s ease-in-out;
    /*background-color: rgba(255, 255, 255, 0.25);*/
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.25), 0 0 0.5em 0 #FF6382;
  }
  .imgBox{
    border: none;
    transition: all 0.2s ease-in-out;
    background-image:linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6));
  }
  .imgBox img{
    mix-blend-mode:multiply;
  }

  .img-inputer {
    position: relative;
    top: 0;
    z-index: 0;
    width: 250px;
    height: 250px;
    /*object-fit: cover;*/
  }

  .thumbnails .v-waterfall-content {
    width: 100%;
    height: 100%;
    position: absolute;
  }

  .thumbnails .v-waterfall-content .v-waterfall-item {
    float: left;
    position: absolute;
  }


  .gallery {
    display: grid;
    grid-template-columns: repeat(8, 130px);
    grid-template-rows: repeat(9, 100px);
    grid-gap: 15px;
    width: 1040px;
    margin-left: -7%;
  }

  .gallery__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .gallery__item--1 {
    grid-column-start: 1;
    grid-column-end: 5;
    grid-row-start: 1;
    grid-row-end: 4;
  }

  .gallery__item--2 {
    grid-column-start: 5;
    grid-column-end: 9;
    grid-row-start: 4;
    grid-row-end: 7;
  }

  .gallery__item--3 {
    grid-column-start: 5;
    grid-column-end: 7;
    grid-row-start: 1;
    grid-row-end: 4;
  }

  .gallery__item--4 {
    grid-column-start: 7;
    grid-column-end: 9;
    grid-row-start: 1;
    grid-row-end: 4;
  }

  .gallery__item--5 {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 4;
    grid-row-end: 7;
  }

  .gallery__item--6 {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 4;
    grid-row-end: 7;
  }

  .gallery__item--7 {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 7;
    grid-row-end: 10;
  }

  .gallery__item--8 {
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row-start: 7;
    grid-row-end: 10;
  }

  .gallery__item--9 {
    grid-column-start: 5;
    grid-column-end: 7;
    grid-row-start: 7;
    grid-row-end: 10;
  }

  .gallery__item--10 {
    grid-column-start: 7;
    grid-column-end: 9;
    grid-row-start: 7;
    grid-row-end: 10;
  }

  figure {
    display: block;
    margin-block-start: 0;
    margin-block-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
  }

  figure img {
    border-radius: 4px;
  }

  .label_Toppp {
    position: relative;
    width: 100%;
    z-index: 10;
    margin-top: -40px;
  }

  .BKW::before {
    height: 330px;
    border-radius: 4px;
    margin-left: 0;
    width: 100%;
    content: "";
    z-index: -1;
    top: -296px;
    left: 0;
    bottom: -10px;
    right: 0px;
    position: absolute;
    opacity: 1;
    background: linear-gradient(rgba(0, 0, 0, 0), rgba(18, 18, 18, 0.6));
    transition: opacity 150ms linear 0s;
  }

  .BKW:hover:after {
    opacity: 1;
  }

  .BKW::after {
    height: 330px;
    border-radius: 4px;
    margin-left: 0;
    width: 100%;
    content: "";
    z-index: -1;
    top: -296px;
    left: 0;
    right: 0px;
    position: absolute;
    opacity: 0;
    transition: opacity 150ms linear 0s;
    background: linear-gradient(rgba(0, 0, 0, 0), rgba(255, 102, 102, 0.2), rgba(255, 102, 102, 0.9) 100%);
  }

  .label_Top {
    margin-left: 10%;
    font-weight: 600;
    text-align: left;
    font-family: nexablack, sans-serif;
    -webkit-font-smoothing: antialiased;
    font-size: 20px;
    color: rgb(255, 255, 255);
    line-height: 1.2;
    user-select: none;
  }
  .Scale{
    width: 100%;
    height: 100%;
    transform: scale(1);
    transition: transform 150ms linear 0s;
  }
  .Scale_enter{
    width: 100%;
    height: 100%;
    transform: scale(1.15);
    transition: transform 150ms linear 0s;
  }

</style>
