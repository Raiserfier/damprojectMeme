<template>
  <div class="channel">
    <!-- Banner -->
    <section id="banner" data-video="images/banner">
      <div class="inner">
        <header>
          <!-- 用户头像 -->
          <span class="avatar"><img src="../assets/images/avatar.jpg" alt=""/></span>
          <!-- 用户名 调state -->
          <h1>{{this.username}}</h1>
          <!--					<p>A responsive video gallery template with a functional lightbox<br />-->
          <!--						designed by Templated and released under the Creative Commons License.</p>-->
          <div class="container"><!-- 搜索框 -->
            <div class="search bar3">
<!--              <form>-->
                <label v-if="!this.$store.state.manager">
                  <input type="text" @keyup.enter="search_self($event)" placeholder="搜索我的上传...">
                </label>
                <label v-if="this.$store.state.manager">
                  <input type="text" @keyup.enter="search_self($event)" placeholder="搜索举报图片...">
                </label>
                <button @click="search($event)"></button>
<!--              </form>-->
            </div>
          </div>
<!--          <div class="info_line" v-if="this.$store.state.manager">-->
<!--            <li @click="delete_all">-->
<!--          <p>一键清除</p>-->
<!--        </li>-->
<!--          </div>-->
        </header>
      </div>
    </section>

    <user-uploads></user-uploads>
    <!--    <test-images></test-images>-->
    <!--    <test-images1></test-images1>-->
  </div>
</template>

<script>
    import ImageStream from './ImagePage/ImageStream'

    export default {
        name: 'Channel',
        components: {
            'user-uploads': ImageStream,
        },
        data() {
            return {
                msg: "在图库中搜索...",
                keyw: 'all',
                username:'Test',
            };
        },
        created(){
             if (this.$route.params.id !== undefined) {
                this.$api.post('/get_username', {email: this.$route.params.id}).then(response => {
                    console.log(response.data);
                    if (response.data !== 'no such user') {
                        this.username = response.data;
                    } else {
                        this.$message.warning('主页加载错误');
                    }
                }), (response) => {
                    this.$message.error('主页加载错误');
                }
            }//用户页
        },
        methods: {
            // search_user(e) {
            //     this.keyw = e.target.text.trim();
            //     if (this.keyw == '') this.keyw = 'all'
            //     console.log(this.keyw);
            //     console.log(this.$route.params);
            //     // console.log(merge(this.$route.query, {'key': this.keyw}));
            //     // this.$router.push({query: merge(this.$route.query, {'key': this.keyw})});
            //     this.$router.push({name:'PageWithSearch', params:{type:this.$route.params.type,id:this.$route.params.id,key:this.keyw}});
            // },
            //点击搜索跳转
            search_self(e) {
                this.keyw = e.target.value.trim();
                if (this.keyw == '') this.keyw = 'all';
                this.$router.push({name:'PageWithSearch', params:{type:this.$route.params.type,id:this.$route.params.id,key:this.keyw,rank:'hot'}});
            },
            search(e) {
                this.keyw = e.target.previousElementSibling.firstElementChild.value.trim();
                if (this.keyw == '') this.keyw = 'all';
                this.$router.push({name:'PageWithSearch', params:{type:this.$route.params.type,id:this.$route.params.id,key:this.keyw,rank:'hot'}});
            },
            delete_all(){
              this.$api.post('/delete_report', {}).then(response => {
                    if (response.data === 'SUCCESS') {
                        this.$message.success('清除成功！');
                        this.$router.replace({ path: '/' });
                    }
                }), (response) => {
                    //console.log("error");
                    this.$message.error('清除失败！');
                }
            }
        }
    }
</script>

