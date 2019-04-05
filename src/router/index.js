import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: resolve => require(['@/pages/home/Home'], resolve)
    },
    {
      path: '/city',
      name: 'City',
      component: resolve => require(['@/pages/city/City'], resolve)
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
