<template>
  <div class="main_window_setting">
    <!--avatar and buttons-->
    <div class="column_left">
      <form>
        <div class="avatar_container">
          <img src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3900046848,1834418761&fm=26&gp=0.jpg"
               alt="">
          <div><label for="avatar">
            <button class="Change_avatar">更换头像</button>
          </label>
            <input id="avatar" type="file" accept="image/*">
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
                     class="setting_input" :value="this.$store.state.user_name">
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
              <textarea name="introduction" placeholder="这个用户很懒..." class="Introduction_input"></textarea>
<!--              <input placeholder="这个用户很懒..." class="Introduction_input" type="text"/>-->
            </label>
          </div>
          <!--commit button-->
          <div class="setting_buttons">
            <button class="setting_commit_button">
              确认
            </button>
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
                     class="setting_input">
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
                     class="setting_input">
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
                     class="setting_input">
            </label>
          </div>
          <!--commit button-->
          <div class="setting_buttons">
            <button class="setting_commit_button">
              确认
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
    export default {
        name: "Info_setting"
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
