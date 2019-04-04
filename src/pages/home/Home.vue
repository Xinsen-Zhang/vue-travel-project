<template>
  <div class="home">
    <home-header :city="city"></home-header>
    <home-swiper :list="swipeList"></home-swiper>
    <home-icons :list="iconList"></home-icons>
    <home-hottest :list="hottestList"></home-hottest>
    <home-recommend></home-recommend>
  </div>
</template>

<script>
import axios from 'axios'

import HomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeIcons from './components/Icons'
import HomeHottest from './components/Hottest'
import HomeRecommend from './components/Recommend.vue'
export default {
  name: 'Home',
  data () {
    return {
      city: '',
      swipeList: [],
      iconList: [],
      hottestList: []
    }
  },
  components: {
    HomeHeader,
    HomeSwiper,
    HomeIcons,
    HomeHottest,
    HomeRecommend
  },
  mounted () {
    this.getHomeData()
  },
  methods: {
    handleResponse (res) {
      var data = res.data
      this.city = data.city
      this.swipeList = data.swipeList
      this.iconList = data.iconList
      this.hottestList = data.hottestList
    },
    getHomeData () {
      axios.get('/api1/home').then(this.handleResponse)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .home
    background #eee
</style>
