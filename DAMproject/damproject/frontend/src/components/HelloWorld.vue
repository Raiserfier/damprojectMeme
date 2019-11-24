17-树莓-孙文欣 2019/11/4 13:32:08
<template>
  <div class="login-list">
    <form>
      <input class="form-control" type="text" placeholder="请输入登录邮箱" required="" name="email" @input="input($event)">
      <input class="form-control" type="password" placeholder="请输入密码" required="" name="password" @input="input($event)">

      <div class="form-button">
        <p id="submit" class="ibtn" @click="login">Login</p>
        <a href="">Forget password?</a>
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
                if (this.email===""){
                    this.$message.error('未填写登录邮箱!');
                }
                else if (this.password===""){
                    this.$message.error('未填写密码！');
                }
                else {
                    console.log('login function');
                    // this.$store.commit("login",{userid:"1", username:"2"});
                    // console.log(this.$store.state.user_id, this.$store.state.user_name);
                    this.$api.post('/login', {username:this.name,email: this.email, password: this.password}).then(response => {
                        //var res = JSON.parse(response.data);
                        //res = response.data;
                        console.log(response.data);
                        if (response.data.msg === "SUCCESS") {
                            // 更新store登录状态
                            this.$store.commit("login",{userid:this.email, username:response.data.username});
                            this.$message.success('登录成功!');
                            // 跳转个人页
                            this.$router.replace({ path: '/channel/user-id' });
                        }
                        else if (response.data === 'ERROR') {
                            this.$message.error('登录失败，密码错误!');
                        }
                    })
                }
            }
        }
    }
</script>

<style scoped>

</style>
