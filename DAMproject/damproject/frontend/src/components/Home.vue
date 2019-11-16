<template>
  <div class="home" style="background-color: aqua">
    <main class="nraeUgP6">
      <div data-test-selector="page-item-detail">
        <section class="_3LZaCHBh">
          <div class="_1F53lIfv">
             <!-- Thumbnails 使用poptrox-->
            <section v-for="count in cate_num">
              <header class="_30jhRtnB" style="height: 44px">
                <h2 class="_2uvC445S">{{classname[count-1]}}</h2>
                <a class="_6Xeq5Ikb _3rHyVhAS" @click="tocate(classname[count-1])">
                  <span class="_1_4B_gHA">更多</span>
                  <svg aria-label="Arrow right" class="_2YAsIJAi _3f8vV4uW" role="img" tabindex="-32768"
                       viewBox="0 0 28.9 7.8" xmlns="http://www.w3.org/2000/svg">
                    <path d="M 25 3.2 H 0.7 c -0.4 0 -0.7 0.3 -0.7 0.7 c 0 0.4 0.3 0.7 0.7 0.7 H 25 c 0.4 0 0.7 -0.3 0.7 -0.7 c 0 -0.4 -0.3 -0.7 -0.7 -0.7 Z"/>
                    <path d="M 24.4 4.7 V 0.4 c 0 -0.4 0.3 -0.6 0.6 -0.3 l 1.2 1.1 c 0.3 0.3 0.9 0.8 1.2 1.1 l 1.2 1.1 c 0.3 0.3 0.3 0.8 0 1.1 l -1.2 1.1 c -0.3 0.3 -0.9 0.8 -1.2 1.1 l -1.2 0.9 c -0.3 0.3 -0.6 0.2 -0.6 -0.3 V 4.7 Z"/>
                  </svg>
                </a>
              </header>
              <ul class="ELHm5RGs">
                <li v-for="img in imgList[count-1]" class="_2-KcWAGg">
                  <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
                    <div class="v-waterfall-content" id="v-waterfall">
                      <div class="v-waterfall-item">
                        <div class="icons"><!-- 三个icon按钮 -->
                                  <ul @mouseout="leaveul($event)" @mouseover="enterul($event)">
                                    <li><p @click="clickCollect($event)" class="icon style2 fa-star"
                                           v-bind:class="{ Collected:img.state }"><span class="label">Collect</span></p></li>
                                    <li><p @click="clickLike($event)" class="icon style2 fa-thumbs-up"
                                           v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p></li>
                                    <li><a class="icon style2 fa-info" data-poptrox="iframe,1200x800" href="index.html"><span
                                      class="label">ForMore</span></a></li>

                                  </ul>
                                </div>
                        <div class="labels"><!-- labels链接 -->
                          <ul :style="{top:500 +'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)" class="KSVul">
                            <a href="#">{{img.tags}}</a>
                          </ul>
                        </div>
                        <a>
                          <img :id="img.id" :src="img.img" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)"
                               alt="" style="width: 100%; height: 100%; position: absolute; inset: 0px;">
                        </a>
                      </div>
                    </div>
                  </section>
                </li>
              </ul>
            </section>

<!--            <section>-->
<!--              <header class="_30jhRtnB" style="height: 44px">-->
<!--                <h2 class="_2uvC445S">123132</h2>-->
<!--                <a class="_6Xeq5Ikb _3rHyVhAS" href="/web-templates/similar-to-E52L89">-->
<!--                  <span class="_1_4B_gHA">更多</span>-->
<!--                  <svg aria-label="Arrow right" class="_2YAsIJAi _3f8vV4uW" role="img" tabindex="-32768"-->
<!--                       viewBox="0 0 28.9 7.8" xmlns="http://www.w3.org/2000/svg">-->
<!--                    <path-->
<!--                      d="M 25 3.2 H 0.7 c -0.4 0 -0.7 0.3 -0.7 0.7 c 0 0.4 0.3 0.7 0.7 0.7 H 25 c 0.4 0 0.7 -0.3 0.7 -0.7 c 0 -0.4 -0.3 -0.7 -0.7 -0.7 Z"/>-->
<!--                    <path-->
<!--                      d="M 24.4 4.7 V 0.4 c 0 -0.4 0.3 -0.6 0.6 -0.3 l 1.2 1.1 c 0.3 0.3 0.9 0.8 1.2 1.1 l 1.2 1.1 c 0.3 0.3 0.3 0.8 0 1.1 l -1.2 1.1 c -0.3 0.3 -0.9 0.8 -1.2 1.1 l -1.2 0.9 c -0.3 0.3 -0.6 0.2 -0.6 -0.3 V 4.7 Z"/>-->
<!--                  </svg>-->
<!--                </a>-->
<!--              </header>-->

