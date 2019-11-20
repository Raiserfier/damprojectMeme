<template>
  <div class="main_window_setting">
    <!--avatar and buttons-->
    <div class="column_left">
      <form>
        <div class="avatar_container">
          <img :src="portrait" alt="">
          <div><label for="avatar">
            <button class="Change_avatar">更换头像</button>
          </label>
            <input id="avatar" type="file" accept="image/jpeg,image/png,image/bmp" @change="choose_img($event)">
          </div>
        </div>
      </form>
      <router-link :to="'/channel/'+this.$store.state.user_id+'/all'" class="column_button"><i class="icon fa-upload"></i><span style="padding-left: 10px">我的上传</span></router-link>
      <router-link :to="'/favorite/'+this.$store.state.user_id+'/all'" class="column_button"><i class="icon fa-star"></i><span style="padding-left: 10px">我的收藏</span></router-link>
    </div>
    <div class="setting_window">
      <!--Items-->
      <form>
        <div class="form_container">
          <div class="setting_title">
            <div>
              用户设置
            </div>
          </div>
          <!--username-->
          <div class="form_content">
            <div>
              <div class="item_title">
                <div>用户名</div>
              </div>
            </div>
            <label>
              <input minlength="1" maxlength="30" type="text" name="username" placeholder="Username"
                     class="setting_input" v-model="username">
            </label>
          </div>
          <!--email address-->
<!--          <div class="form_content">-->
<!--            <div>-->
<!--              <div class="item_title">-->
<!--                <div>邮箱地址</div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <label>-->
<!--              <input minlength="1" maxlength="30" type="text" name="email" placeholder="email address"-->
<!--                     class="setting_input" :value="this.$store.state.user_id">-->
<!--            </label>-->
<!--          </div>-->
          <!--introduction-->
          <div class="form_content">
            <div>
              <div class="item_title">
                <div>简介</div>
              </div>
            </div>
            <label>
              <textarea name="introduction" placeholder="这个用户很懒..." class="Introduction_input" v-model="profile"></textarea>
<!--              <input placeholder="这个用户很懒..." class="Introduction_input" type="text"/>-->
            </label>
          </div>
          <!--commit button-->
          <div class="setting_buttons">
            <p class="setting_commit_button" @click="user_info_update()">
              确认
            </p>
          </div>
        </div>
      </form>
      <!--Password change-->
      <form :style="{'padding-top': 5+'%'}">
        <div class="form_container">
          <div class="setting_title">
            <div>
              修改密码
            </div>
          </div>
          <!--old password-->
          <div class="form_content">
            <div>
              <div class="item_title">
                <div>旧密码</div>
              </div>
            </div>
            <label>
              <input minlength="1" maxlength="30" type="password" name="old_password" placeholder="Old password"
                     v-model="password_old" class="setting_input">
            </label>
          </div>
          <!--new password-->
          <div class="form_content">
            <div>
              <div class="item_title">
                <div>新密码</div>
              </div>
            </div>
            <label>
              <input minlength="1" maxlength="30" type="password" name="new_password" placeholder="New password"
                     v-model="password_new" class="setting_input">
            </label>
          </div>
          <!--new password confirm-->
          <div class="form_content">
            <div>
              <div class="item_title">
                <div>新密码确认</div>
              </div>
            </div>
            <label>
              <input minlength="1" maxlength="30" type="password" name="new_password_confirm" placeholder="New password confirm"
                     v-model="password_confirm" class="setting_input">
            </label>
          </div>
          <!--commit button-->
          <div class="setting_buttons">
            <p class="setting_commit_button" @click="password_modi()">
              确认
            </p>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Info_setting",
        data(){
            return{
                isRouterAlive:true,
                username: '游客',
                profile: '',
                portrait: '',
                password_old: '',
                password_new: '',
                password_confirm: '',
            }

        },
        created(){
            this.load();
        },
        methods:{
            load(){
                this.$api.post('/get_user_info',{email:this.$store.state.user_id}).then(response=>{
                    if(response.data !== 'Not received'){
                        // console.log(response.data);
                        this.username = response.data.username;
                        this.profile = response.data.profile;
                        this.portrait = response.data.portrait;
                    }
                }),(response)=>{
                    //console.log("error");
                    this.$message.error('用户信息获取失败');
                }
            },
            choose_img(e) {
                if(e.target.files[0]){
                    let reader = new FileReader();
                    let that = this;
                    reader.readAsDataURL(e.target.files[0]);
                    reader.onload = function (e) {
                        // console.log(this.result);
                        let image = new Image(); //新建一个img标签（还没嵌入DOM节点)
                        image.src = this.result;
                        image.onload = function () {
                            let canvas = document.createElement('canvas'), // 新建canvas
                                context = canvas.getContext('2d');
                            let imageHeight = image.height, imageWidth = image.width, data = '';
                            if (image.height > image.width) {
                                if (image.height > 200) {
                                    imageHeight = 200;
                                    imageWidth = image.width / image.height * 200;
                                }
                            } else {
                                if (image.width > 200) {
                                    imageWidth = 200;
                                    imageHeight = image.height / image.width * 200;
                                }
                            }
                            canvas.width = imageWidth;
                            canvas.height = imageHeight;
                            context.drawImage(image, 0, 0, imageWidth, imageHeight);
                            data = canvas.toDataURL('image/jpeg'); // 输出压缩后的base64
                            // console.log(data);
                            that.portrait = data;
                        }
                    }
                }
                // this.user_info_update();
            },
            user_info_update(){
                console.log(this.$store.state.user_id,this.username,this.profile,this.portrait);
                this.$api.post('/modify_user_info',{email:this.$store.state.user_id, username:this.username, profile:this.profile, portrait:this.portrait}).then(response=>{
                    if(response.data === 'success'){
                        this.$message.success('成功更改个人信息');
                    }else{
                        this.$message.warning('更改个人信息失败');
                    }
                }),(response)=>{
                    this.$message.error('更改个人信息失败');
                }
                // this.$router.replace({path: '/settings'});
                // this.load();
            },
            password_modi(){
                console.log()
                if(this.password_new !== this.password_confirm){
                    this.$message.warning('两次输入的新密码不同，请重新确认');
                    this.password_new = '';
                    this.password_confirm = '';
                    return;
                }else{
                    this.$api.post('/modify_password',{email:this.$store.state.user_id, password_old:this.password_old, password_new:this.password_new}).then(response=>{
                        if(response.data === 'success'){
                            this.$message.success('成功更改密码');
                        }else if(response.data === 'error'){
                            this.$message.warning('用户密码输入错误');
                        }else{
                            this.$message.warning('密码更改失败');
                        }
                    }),(response)=>{
                        this.$message.error('密码更改失败');
                    }
                }
                // this.password_new = '';
                // this.password_old = '';
                // this.password_confirm = '';
                // this.load();
            },
        }
    }
