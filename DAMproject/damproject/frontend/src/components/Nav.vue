<template>
  <div class="top-nav">
    <!-- Header -->
    <header id="header" class="hello">
      <router-link to="/" class="logo"><strong>MEEEEME</strong></router-link>
      <nav>
        <div class="fnwVXu"><!-- 导航栏 -->
          <ul>
            <li v-for="c in categories" class="topBar">
              <router-link :to="'/category/'+c.id" class="fnxsKA">{{c.name}}</router-link>
            </li>
            <!--            <li class="topBar" >-->
            <!--              <router-link to="/animal" class="fnxsKA">动物</router-link>-->
            <!--            </li>-->
            <!--            <li class="topBar" >-->
            <!--              <router-link to="/food" class="fnxsKA">食物</router-link>-->
            <!--            </li>-->
            <!--            <li class="topBar" >-->
            <!--              <router-link to="/anime" class="fnxsKA">动画</router-link>-->
            <!--            </li>-->
            <!--            <li class="topBar" >-->
            <!--              <router-link to="/game" class="fnxsKA">游戏</router-link>-->
            <!--            </li>-->
            <!--            <li class="topBar" >-->
            <!--              <router-link to="/people" class="fnxsKA">人物</router-link>-->
            <!--            </li>-->

            <!--            * 测试-->
<!--            <li class="topBar">-->
<!--              <router-link to="/upload" class="fnxsKA">测试:上传</router-link>-->
<!--            </li>-->
<!--            <li class="topBar">-->
<!--              <router-link :to="'/channel/'+this.$store.state.user_id+'/all'" class="fnxsKA">我的上传</router-link>-->
<!--            </li>-->
<!--            <li class="topBar">-->
<!--              <router-link :to="'/favorite/'+this.$store.state.user_id+'/all'" class="fnxsKA">我的收藏</router-link>-->
<!--              &lt;!&ndash;              <router-link to="/favorite" class="fnxsKA">我的收藏</router-link>&ndash;&gt;-->
<!--            </li>-->
            <li class="topBar">
              <router-link to="/recommend" class="fnxsKA">猜你喜欢</router-link>
            </li>
<!--            <li class="topBar">-->
<!--              <router-link to="/login" class="fnxsKA">登录</router-link>-->
<!--            </li>-->
          </ul>
        </div>
        <div class="container"><!-- 搜索框 -->
          <div class="search bar1">
            <label>
              <input style="width: 250px" type="text" @keyup.enter="search_self($event)" placeholder="搜索全站...">
            </label>
            <button @click="search($event)"></button>
          </div>

          <!--        * 先判断登录状态-->
          <!--        * 若未登录,显示登录按钮:样式和上传按钮一样,跳转到/login-->
          <!--        * 若已登录,显示上传按钮和menu-->

          <div v-if="!this.$store.state.login"><!--登录按钮-->
            <form>
              <button class="upload login"><span><router-link class="upload-button" to="/login">登录</router-link></span>
              </button>
            </form>
          </div>

          <div v-if="!this.$store.state.login"><!--注册按钮-->
            <form>
              <button class="upload register"><span><router-link class="upload-button" to="/register">注册</router-link></span>
              </button>
            </form>
          </div>

          <div v-if="this.$store.state.login"><!--上传按钮-->
            <form>
              <button class="upload upp"><span><router-link class="upload-button" to="/upload">上传</router-link></span>
              </button>
            </form>
          </div>
          <div class="Menu" v-if="this.$store.state.login">
            <!--            <a href="#menu">菜单</a>-->
            <a href="#menu" @click="dropbox($event,this)">菜单</a>
          </div>
        </div>
      </nav>
    </header>

    <!-- Nav -->
    <nav id="menu" v-if="this.$store.state.login" v-bind:class="{ MENU: isActive }">
      <ul class="links">
        <!-- 导航栏 -->
        <!--        * 根据user_id动态分配路由-->
        <li @click="jump">
          <router-link :to="'/channel/'+this.$store.state.user_id+'/all'">我的上传</router-link>
        </li>
        <li @click="jump">
          <router-link :to="'/favorite/'+this.$store.state.user_id+'/all'">我的收藏</router-link>
        </li>
        <li @click="jump">
          <router-link to="/settings">个人设置</router-link>
        </li>
        <li @click="logout">
          <router-link to="/">退出登录</router-link>
        </li>
      </ul>
    </nav>
  </div>
  <div>
    <router-view :key="key"></router-view>
  </div>
