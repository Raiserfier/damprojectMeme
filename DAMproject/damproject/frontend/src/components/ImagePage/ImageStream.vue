<template>
  <div class="ImageStream">
    <div class="buttonGroup_upd">
      <div v-if="this.$route.params.rank === 'hot'">
        <button type="button" class="Button_mask_upd choosen_upd" style="border-radius: 5px 0 0 5px"
                @click="By_heat($event)">按热度
        </button>
        <button type="button" class="Button_mask_upd unchoosen_upd"
                style="border-radius: 0 5px 5px 0;margin-left: -6px;" @click="By_time($event)">按时间
        </button>
        <button v-if="this.$store.state.manager && this.$route.params.type==='channel'" type="button"
                class="Button_mask_del" style="border-radius: 5px;margin-left: 20px;" @click="delete_all($event)">一键清除
        </button>
      </div>
      <div v-if="this.$route.params.rank === 'new'">
        <button type="button" class="Button_mask_upd unchoosen_upd" style="border-radius: 5px 0 0 5px"
                @click="By_heat($event)">按热度
        </button>
        <button type="button" class="Button_mask_upd choosen_upd" style="border-radius: 0 5px 5px 0;margin-left: -6px;"
                @click="By_time($event)">按时间
        </button>
        <button v-if="this.$store.state.manager && this.$route.params.type==='channel'" type="button"
                class="Button_mask_del" style="border-radius: 5px;margin-left: 20px;" @click="delete_all($event)">一键清除
        </button>
      </div>
    </div>
    <section id="main" style="align-content: center;align-items: center">
      <!-- Thumbnails 使用poptrox-->
      <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
        <div class="v-waterfall-content" id="v-waterfall" :style="{left:6+'%'}">
          <div v-for="img in waterfallList" v-bind:key="img.id"
               class="v-waterfall-item"
               :style="{top:img.top+'px',left:img.left+'px',width:waterfallImgWidth+'px',height:img.height+20+'px'}">
            <div class="icons" v-if="$store.state.user_id !== '99'"><!-- 三个icon按钮 -->
              <ul @mouseover="enterul($event)" @mouseout="leaveul($event)">
                <li
                  v-if="$route.params.type==='channel' && !$store.state.manager && $store.state.user_id===$route.params.id">
                  <p class="icon style3 fa-trash" @click="user_delete($event)">
                    <span class="label">Delete</span></p></li>
                <li v-if="$route.params.type==='channel' && $store.state.manager">
                  <p class="icon style3 fa-trash-o" @click="manager_delete($event)">
                    <span class="label">Delete</span></p></li>
                <li><p class="icon style2 fa-star" @click="fav_click($event)" v-bind:class="{ Collected:img.state }">
                  <span class="label">Collect</span></p></li>
                <li><p class="icon style2 fa-thumbs-up" @click="thumb_click($event)"
                       v-bind:class="{ Likeded:img.state }"><span class="label">Like</span></p></li>
                <li>
                  <router-link :to="'/details/'+img.id+'/hot'" class="icon style2 fa-info"><span
                    class="label">ForMore</span>
                  </router-link>
                </li>
              </ul>
            </div>
            <div class="labels">
              <ul @mouseover="enterul_la($event)" @mouseout="leaveul_la($event)" class="KSVul"
                  :style="{top:img.height-40+'px', left:10+'px'}"><!-- labels链接 -->
                <router-link :to="'/category/'+img.classification+'/hot'">{{'#'+img.classification}}</router-link>
                <router-link v-for="tag in JSON.parse(img.tags)" :to="'/search/'+tag+'/hot'">{{'#'+tag+' '}}</router-link>
<!--                <div>{{img.thumbs + '@' + img.likes}}</div>-->
<!--                <div>{{img.upload_time}}</div>-->
              </ul>
            </div>
            <div class="imgHover" :style="{height:img.height+'px'}">
              <img @mouseenter="enterpic($event)" @mouseleave="leavepic($event)" :id="img.id" :src="img.img" alt=""
                   style="border-radius: 4px">
            </div>
          </div>
        </div>
      </section>

    </section>
  </div>
</template>

