<template>
    <div class="user">
      <div class="container" id="login-container">
        <div class="form-body">
          <div class="row">
            <div class="form-holder">
              <div class="form-content">
                <div class="form-items">
                  <h3>Welcome</h3>
                  <p></p>
                  <router-link to="/login" id="login-tab">登录</router-link>
                  <router-link to="/register" id="register-tab">注册</router-link>

                  <transition name="fade" mode="out-in">
                    <router-view/>
                  </transition>
                </div>
              </div>
                <!-- Footer -->
              <footer id="footer">
                  <p>&copy; 2019. Group 2. All rights reserved.</p>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: 'User'
    }
</script>

<style scoped>
.user {
    background-image: url("../assets/images/Light.jpg");
    background-size: 100%;
    background-repeat: no-repeat;
}
.form-content {
    /*background-color: #202024;*/
}
#footer::before {
    margin: 0 auto 1.5em auto;
}
#footer p{
    cursor: text;
}
#footer {
    /*background-color: #495057;*/
    /*background-color: #202024;*/
    padding-top: 1.5em;
    padding-bottom: 5em;
}
#register-tab::after {
    position: absolute;
    content: "";
    width: 100%;
    height: 2px;
    left: 0;
    bottom: -10px;
    background-color: rgba(255, 255, 255, 0.5);
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#register-tab.router-link-exact-active::after {
    background-color: #fff;
}
#register-tab.router-link-exact-active {
    font-weight: 700;
}
#register-tab {
    position: relative;
    display: inline-block;
    text-decoration: none;
    color: #fff;
    font-weight: 300;
    font-size: 15px;
    margin-right: 20px;
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#register-tab {
    transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    outline: 0;
}
#login-tab::after {
    position: absolute;
    content: "";
    width: 100%;
    height: 2px;
    left: 0;
    bottom: -10px;
    background-color: rgba(255, 255, 255, 0.5);
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#login-tab.router-link-exact-active::after {
    background-color: #fff;
}
#login-tab.router-link-exact-active {
    font-weight: 700;
}
#login-tab {
    position: relative;
    display: inline-block;
    text-decoration: none;
    color: #fff;
    font-weight: 300;
    font-size: 15px;
    margin-right: 20px;
    -webkit-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#login-tab {
    transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
    outline: 0;
}
.form-content h3 {
    padding-top: 0;
    color: #fff;
    text-align: left;
    font-size: 60px;
    font-weight: 900;
    margin-bottom: 8px;
}
#login-container {
    padding-top: 4.25em;
    margin: 0;
    /*padding: 0;*/
    border: 0;
    /*font-size: 100%;*/
    font: inherit;
    vertical-align: baseline;
    font-family: 'Lato', sans-serif;
    font-weight: 400;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    -moz-osx-font-smoothing: grayscale;
    -moz-box-sizing: border-box;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    font-size: 11pt;
    color: rgba(255, 255, 255, 0.75);
    /*font-family: "Source Sans Pro", sans-serif;*/
    /*font-size: 14pt;*/
    /*font-weight: 300;*/
    line-height: 1.65;
    -webkit-text-size-adjust: none;
}
</style>