<!--              <ul class="ELHm5RGs">-->
<!--                <li class="_2-KcWAGg" v-for="img in imgList">-->

<!--                  <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">-->
<!--                    <div class="v-waterfall-content" id="v-waterfall1">-->
<!--                      <div class="v-waterfall-item" style="width: 300px; height: 300px;">-->
<!--                        <div class="icons"> &lt;!&ndash; 三个icon按钮 &ndash;&gt;-->
<!--                          <ul @mouseout="leaveul($event)" @mouseover="enterul($event)">-->
<!--                            <li><p @click="clickCollect($event)" class="icon style2 fa-star"-->
<!--                                   v-bind:class="{ Collected:false }"><span class="label">Collect</span></p></li>-->
<!--                            <li><p @click="clickLike($event)" class="icon style2 fa-thumbs-up"-->
<!--                                   v-bind:class="{ Likeded:false }"><span class="label">Like</span></p></li>-->
<!--                            <li><a class="icon style2 fa-info" data-poptrox="iframe,1200x800" href="index.html"><span-->
<!--                              class="label">ForMore</span></a></li>-->

<!--                          </ul>-->
<!--                        </div>-->
<!--                        <div class="labels">&lt;!&ndash; labels链接 &ndash;&gt;-->
<!--                          <ul :style="{top:imgheight+ 20 +'px'}" @mouseout="leaveul_la($event)" @mouseover="enterul_la($event)" class="KSVul">-->
<!--                            <a href="#">#AAA</a>-->
<!--                            <a href="#">#AAA</a>-->
<!--                            <a href="#">#AAA</a>-->
<!--                          </ul>-->
<!--                        </div>-->
<!--                        <a>-->
<!--                          <img :src="img" @mouseenter="enterpic($event)" @mouseleave="leavepic($event)"-->
<!--                               alt="" style="width: 100%; height: 100%; position: relative; inset: 0px;">-->
<!--                        </a>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                  </section>-->
<!--                </li>-->
<!--              </ul>-->
<!--            </section>-->

          </div>
        </section>
      </div>
    </main>

  </div>
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
            }
        },
        created() {
            this.my_id = this.$store.state.user_id;
            this.getcate();
        },
        mounted() {
        },

        methods: {
            tocate(k){
              this.$route.replace({path:'/category/' + k});
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
                        this.cate_num = response.data.length;
                        this.classname = Object.keys(response.data[0]);
                        for (let i = 0; i < this.cate_num; i++) {
                            let list = response.data[i][this.classname[i]];
                            this.imgList.push(list)
                        }
                        console.log((this.classname))
                        console.log(this.imgList)
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
                this.preloading();
            },
            preloading() {
                for (let i = 0; i < this.cate_num; i++) {
                    for (let j = 0; j < this.each_num; j++) {

                    }
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
                this.$api.post('/like_image ', {
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
                this.$api.post('/like_image ', {
                    id: e.target.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttributeNode('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    //console.log("home")
                    //console.log(response.data);
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
    transform: translate(0, 25%);
    transition: all 0.3s ease-in-out;
  }

  .LabelsOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(100%);
    -webkit-transform: translateY(100%);
    -ms-transform: translateY(100%);
    transform: translateY(20px);
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out;
  }

  .IconOver {
    visibility: visible;
    opacity: 1;
    -webkit-transform: translate(0, -100%);
    transform: translate(0, 25%);
    transition: all 0.3s ease-in-out;
  }

  .IconOut {
    visibility: hidden;
    opacity: 0;
    -moz-transform: translateY(-100%);
    -webkit-transform: translateY(-100%);
    -ms-transform: translateY(-100%);
    transform: translateY(-10%);
    -webkit-transition: all 1s ease-in-out;
    transition: all 0.3s ease-in-out
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

  .v-waterfall-item img {
    width: 100%;
    height: auto;
  }
</style>