<script>
    export default {
        name: "ImageStream",
        data() {
            return {
                key: 'all',//检索关键词
                my_id: '',
                type: 0,//0是全局搜索，1是收藏，2是上传，3是类别
                isCollect: false,
                isLike: false,

                imgList: [],//从后端获取到的图片包括图片的img\id\tags\state\classification
                count: 0,//已经从后端获取的图片数量
                last: 0,//List中未被加载的图片数量
                each_time: 10,//每次加载的图片数量
                imgArr: [],//当次要加载的图片
                waterfallList: [],//已经加载的照片

                waterfallImgWidth: 350,
                waterfallImgCol: 3,
                waterfallImgRight: 10,
                waterfallImgBottom: 10,
                waterfallDeviationHeight: [],
                threshold: 20,
            }
        },
        created() {
            // console.log(this.$route.params.type);
            // console.log(this.$route.params.key);
            // console.log(this.$route.params.id);
            this.my_id = this.$store.state.user_id;
            this.key = this.$route.params.key;
            //图片详情页推荐
            if (this.$route.params.pic !== undefined) {
                this.get_details_recommend(this.$route.params.pic, this.$store.state.user_id);
            }//用户页
            else if (this.$route.params.id !== undefined) {
                if (this.$route.params.type === 'channel') this.type = 2;
                else if (this.$route.params.type === 'favorite') this.type = 1;
                this.get_user(this.$route.params.id, this.type, this.key);
            }
            //搜索、类别页\\用户推荐页
            else {
                if (this.$route.params.type === undefined) {
                    this.get_recommend(this.$store.state.user_id);
                } else {
                    if (this.$route.params.type === 'search') this.type = 0;
                    else if (this.$route.params.type === 'category') this.type = 3;
                    this.get_img(this.type, this.key);
                }
            }
        },
        mounted() {
            window.addEventListener('scroll', this.scrollEvent, false);
        },
        destroyed() {
            window.removeEventListener('scroll', this.scrollEvent, false);
        },
        methods: {
            delete_all() {
                this.$api.post('/delete_report', {}).then(response => {
                    if (response.data === 'SUCCESS') {
                        this.$message.success('清除成功！');
                        this.$router.replace({path: '/'});
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('清除失败！');
                }
            },
            user_delete(e) {
                this.$api.post('/delete_image', {
                    id: e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttribute('id'),
                }).then(response => {
                    if (response.data === 'SUCCESS') {
                        this.$message.success('删除成功！');
                        this.$router.replace({path: '/'});
                        this.$router.replace({path: '/channel/' + this.$store.state.user_id + '/all' + '/hot'});
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('删除失败！');
                }
            },
            manager_delete(e) {
                this.$api.post('/delete_image', {
                    id: e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttribute('id'),
                }).then(response => {
                    if (response.data === 'SUCCESS') {
                        this.$message.success('删除成功！');
                        this.$router.replace({path: '/'});
                        this.$router.replace({path: '/channel/' + this.$store.state.user_id + '/all' + '/hot'});
                    }
                }), (response) => {
                    this.$message.error('删除失败！');
                }
            },
            By_heat(e) {
                this.$router.push('hot');
                if (e.currentTarget.className === "Button_mask_upd unchoosen_upd") {
                    e.currentTarget.className = "Button_mask_upd choosen_upd";
                    e.currentTarget.nextElementSibling.className = "Button_mask_upd unchoosen_upd";
                }
            },
            By_time(e) {
                this.$router.push('new');
                if (e.currentTarget.className === "Button_mask_upd unchoosen_upd") {
                    e.currentTarget.className = "Button_mask_upd choosen_upd";
                    e.currentTarget.previousElementSibling.className = "Button_mask_upd unchoosen_upd";
                }
            },
            // scrollEvent(){
            //     let pageHeight = $('body').height(),
            //         scrollTop = $(window).scrollTop(),
            //         winHeight = $(window).height(),
            //         thresold = pageHeight - scrollTop - winHeight;
            //     if (thresold > -100 && thresold <= 20) {
            //     }
            //     if (document.body.scrollTop+ document.body.clientHeight>= document.body.scrollHeight-this.threshold) {
            //         console.log('end');
            //         this.threshold = -100;
            //         this.load_more();
            //     }
            // },
            scrollEvent() {
                let pageHeight = $(document).height(),
                    scrollTop = $(window).scrollTop(),
                    winHeight = $(window).height(),
                    thresold = pageHeight - scrollTop - winHeight;
                // console.log(pageHeight,scrollTop,winHeight);
                if (thresold <= 10) {
                    console.log('end');
                    if (this.last) {
                        this.load_more();
                    }
                }
                // console.log('132\n\n'+document.body.scrollHeight,document.body.scrollTop,document.body.clientHeight);
            },
            //一次加载10张图片
            load_more() {
                // console.log('moremoremore')
                this.imgArr = []
                for (let i = 0; i < this.each_time; i++) {
                    if (this.last === 0) {
                        break;
                    }
                    this.last--;
                    this.imgArr.push(this.imgList[this.last]);
                }
                this.preloading();
                this.threshold = 20;
            },
            enterpic(e) {
                //icon
                e.currentTarget.parentElement.className = "imgHover imgBox";
                if (this.$store.state.user_id !== '99')
                    e.currentTarget.parentElement.previousElementSibling.previousElementSibling.firstElementChild.className = "IconOver";
                var label_number = e.currentTarget.parentElement.previousElementSibling.firstElementChild.childElementCount;
                var children = e.currentTarget.parentElement.previousElementSibling.firstElementChild.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOver";
                }
            },
            leavepic(e) {
                //icon
                e.currentTarget.parentElement.className = "imgHover";
                if (this.$store.state.user_id !== '99')
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
                e.currentTarget.parentElement.nextElementSibling.nextElementSibling.className = "imgHover imgBox";
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
                if (this.$store.state.user_id !== '99')
                    e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOver";
                e.currentTarget.parentElement.nextElementSibling.className = "imgBox";
            },
            leaveul_la(e) {
                var label_number = e.currentTarget.childElementCount;
                var children = e.currentTarget.children;
                for (var i = 0; i < label_number; i++) {
                    children[i].className = "LabelsOut";
                }
                if (this.$store.state.user_id !== '99')
                    e.currentTarget.parentElement.previousElementSibling.firstElementChild.className = "IconOut";
            },

            //搜索结果
            get_img(t, k) {
                this.$api.post('/get_user_image', {
                    key: k,
                    email: this.my_id,
                    email_user: this.my_id,
                    type: t
                }).then(response => {
                    if (response.data !== 'Not received') {
                        // console.log(response.data);
                        this.imgList = response.data;
                        this.count += response.data.length;
                        this.last += response.data.length;

                        this.init();
                    } else {
                        console.log('error get_img?')
                    }
                }), (response) => {
                    //console.log("error get_img");
                    this.$message.error('图片获取失败');
                }
            },
            //看主页和收藏
            get_user(id, t, k) {
                console.log(k);
                this.$api.post('/get_user_image', {
                    key: k,
                    email: id,
                    type: t,
                    email_user: this.my_id
                }).then(response => {
                    if (response.data !== 'Not received') {
                        // console.log(response.data);
                        this.imgList = response.data;
                        // console.log(this.imgList);
                        this.count += response.data.length;
                        this.last += response.data.length;

                        this.init();
                    } else {
                        console.log('error get_user?')
                    }
                }), (response) => {
                    //console.log("error get_user");
                    this.$message.error('图片获取失败');
                }
            },
            init(){
                //！！！！！排序
                if (this.$route.params.rank === 'new') {
                    sortByTime(this.imgList);
                }else{
                    sortByHeat(this.imgList);
                }
                //加载图片
                for (let i = 0; i < this.each_time; i++) {
                    if (this.last === 0) {
                        break;
                    }
                    this.last--;
                    this.imgArr.push(this.imgList[this.last]);
                }
                this.calculationWidth();
            },
            //用户推荐
            get_recommend(id) {
                console.log("user recommend");
                console.log(id);
                this.$api.post('/get_recommend', {email_user: id}).then(response => {
                    if (response.data !== 'Not received') {
                        // console.log(response.data);
                        this.imgList = response.data;
                        // console.log(this.imgList);
                        this.count += response.data.length;
                        this.last += response.data.length;

                        this.init();
                    } else {
                        this.$message.warnings('图片获取失败');
                    }
                }), (response) => {
                    this.$message.error('图片获取失败');
                }
            },
            //图片详情页推荐
            get_details_recommend(pid, id) {
                this.$api.post('/detail_recommend', {id: pid, number: 5, email: id}).then(response => {
                    console.log(response.data);
                    if (response.data !== 'Not received') {
                        this.imgList = response.data;
                        this.count += response.data.length;
                        this.last += response.data.length;

                        this.init();
                    } else {
                        this.$message.warnings('图片获取失败');
                    }
                }), (response) => {
                    this.$message.error('图片获取失败');
                }
            },
            //计算每个图片的宽度或者是列数
            calculationWidth() {
                let domWidth = document.getElementById("v-waterfall").offsetWidth;
                if (!this.waterfallImgWidth && this.waterfallImgCol) {
                    this.waterfallImgWidth = (domWidth - this.waterfallImgRight * this.waterfallImgCol) / this.waterfallImgCol;
                } else if (this.waterfallImgWidth && !this.waterfallImgCol) {
                    this.waterfallImgCol = Math.floor(domWidth / (this.waterfallImgWidth + this.waterfallImgRight))
                }
                //初始化偏移高度数组
                this.waterfallDeviationHeight = new Array(this.waterfallImgCol);
                for (let i = 0; i < this.waterfallDeviationHeight.length; i++) {
                    this.waterfallDeviationHeight[i] = 0;
                }
                this.preloading();
            },
            //按图片流格式预处理获得图片位置
            preloading() {
                for (let i = 0; i < this.imgArr.length; i++) {
                    let aImg = new Image();
                    aImg.src = this.imgArr[i].img;
                    aImg.onload = aImg.onerror = (e) => {
                        let imgData = {};
                        imgData = this.imgArr[i];
                        imgData.height = this.waterfallImgWidth / aImg.width * aImg.height;
                        this.waterfallList.push(imgData);
                        this.rankImg(imgData);
                    }
                }
            },
            //瀑布流布局
            rankImg(imgData) {
                let {waterfallImgWidth, waterfallImgRight, waterfallImgBottom, waterfallDeviationHeight, waterfallImgCol} = this;
                //for (let i = 0;i < this.waterfallList.length;i++){
                let minIndex = this.filterMin();
                imgData.top = waterfallDeviationHeight[minIndex];
                imgData.left = minIndex * (waterfallImgRight + waterfallImgWidth);
                waterfallDeviationHeight[minIndex] += imgData.height + waterfallImgBottom;
                //}
            },
            /**
             * 找到最短的列并返回下标
             * @returns {number} 下标
             */
            filterMin() {
                const min = Math.min.apply(null, this.waterfallDeviationHeight);
                return this.waterfallDeviationHeight.indexOf(min);
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
                this.$api.post('/thumb_image', {
                    id: e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttribute('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    // console.log('1111111' + response.data);
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
                this.$api.post('/like_image ', {
                    id: e.target.parentElement.parentElement.parentElement.parentElement.lastElementChild.firstElementChild.getAttribute('id'),
                    email: this.my_id, state: flag
                }).then(response => {
                    //console.log(response.data);
                    if (response.data === 'SUCCESS') {
                        //改变按钮状态
                        if (flag)
                            this.$message.success('收藏成功！');
                        else
                            this.$message.success('取消收藏成功！');
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('收藏失败！');
                }
            },
        }
    }

    function sortByHeat(array) {
        return array.sort(function (a, b) {
            let x = parseInt(a['likes']) + parseInt(a['thumbs']);
            let y = parseInt(b['likes']) + parseInt(b['thumbs']);
            // console.log(x);
            // console.log(y);
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
        })
    }

    function sortByTime(array) {
        return array.sort(function (a, b) {
            let x = a['upload_time'];
            let y = b['upload_time'];
            // console.log(x);
            // console.log(y);
            return ((x < y) ? -1 : ((x > y) ? 1 : 0));
        })
    }
</script>

<style scoped>
  #main {
    padding: 1.5em 0 2em 0;
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

  .imgBox {
    transition: all 0.2s ease-in-out;
    background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.6));
  }

  .imgBox img {
    mix-blend-mode: multiply;
  }

  .imgHover {
    border-radius: 4px;
  }

  .imgHover :hover {
    transition: all 0.2s ease-in-out;
    /*background-color: rgba(255, 255, 255, 0.25);*/
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.25), 0 0 0.5em 0 #FF6382;
  }

  .buttonGroup_upd {
    padding: 10px 0 10px 225px;
  }

  .Button_mask_upd {
    border: none;
    height: 33px;
    width: 100px;
    flex: 1 1 0%;
    white-space: nowrap;
    box-sizing: border-box;
    cursor: pointer;
    font-family: inherit;
    font-size: 14px;
    font-weight: bold;
    line-height: 36px;
    min-width: 36px;
    text-align: center;
    user-select: none;
    -webkit-appearance: none;
    -webkit-font-smoothing: antialiased;
    position: relative;
    outline: none;
    padding: 0px 15px;
    transition: all 0.2s;
    /*background: rgb(0, 255, 153);*/
  }

  .Button_mask_upd:hover {
    color: rgb(18, 18, 18);
    background: rgba(90, 255, 178, 0.85);
  }

  .choosen_upd {
    background: #4bee97;
    color: rgb(18, 18, 18);
  }

  .unchoosen_upd {
    background: #2c2c2f;
    color: white;
  }

  .Button_mask_del {
    border: none;
    height: 33px;
    width: 100px;
    flex: 1 1 0%;
    white-space: nowrap;
    box-sizing: border-box;
    cursor: pointer;
    font-family: inherit;
    font-size: 14px;
    font-weight: bold;
    line-height: 36px;
    min-width: 36px;
    text-align: center;
    user-select: none;
    -webkit-appearance: none;
    -webkit-font-smoothing: antialiased;
    position: relative;
    outline: none;
    padding: 0px 15px;
    transition: all 0.2s;
    background: #2c2c2f;
    color: white;
    /*background: rgb(0, 255, 153);*/
  }

  .Button_mask_del:hover {
    color: rgb(18, 18, 18);
    background: rgba(255, 102, 102, 0.85);
  }
</style>
