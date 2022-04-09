import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Home from '../components/Home.vue'
import route from 'uview-ui/libs/util/route'

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
    path:'/',
    redirect:'/login' 
  },
  {
    path:'/home',
    component: Home,
    name: 'Home'
  }

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
