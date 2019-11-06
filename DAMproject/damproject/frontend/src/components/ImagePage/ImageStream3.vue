<template>
    <section id="main" style="align-content: center;align-items: center">
					<!-- Thumbnails 使用poptrox-->
    <section class="thumbnails" style="margin-left: 10%; margin-right: 10%">
    <div class="v-waterfall-content" id="v-waterfall">
      <div v-for="img in waterfallList"
           class="v-waterfall-item"
           :style="{top:img.top+'px',left:img.left+'px',width:waterfallImgWidth+'px',height:img.height}">
          <div class="icons"><!-- 三个icon按钮 -->
              <ul @mouseover="enterul($event)" @mouseout="leaveul($event)">
                <li><p class="icon style2 fa-star" @click="clickCollect($event)" v-bind:class="{ Collected:isCollect }" ><span class="label">Collect</span></p></li>
                <li><p class="icon style2 fa-thumbs-up" @click="clickLike($event)" v-bind:class="{ Likeded:isLike }"><span class="label">Like</span></p></li>
                <li><a href="index.html" class="icon style2 fa-info" data-poptrox="iframe,1200x800"><span class="label">ForMore</span></a></li>
              </ul>
          </div>
        <div class="labels"><!-- labels链接 -->
          <ul @mouseover="enterul_la($event)" @mouseout="leaveul_la($event)" class="KSVul" :style="{top:img.height+20+'px'}">
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

</template>

<script>
    export default {
        name: "v-waterfall-test",
        data(){
            return {
                isCollect:false,
                isLike: false,
                waterfallList:[],
                imgArr:[
                    require('../../assets/test/1.jpg'),
                    require('../../assets/test/2.jpg'),
                    require('../../assets/test/3.jpg'),
                    require('../../assets/test/4.jpg'),
                    require('../../assets/test/5.jpg'),
                    require('../../assets/test/6.jpg'),
                    require('../../assets/test/7.jpg'),
                    require('../../assets/test/8.jpg')
                ],
                waterfallImgWidth:350,
                waterfallImgCol:3,
                waterfallImgRight:10,
                waterfallImgBottom:10,
                waterfallDeviationHeight:[],
                imgList:[],
                message: '123',
            }
        },
        created() {
            for (let i = 0;i < 8;i++){
                this.imgList.push(this.imgArr[i]);
            }
        },
        mounted(){
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
  .Liked{
    color: rgb(238,106,132);
  }
  .Collected{
    color: rgb(238,203,106);
  }
  .LabelsOver{
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

.thumbnails .v-waterfall-content{
    width: 100%;
    height: 100%;
    position: absolute;
}
.thumbnails .v-waterfall-content .v-waterfall-item{
    float: left;
    position: absolute;
}
.v-waterfall-item img{
    width: 100%;
    height: auto;
}
</style>
