<template>
  <div class="icons">
    <swiper :options="swiperOption">
      <swiper-slide v-for="(page, index) of pages" :key="index">
        <div class="icon" v-for="item of page" :key="item.id">
          <div class="icon-img">
            <img class="icon-img-content" :src="item.imgUrl" alt="item.desc"/>
          </div>
          <p class="icon-desc">{{item.desc}}</p>
        </div>
      </swiper-slide>
      <div class="swiper-pagination"  slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeIcons',
  props: {
    list: Array
  },
  data () {
    return {
      swiperOption: {
        pagination: '.swiper-pagination'
      }
    }
  },
  computed: {
    pages () {
      const pages = []
      this.list.forEach((item, index) => {
        let page = Math.floor(index / 8)
        if (pages[page] === undefined) {
          pages[page] = []
        }
        pages[page].push(item)
      })
      return pages
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variables.styl'
  @import '~styles/mixins.styl'

  .icons >>> .swiper-wrapper
    width: 100%
    height: 0
    padding-bottom: 50%
    margin-bottom .5rem
    // overflow: hidden
    // background-color: green
  .icons >>> .swiper-pagination-bullet-active
    background rgba(0,175,190,.8) !important
  .icons
    background #fff
    .icon
      width: 25%
      float: left
      height: 0
      padding-bottom: 25%
      // background-color: #f00
      position relative
      .icon-img
        position absolute
        top 0
        left 0
        right 0
        bottom .44rem
        // background-color blue
        box-sizing border-box
        padding .1rem
        .icon-img-content
          display block
          margin 0 auto
          height 100%
      .icon-desc
        position absolute
        bottom 0
        right 0
        left 0
        height .44rem
        line-height .44rem
        color $darkTextColor
        text-align center
        ellipsis()
</style>