<style scoped>
  .channel {
    padding-top: 4.25em;
    min-height: 60vh;
  }

  #banner {
    margin-bottom: 2.5em;
    padding: 0;
    /*background-image: url("../assets/images/Veil.jpg");*/
  }

  #banner h1 {
    font-size: 4em;
    font-weight: 400;
    font-family: "sans-serif";
    margin: 0;
  }

  #banner .avatar img {
    width: 9em;
  }

  div.search {
    padding-top: 1.5em;
  }

  /* Search */
  .container {
    bottom: 0;
    height: 107px;
    /*position: absolute;*/
    /*line-height: 150px;*/
    /*right: 120px;*/
    width: 500px;
    margin: 0 auto;
  }

  button.container {
    -webkit-appearance: button;
    -webkit-writing-mode: horizontal-tb !important;
    text-rendering: auto;
    color: buttontext;
    letter-spacing: normal;
    word-spacing: normal;
    text-transform: none;
    text-indent: 0;
    text-shadow: none;
    display: inline-block;
    text-align: center;
    align-items: flex-start;
    cursor: default;
    background-color: buttonface;
    box-sizing: border-box;
    margin: 0;
    font: 400 13.3333px Arial;
    padding: 1px 6px;
    border-width: 2px;
    border-style: outset;
    border-color: buttonface;
    border-image: initial;
  }

  /*div.search {padding: 0 0;}*/

  body.container {
    margin: 0;
    padding: 0;
    background: #494A5F;
    font-weight: 500;
    font-family: "Microsoft YaHei", "宋体", "Segoe UI", "Lucida Grande", Helvetica, Arial, sans-serif, FreeSans, Arimo;
  }

  form {
    position: relative;
    margin: 0 0 -6.2em 0;
  }

  input, button {
    border: none;
    outline: none;
  }

  input {
    width: 100%;
    /*height: 33px;*/
    padding-left: 13px;
    height: 39px;
  }

  button {
    /*height: 42px;*/
    /*width: 42px;*/
    cursor: pointer;
    position: absolute;
  }

  ::-webkit-input-placeholder { /* WebKit, Blink, Edge */
    color: rgba(198, 196, 196, 0.73);
  }

  .bar1 form {
    width: 200px;
    margin: 0 0 0 12em;
  }

  .bar1 input {
    border: 0;
    padding: 5px 40px 5px 13px;
    font-size: 14px;
    border-bottom: solid 1px;
    text-shadow: none;
    border-radius: 6px;
    background: #ffffff;
    color: #343232;
    outline: none;
  }

  .bar1 button {
    top: 59px;
    right: 0;
    background: rgb(238, 106, 132);
    border-radius: 0 5px 5px 0;
    height: 33px;
    width: 35px;
    cursor: pointer;
    position: absolute;
    border: none;
  }

  .bar1 button:before {
    content: "\f002";
    font-family: FontAwesome, serif;
    font-size: 16px;
    color: #ffffff;
  }

  .bar3 form {
    width: 400px;
    margin: 3em 0 0 3.5em;
  }

  .bar3 input {
    border: 0;
    padding: 5px 40px 5px 13px;
    font-size: 14px;
    border-bottom: solid 1px;
    text-shadow: none;
    border-radius: 6px;
    background: #ffffff;
    color: #343232;
    outline: none;
  }

  .bar3 button {
    /*top: 59px;*/
    right: 0;
    border-radius: 0 5px 5px 0;
    height: 38px;
    width: 38px;
    cursor: pointer;
    position: absolute;
    border: none;
    background: #ffffff;
  }

  .bar3 button:before {
    content: "\f002";
    font-family: FontAwesome, serif;
    font-size: 16px;
    color: rgb(238, 106, 132);
  }

  @media screen and (max-width: 1280px) {
    .bar1 {
      padding: 0;
      font-size: 14px;
    }
  }

  @media screen and (max-width: 980px) {

    .bar1 {
      padding: 0;
      font-size: 14px;
    }

    .bar1 form {
      width: 180px;
      margin: 0 0 0 12em;
    }
  }

  @media screen and (max-width: 736px) {

    .bar1 {
      padding: 0;
      font-size: 14px;
    }

    .bar1 form {
      width: 150px;
      margin: 0 0 0 18em;
    }

    .bar1 input {
      height: 80%;
      width: 80%;
      padding: 5px 30px 5px 10px;
      font-size: 8px;
    }

    .bar1 button {
      top: 4em;
      margin-top: 7px;
      height: 15%;
      width: 15%;
    }
  }
</style>
