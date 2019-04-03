<template>
  <div class="wrapper">
    <swiper :options="swiperOption">
      <!-- slides -->
      <swiper-slide v-for="item of imgList" :key="item.id">
        <img :src="item.imgUrl" :alt="item.alt" class="swiper-img">
      </swiper-slide>
      <!-- Optional controls -->
      <div class="swiper-pagination"  slot="pagination"></div>
      <!-- 不需要箭头 -->
      <!-- <div class="swiper-button-prev" slot="button-prev"></div> -->
      <!-- <div class="swiper-button-next" slot="button-next"></div> -->
      <!-- <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
    </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeSwiper',
  data () {
    return {
      swiperOption: {
        pagination: '.swiper-pagination',
        loop: true
      },
      imgList: [
        {
          id: '001',
          imgUrl: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20194/cd159d07551d6506de88e0e2b04047ce.jpg_750x200_8a1f27c0.jpg',
          alt: '1号轮播图'
        },
        {
          id: '002',
          imgUrl: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/6b6fd3d9e40b749ac1d189ce80ebb3cc.jpg_750x200_9616e2e7.jpg',
          alt: '2号轮播图'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
// 样式穿透
  .wrapper >>> .swiper-pagination-bullet-active
    background #fff
  .wrapper
    width: 100%
    overflow: hidden
    height: 0
    padding-bottom: 25%
    background-color #eee
    .swiper-img
      width: 100%
</style>
