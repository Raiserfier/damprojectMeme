import  Vue from 'vue'
import Vuex from 'vuex'
import Router from "vue-router"

Vue.use(Vuex)

export default new Vuex.Store({
  //设置属性
  state:{
      //登录状态
      login: false,
      user_id: "99",
      user_name: "Tester",
      manager: false
    },

  //获取属性的状态
  getters:{
      //获取到设置的属性的状态
  },

  //改变属性的状态
  mutations:{
      //登录状态更新
      login(state,userid,username,isManager){
          state.login = true;
          state.user_id = userid;
          state.user_name = username;
          state.manager = isManager;
      },
      logout(state){
          state.login = false;
          state.user_id = "99";
          state.user_name = "Tester";
          state.manager = false;
      }
  }
})
