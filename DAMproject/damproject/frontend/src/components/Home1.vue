<template>
  <section id="main" style="align-content: center;align-items: center">
    <header>
    </header>
    <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
      <div class="v-waterfall-content" id="v-waterfall1" style="padding-top: 50px;">
        <div>
          <section v-for="count in cate_num">
            <div class="Cat">
            <div>
              <h2 class="Titleeeee" @click="tocate(classname[count-1])" :style="{'padding-top':(count-1)*340+'px'}">{{classname[count-1][0]}}</h2>
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
                    <!--<a class="" href="#">{{img.tags}}</a>-->
                    <a class="" v-for="tag in JSON.parse(img.tags)" href="#">{{'#'+tag}}</a>
                </ul>
              </div>
              <div class="Img-Iput">
                <div class="img_inputBox" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)">
                  <img :id="img.id" :src="img.img" alt="" class="img-inputer">
                </div>
              </div>
            </div>
            </div>
          </div>
          </section>
          <!--点赞数最高的十张图-->
            <div class="Cat">
            <div>
              <h2 class="Titleeeee" :style="{'padding-top':340+'px'}">{{'流行表情包Top'+pop_num}}</h2>
            </div>
            <div class="Line">
              <div v-for="(img, index) in popList"
                 class="v-waterfall-item"
                 :style="{top:140+(cate_num)*400+index/4+ 'px',left:30+(index%4)*300+'px',width:250+'px',height:250+'px','padding-right':10+'px'}">
              <div class="icons"> <!-- 三个icon按钮 -->
                <ul @mouseout="leaveul($event)" @mouseover="enterul($event)"
                    :style="{top:imgheight-395+'px',right:3+'%'}">
                  <li><p @click="fav_click($event)" class="icon style2 fa-star" v-bind:class="{ Collected:img.state }"><span class="label">Collect</span></p>
                  </li>
                  <li><p @click="thumb_click($event)" class="icon style2 fa-thumbs-up" v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p>
                  </li>
                  <li><a class="icon style2 fa-info" data-poptrox="iframe,1200x800" href="index.html"><span class="label">ForMore</span></a>
                  </li>
                </ul>
              </div>
              <div class="labels"><!-- labels链接 -->
                <ul :style="{top:imgheight-185+'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)"
                    class="KSVul">
                  <a>{{img.classification}}</a>
                  <!--<a class="" href="#">{{img.tags}}</a>-->
                  <a class="" v-for="tag in img.tags" href="#">{{'#'+tag}}</a>
                </ul>
              </div>
              <div class="Img-Iput">
                <div class="img_inputBox" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)">
                  <img :id="img.id" :src="img.img" alt="" class="img-inputer">
                </div>
              </div>
            </div>
            </div>
          </div>
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
            tocate(k){
              this.$router.replace({path:'/category/' + k});
            },
            enterpic(e) {
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOver";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
            },
            leavepic(e) {
                //icon
                e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOut";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
            },
            enterul(e) {
                e.currentTarget.className = "IconOver";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
            },
            leaveul(e) {
                e.currentTarget.className = "IconOut";
                //label
                var label_number = e.currentTarget.parentElement.nextElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.nextElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
            },
            enterul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOver";
            },
            leaveul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
                e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOut";
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
                this.$api.post('/thumb_image ', {
                    id: e.target.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttributeNode('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    //console.log(response.data);
                    if (response.data === 'SUCCESS') {
                        this.$message.success('成功');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('失败');
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
                        this.$message.success('成功');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('失败');
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
    /*margin-top: 60px;*/
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 250px;
    height: 250px;
    border-radius: 5px;
    background-color: rgba(26, 25, 29, 0.84);
  }

  .img_inputBox {
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

  .img-inputer {
    position: relative;
    top: 0;
    z-index: 0;
    width: auto;
    height: 100%;
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

</style>