</script>

<style scoped>
  .main_window_setting {
    width: 1040px;
    display: flex;
    font-size: 14px;
    font-weight: bold;
    text-align: center;
    padding-top: 7%;
    padding-left: 20%;
  }

  .column_left {
    margin-right: 17px;
    display: flex;
    flex-direction: column;
  }

  .avatar_container {
    display: flex;
    flex-direction: column;
    position: relative;
    width: 200px;
  }

  .avatar_container input[type="file"] {
    height: 100%;
    left: 0px;
    opacity: 0;
    position: absolute;
    top: 0px;
    width: 100%;
  }

  .avatar_container img {
    width: 100%;
    height: auto;
  }

  .Change_avatar {
    border: none;
    white-space: nowrap;
    box-sizing: border-box;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-family: inherit;
    font-size: 14px;
    font-weight: bold;
    height: 36px;
    line-height: 36px;
    min-width: 36px;
    text-align: center;
    user-select: none;
    -webkit-appearance: none;
    -webkit-font-smoothing: antialiased;
    background-color: rgb(97, 87, 255);
    margin-bottom: 7px;
    width: 100%;
    outline: none;
    padding: 0px 15px;
    display: inline-block;
    text-transform: none;
  }

  .column_button {
    color: rgb(0, 204, 255);
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    padding: 10px;
    text-decoration: none;
  }

  .setting_window {
    flex: 1 1 0%;
  }

  .form_container {
    display: flex;
    flex-direction: column;
    -webkit-box-pack: start;
    justify-content: flex-start;
    background: rgb(44, 44, 47);
    padding: 35px 90px 35px 55px;
  }

  .setting_title {
    font-family: nexablack, sans-serif;
    -webkit-font-smoothing: antialiased;
    font-size: 36px;
    margin-bottom: 40px;
    text-align: left;
  }

  .item_title {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    width: 100px;
  }

  .form_content {
    font-weight: normal;
    margin-top: 0px;
    height: 40px;
    width: 100%;
    position: relative;
    display: flex;
  }

  .setting_input {
    border-radius: 5px;
    height: 30px;
    width: 400px;
    box-sizing: border-box;
    padding: 5px 5px 5px 12px;
    border: none;
    font-size: 14px;
    font-weight: 400;
    line-height: normal;
    color: rgb(0, 0, 0);
    margin: 0px 0px 10px;
    outline: none;
  }

  .Introduction_input {
    border-radius: 5px;
    width: 400px;
    height: auto;
    font-size: 14px;
    font-weight: 400;
    line-height: normal;
    color: rgb(0, 0, 0);
    margin: 0px;
    padding: 10px;
    outline: none;
    box-sizing: border-box;
    border: none;
  }

  .setting_buttons {
    width: 400px;
    margin: 0;
    padding: 10px;
    height: auto;
  }

  .setting_commit_button {
    border-radius: 5px;
    border: none;
    white-space: nowrap;
    box-sizing: border-box;
    color: rgb(255, 255, 255);
    cursor: pointer;
    font-family: inherit;
    font-size: 14px;
    font-weight: bold;
    height: 36px;
    line-height: 36px;
    min-width: 36px;
    text-align: center;
    user-select: none;
    -webkit-appearance: none;
    -webkit-font-smoothing: antialiased;
    background-color: rgb(97, 87, 255);
    margin-bottom: 7px;
    width: 400px;
    margin-left: 90px;
    outline: none;
    padding: 0px 15px;
    margin-top: 40px;
    transition: all 0.2s ease 0s;
  }
  .setting_commit_button:hover{
    background-color: rgb(255, 255, 255);
    color: rgb(97, 87, 255);
  }

  textarea {
    -webkit-writing-mode: horizontal-tb !important;
    text-rendering: auto;
    color: initial;
    letter-spacing: normal;
    word-spacing: normal;
    text-transform: none;
    text-indent: 0px;
    text-shadow: none;
    display: inline-block;
    text-align: start;
    -webkit-appearance: textarea;
    background-color: white;
    -webkit-rtl-ordering: logical;
    flex-direction: column;
    cursor: text;
    white-space: pre-wrap;
    overflow-wrap: break-word;
    margin: 0em;
    font: 400 13.3333px Arial;
    border-width: 1px;
    border-style: solid;
    border-color: rgb(169, 169, 169);
    border-image: initial;
    padding: 2px;
}
</style>
