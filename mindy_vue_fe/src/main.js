import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/global.css'
import './plugins/element.js'
import Axios from 'axios';//后台交互



Vue.prototype.$http=Axios
//defaults 设置全局默认路径
Axios.defaults.baseURL="http://127.0.0.1:8080/"
Axios.interceptors.request.use(config => {
  console.log(config)
  return config
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
