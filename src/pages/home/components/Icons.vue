<template>
  <div class="icons">
    <swiper :options="swiperOption">
      <swiper-slide v-for="(page, index) of pages" :key="index">
        <div class="icon" v-for="item of page" :key="item.id">
        <!-- <div
          class="icon"
          v-for="item of page"
          :key="item.id"
        > -->
          <div class="icon-img">
            <img class="icon-img-content" :src="item.iconImg" alt="item.iconDesc"/>
          </div>
          <p class="icon-desc">{{item.iconDesc}}</p>
        </div>
      </swiper-slide>
      <div class="swiper-pagination"  slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
export default {
  name: 'HomeIcons',
  data () {
    return {
      swiperOption: {
        // pagination: '.swiper-pagination'
      },
      iconList: [
        {
          id: '001',
          iconImg: 'http://img1.qunarzz.com/piao/fusion/1803/95/f3dd6c383aeb3b02.png',
          iconDesc: '景点门票景点门票景点门票景点门票景点门票景点门票'
        },
        {
          id: '002',
          iconImg: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/f0f00d6dfe038c044dbc9a437f58b0eb.png',
          iconDesc: '北京一日游'
        },
        {
          id: '003',
          iconImg: 'http://img1.qunarzz.com/piao/fusion/1804/ff/fdf170ee89594b02.png',
          iconDesc: '北京必玩'
        },
        {
          id: '004',
          iconImg: 'http://img1.qunarzz.com/piao/fusion/1803/47/c2b659e048b11602.png',
          iconDesc: '遛娃儿'
        },
        {
          id: '005',
          iconImg: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20191/0334cf5430b9b5505fd79e2b8d7e8670.png',
          iconDesc: '爬长城'
        },
        {
          id: '006',
          iconImg: 'http://img1.qunarzz.com/piao/fusion/1803/6c/9e54a8540fee0102.png',
          iconDesc: '故宫'
        },
        {
          id: '007',
          iconImg: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/338c5b924c5809e8c7b14f60a953c3e2.png',
          iconDesc: '北京欢乐谷'
        },
        {
          id: '008',
          iconImg: 'http://mp-piao-admincp.qunarzz.com/mp_piao_admin_mp_piao_admin/admin/20193/6b7127c142123eabcf3e41c136e0ccc2.png',
          iconDesc: '京城赏花'
        },
        {
          id: '009',
          iconImg: 'http://img1.qunarzz.com/piao/fusion/1803/54/35899492b1302802.png',
          iconDesc: '世界公园'
        },
        {
          id: '010',
          iconImg: 'http://img1.qunarzz.com/piao/fusion/1803/76/eb88861d78fb9902.png',
          iconDesc: '动植物园'
        }
      ]
    }
  },
  computed: {
    pages () {
      const pages = []
      this.iconList.forEach((item, index) => {
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
    // overflow: hidden
    // background-color: green
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
