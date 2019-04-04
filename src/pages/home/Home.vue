<template>
  <div class="home">
    <home-header></home-header>
    <home-swiper></home-swiper>
    <home-icons></home-icons>
    <home-hottest></home-hottest>
    <home-recommend></home-recommend>
  </div>
</template>

<script>
import HomeHeader from './components/Header'
import HomeSwiper from './components/Swiper'
import HomeIcons from './components/Icons'
import HomeHottest from './components/Hottest'
import HomeRecommend from './components/Recommend.vue'
export default {
  name: 'Home',
  components: {
    HomeHeader,
    HomeSwiper,
    HomeIcons,
    HomeHottest,
    HomeRecommend
  }
}
</script>

<style lang="stylus" scoped>
  .home
    background #eee
</style>