</template>

<script>
    export default {
        name: "Nav",
        data() {
            return {
                categories: [{name: '动物', id: 'chrome'},
                    {name: '食物', id: 'safari'},
                    {name: '动画', id: 'Edge'},
                    {name: '游戏', id: 'firefox'},
                    {name: '人物', id: 'ie8'}],
                keyw: 'all',
                my_id: '',
                isActive: false,
            }
        },
        created() {
            // this.get_categories();
        },
        mounted(){
            this.my_id = this.$store.state.user_id;
            console.log('create :  '+this.$store.state.user_id);
        },
        computed: {
            key() {
                this.my_id = this.$store.state.user_id;
                return this.$route.path + Math.random();
            }
        },
        methods: {
            dropbox(e) {
                this.isActive = !this.isActive;
            },
            logout() {
                console.log("logout");
                this.isActive = false;
                this.$store.state.login = false;
                this.$store.state.user_id = "99";
                this.$store.state.user_name = "Tester";
                // this.$router.replace({ path: '' });
                this.my_id = "99";
                console.log(this.$store.state.login);
                console.log(this.$store.state.user_id);
            },
            jump() {
                console.log("jump");
                this.isActive = false;
                this.my_id = this.$store.state.user_id;
                // this.$router.replace({ path: '/channel/user-id' });
            },
            //点击搜索跳转
            search_self(e) {
                // console.log(this.$store.state.login)
                this.keyw = e.target.value.trim();
                if (this.keyw == '') this.keyw = 'all'
                e.target.value = '';
                this.$router.replace({path: '/search/' + this.keyw});
                this.$parent.$children.$forceUpdate()
            },
            search(e) {
                // console.log(this.$store.state.login)
                this.keyw = e.target.previousElementSibling.firstElementChild.value.trim();
                if (this.keyw == '') this.keyw = 'all'
                e.target.previousElementSibling.firstElementChild.value = '';
                this.$router.replace({path: '/search/' + this.keyw});
                this.$parent.$children.$forceUpdate()
            },
            //从后端获取类别
            get_categories() {
                this.$api.post('/get_categories').then(response => {
                    //console.log(response.data);
                    let op = [];
                    for (let i = 0; i < response.data.length; i++) {
                        op.push(response.data.cat);//cat是类别数组，每个元素里有id和name两个值
                    }
                    this.categories = op;
                }), (response) => {
                    //console.log("error");
                    this.$message.error('类别获取失败！');
                }
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #header .logo{
    padding-left: 20px;
  }
  #menu{
    right: 30px;
  }
  .Menu{
    left: 468px;
  }
  form {
    margin: 0 0 -6.15em;
  }
  div.search {
    padding: 0 175px 0 0;
  }
  button.login{
   left: 350px;
  }
  button.register{
    left: 470px;
    background: rgb(89, 89, 89);
  }
  button.upp{
   left: 350px;
  }
  button.register:hover{
		color: rgb(89, 89, 89);
    background: white;
	}
  .fnwVXu {
    margin: 0 18em 0 14em;
  }
  #header nav a:not(.upload-button .Menu) {
    padding: 0 1.5em;
  }

  .bar1 button{
    left: 290px;
  }
  .MENU {
    /*top:225px !important;*/
    visibility: visible !important;
    transform: translateY(1px) !important;
  }

  .Menu {
    height: 110px;
  }

  .topBar {
    padding-right: 1.5em;
  }

  .upload-button {
    padding-right: 0em;
  }

  .fnwVXu {
    width: 900px;
  }

  a, span, input {
    font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif;
  }

  /* Header */
  body {
    padding-top: 4.125em;
  }

  #header {
    background: #1c1c1c;
    color: rgba(255, 255, 255, 0.75);
    cursor: default;
    height: 4.25em;
    left: 0;
    line-height: 4.25em;
    position: fixed;
    text-align: right;
    top: 0;
    width: 100%;
    z-index: 20;
  }

  #header .logo {
    display: inline-block;
    height: inherit;
    /*left: 1.25em;*/
    left: 4em;
    line-height: inherit;
    margin: 0;
    padding: 0;
    position: absolute;
    top: 0;
    color: #fff;
    font-size: 1.25em;
    text-decoration: none;
  }

  #header .logo strong {
    color: inherit;
    font-weight: 700;
  }

  /* topBar*/
  #header .topBar {
    line-height: inherit;
    margin: 0;
    padding: 0;
    top: 0;
    text-decoration: none;
    cursor: pointer;
    float: left;
    height: 4.25em;
    position: relative;
    display: flex;
    -webkit-box-flex: 1;
    flex-grow: 1;
    -webkit-box-align: center;
    align-items: center;
  }

  a.fnxsKA:hover {
    color: rgb(255, 255, 255);
  }

  @media screen and (max-width: 1280px) {
    .fnxsKA {
      font-size: 15px;
    }

    .fnwVXu {
      width: 496px;
      margin: 0 18em 0 15em;
    }
  }

  @media screen and (max-width: 980px) {
    .fnxsKA {
      font-size: 10px;
    }

    .fnwVXu {
      width: 496px;
      margin: 0 12em 0 15em;
    }
  }

  @media screen and (max-width: 736px) {
    .fnxsKA {
      font-size: 5px;
    }

    .fnwVXu {
      width: 496px;
      margin: 0 9em 0 10em;
    }
  }

  #header nav a:not(.upload-button) {
    -moz-transition: color 0.2s ease-in-out;
    -webkit-transition: color 0.2s ease-in-out;
    -ms-transition: color 0.2s ease-in-out;
    transition: color 0.2s ease-in-out;
    display: inline-block;
    padding: 0 0.75em;
    color: inherit;
    text-decoration: none;
  }

  .upload-button {
    -moz-transition: color 0.2s ease-in-out;
    -webkit-transition: color 0.2s ease-in-out;
    -ms-transition: color 0.2s ease-in-out;
    transition: color 0.2s ease-in-out;
    display: inline-block;
    padding-right: 0em;
    color: inherit;
    text-decoration: none;
  }

  #header nav a:hover {
    color: #fff;
  }

  #header nav a[href="#menu"] {
    width: 80px;
    height: 110px;
    text-decoration: none;
    -webkit-tap-highlight-color: transparent;
  }

  #header ul {
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased;
    text-decoration: none;
    list-style: none;
    margin-block-start: 0;
    margin-block-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
    padding-inline-start: 0;
  }

  #header nav a[href="#menu"]:before {
    content: "";
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    font-family: FontAwesome, serif;
    font-style: normal;
    font-weight: normal;
    text-transform: none !important;
  }

  #header nav a[href="#menu"]:before {
    margin: 0 0.5em 0 0;
  }

  #header nav a + a[href="#menu"]:last-child {
    border-left: solid 1px rgba(255, 255, 255, 0.25);
    padding-left: 1.25em;
    margin-left: 0.5em;
  }

  #header nav a:last-child :not(.upload-button) {
    padding-right: 2em;
  }

  @media screen and (max-width: 736px) {

    #header nav a {
      padding: 0 0.5em;
    }

    #header nav a + a[href="#menu"]:last-child {
      padding-left: 1em;
      margin-left: 0.25em;
    }

    #header nav a:last-child {
      padding-right: 1em;
    }

  }

  @media screen and (max-width: 980px) {

    body {
      padding-top: 44px;
    }

    #header {
      height: 44px;
      line-height: 44px;
    }

    #header .logo {
      left: 1em;
      font-size: 1em;
    }

  }

  @media screen and (max-width: 480px) {

    #header {
      min-width: 320px;
    }

  }

  /* Search */
  .container {
    bottom: 0;
    height: 107px;
    position: absolute;
    line-height: 150px;
    right: 120px;
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

  div.search {
    padding: 0 0;
    padding-right: 175px;
  }

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
    height: 33px;
    padding-left: 13px;
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
    top: 60px;
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
    top: 59px;
    right: 0;
    border-radius: 0 5px 5px 0;
    height: 32px;
    width: 32px;
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
