import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Home from '../components/Home.vue'
import route from 'uview-ui/libs/util/route'
import Welcome from '../components/Welcome.vue'
import Userinfo from '../components/Userinfo.vue'
import Admin from '../components/Admin.vue'
import Userslist from '../components/user/Userslist.vue'
import Email_verify from '../components/Email_verify.vue'
import Mindmap from '../components/Mindmap.vue'
import Sharedfile from '../components/Sharedfile.vue'
import File from '../components/File.vue'
import Bin from '../components/Bin.vue'
import Mindmaplist from '../components/user/Mindmaplist.vue'
import Butterfly from '../components/Butterfly.vue'
import Adminhome from '../components/Adminhome.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
  {
    path:'/login',
    component: Login,
    name: 'Login'
  },
  {
    path:'/register',
    component: Register,
    name: 'Register'
  },
  {
    path:'/emailverify',
    component: Email_verify,
    name: 'Email_verify'
  },
  {
    path:'/',
    redirect:'/login' 
  },
  {
    path:'/admin',
    component: Admin,
    name: 'Admin',
    children:[{
      path:'/userslist',
      component: Userslist
    },{
      path:'/mindmaplist',
      component: Mindmaplist
    },
    {
      path:'/admininfo',
      component: Userinfo
    },
    {
      path:'/adminhome',
      component: Adminhome
    },]
  },
  {
    path:'/home',
    component: Home,
    name: 'Home',
    redirect:'/welcome',
    children:[{
      path:'/welcome',
      component: Welcome
    },
    {
      path:'/userinfo',
      component: Userinfo
    },{
      path:'/mindmap',
      component: Mindmap
    },
    {
      path:'/butterfly',
      component: Butterfly,
    },{
      path:'/file',
      component: File
    },{
      path:'/sharedfile',
      component: Sharedfile,
    },
    {
      path:'/bin',
      component: Bin,
    },]
  },  
  // {
  //   path:'/mindmap',
  //   component: Mindmap,
  //   name: 'Mindmap'
  // },

]

const router = new VueRouter({
  routes
})

// router.beforeEach((to,from,next)=>{
//   if(to.path==='/login'){
//     return next()
//     //token
//   }
//   const tokenStr = window.sessionStorage.getItem('token')
//     if(!tokenStr){
//       return next('/login')
//     } 
//     next()
// })

export default router
