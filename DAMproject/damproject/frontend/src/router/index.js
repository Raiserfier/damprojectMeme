import Vue from 'vue'
import Router from 'vue-router'

import Home from '../components/Home'
import Home1 from "../components/Home1";
import Channel from '../components/Channel'
import Recommend from '../components/Recommend';
import PicDetail from "../components/PicDetail";
import Info_setting from "../components/Info_setting";
import Upload from '../components/Upload'
import User from '../components/User'
import Login from '../components/User/Login'
import Title from '../components/Title'
import Register from '../components/User/Register'

Vue.use(Router)

export default new Router({
  routes: [
    {path: '/', name: 'Home', component: Home1},
    {path: '/details/:pic', name: 'PicDetail', component: PicDetail},
    {path: '/:type/:key', name: 'PageWithTitle', component: Title},
    {path: '/:type/:id/:key', name: 'PageWithSearch', component: Channel},
    {path: '/recommend', name: 'Recommend', component: Recommend},
    {path: '/upload', name: 'Upload', component: Upload},
    {path: '/settings', name: 'Info_setting', component: Info_setting},
    {path: '/login', name: 'Login', component: User,
      children:[
        {path: '', name: 'Login', component: Login}
      ]
    },
    {path: '/register', name: 'Login', component: User,
      children:[
        {path: '', name: 'Register', component: Register}
      ]
    }
  ]
})
