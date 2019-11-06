<template>
  <div class="register">
    <form>
      <input class="form-control" name="name" placeholder="用户名" required="" type="text" @input="input($event)">
      <input class="form-control" name="email" placeholder="登录邮箱" required="" type="text" @input="input($event)">
      <input class="form-control" name="password" placeholder="密码" required="" type="password" @input="input($event)">
      <div class="form-button">
        <p class="ibtn" id="submit" type="submit" @click="register">注册</p>
      </div>
    </form>
  </div>
</template>

<script>
    export default {
        name: "Register",
        data(){
            return {
                name:"",
                email:"",
                password:""
            }
        },
        methods: {
            input(e){
                if(e.target.name==='email'){
                    this.email = e.target.value;
                }
                else if(e.target.type==='password'){
                    this.password = e.target.value;
                }
                else if(e.target.name === 'name'){
                    this.name = e.target.value;
                }
            },
            register(){
                // if(this.email===""){
                //     this.$message.error('未填写登录邮箱!');
                // }
                // else if(this.name===""){
                //     this.$message.error('未填写登录昵称!');
                // }
                // else if(this.password===""){
                //     this.$message.error('未填写密码！');
                // }
                // else{
                    console.log('register function');
                    this.$api.post('/register', {username:this.name, email: this.email, password: this.password}).then(response => {
                        console.log(response.data);
                        if (response.data === 'SUCCESS') {
                            // 更新store登录状态
                            this.$store.commit("login", {userid:this.email, username:this.name});
                            this.$message.success('注册并登录成功!');
                            // 跳转个人页
                            this.$router.replace({ path: '/channel/'+this.$store.state.user_id+'/all' });
                        }
                        else if (response.data === "EXIST") {
                            this.$message.error('该邮箱已被注册！');
                        }
                    })
                // }
            }
        }
    }
</script>

<style scoped>
.ibtn {
    width: 88px;
}
a {
    cursor: hand;
    text-decoration: underline;
}
.register {
    padding-top: 50px;
}
.form-content .form-button  {
    padding-top: 0;
}
.form-content .form-button .ibtn {
    color: #ee6a84;
}
</style>
