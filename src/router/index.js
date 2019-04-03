import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: resolve => require(['@/pages/home/Home.vue'], resolve)
    },
    {
      path: '/list',
      name: 'List',
      component: resolve => require(['@/pages/list/List.vue'], resolve)
    }
  ]
})
