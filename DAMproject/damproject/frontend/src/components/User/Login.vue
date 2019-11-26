<template>
  <div class="login-list">
    <form>
      <input class="form-control" type="text" placeholder="请输入登录邮箱" required="" name="email" @change="input($event)">
      <input class="form-control" type="password" placeholder="请输入密码" required="" name="password" @change="input($event)">

      <div class="form-button">
<!--        <button id="submit" class="ibtn" @click="login">登录</button>-->
        <p class="ibtn" @click="login">登录</p>
        <a @click="easterEgg">忘记密码?</a>
      </div>
    </form>
  </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                email: "",
                password: ""
            }
        },
        methods: {
            input(e) {
                if(e.target.name==='email'){
                    this.email = e.target.value;
                }
                else if(e.target.type==='password'){
                    this.password = e.target.value;
                }
            },
            login() {
                // if (this.email===""){
                //     this.$message.error('未填写登录邮箱!');
                // }
                // else if (this.password===""){
                //     this.$message.error('未填写密码！');
                // }
                // else {
                    console.log('login function');
                    this.$api.post('/login', {email: this.email, password: this.password}).then(response => {
                        console.log(response.data);
                        if (response.data.msg === "SUCCESS") {
                            // 更新store登录状态
                            // this.$store.commit("login",{userid:this.email, username:response.data.username});
                            this.$store.state.login = true;
                            this.$store.state.user_id = this.email;
                            this.$store.state.user_name = response.data.username;
                            this.$store.state.manager = response.data.manager;
                            console.log(this.$store.state.login);
                            console.log(this.$store.state.user_id);
                            console.log(this.$store.state.user_name);
                            this.$message.success('登录成功！');
                            // 跳转个人页
                            this.$router.replace({ path: '/favorite/'+this.$store.state.user_id+'/all'+'/hot' });
                        }
                        else if (response.data === '密码错误') {
                            this.$message.error('登录失败，请确认您的用户名和密码！');
                        }
                    })
                // }
            },
            easterEgg() {
                this.$message.warning('哈哈哈哈傻逼，密码都不记得！');
            }
        }
    }
</script>

<style scoped>
.ibtn {
    width: 88px;
}
a {
    cursor: pointer;
    text-decoration: underline;
}
.login-list {
    padding-top: 60px;
}
.form-content .form-button  {
    padding-top: 1em;
    /*color: #ee6a84;*/
    /*box-shadow: 0 0 0 #ee6a84;*/
    /*background-color: #29A4FF;*/
}
.form-content .form-button .ibtn {
    color: #ee6a84;
}
</style>
