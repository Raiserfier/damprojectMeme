import Vue from 'vue'
import Router from 'vue-router'

import Home from '../components/Home'
import Home1 from "../components/Home1";
import Channel from '../components/Channel'
 //import ImageStream from '../components/ImagePage/ImageStream'
import Upload from '../components/Upload'
import User from '../components/User'
import Login from '../components/User/Login'
import Title from '../components/Title'
import Register from '../components/User/Register'
// import Favorite from '../components/Favorite'

Vue.use(Router)

export default new Router({
  routes: [
    // home-page
    {path: '/', name: 'Home', component: Home},
    {path: '/1', name: 'Home', component: Home1},
    {path: '/:type/:key', name: 'PageWithTitle', component: Title},
    {path: '/:type/:id/:key', name: 'PageWithSearch', component: Channel},
    // {path:'/animal', name:'Animal',components:Upload},
    // // class-page
    // {path:'/animal', name:'Animal',component:Animal},
    // {path:'/anime', name:'Anime', component:Anime},
    // {path:'/food', name:'Food', component:Food},
    // {path:'/game', name:'Game', component:Game},
    // {path:'/people', name:'People', component:People},
    // {path:'/animal', name:'Animal',components:{Nav, Title, ImageStream}},
    // {path:'/anime', name:'Anime', components:{Nav, Title, ImageStream}},
    // {path:'/food', name:'Food', components:{Nav, Title, ImageStream}},
    // {path:'/game', name:'Game', components:{Nav, Title, ImageStream}},
    // {path:'/people', name:'People', component:{Nav, Title, ImageStream}},
    // upload-page
    {path: '/upload', name: 'Upload', component: Upload},
    // // search-page
     //{path:'/search', name:'Search', component: {Nav, Title, ImageStream}},
    // user-page
    // {path: '/channel/user-id', name: 'Channel', component: Channel},
    // favorite-page
    // {path: '/favorite', name: 'Favorite', component: Favorite},
    // {path: '/favorite', name:'Favorite', component: ImageStream},
    // login-page
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
