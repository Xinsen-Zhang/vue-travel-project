<template>
  <div class="hottest">
    <div class="title">
      <div class="title-left">
        <div class="left-img">
          <img src="http://img1.qunarzz.com/piao/fusion/1711/16/bfbb9874e8f11402.png" alt="">
        </div>
        <div class="left-desc">本周热门榜单</div>
      </div>
      <div class="title-right">
        <span class="right-desc">全部榜单</span>
        <span class="right-icon iconfont">&#xe624;</span>
      </div>
    </div>
    <ul class="content">
      <li class="item" v-for="item in list" :key="item.id">
        <div class="top-img" v-if="item.order && item.order < 4">
          <img :src="topList[item.order - 1]" alt="">
        </div>
        <div class="item-img">
          <img :src="item.imgUrl" :alt="item.desc">
        </div>
        <div class="item-name">{{item.desc}}</div>
        <div class="item-price">
          <span class="price-currency">¥</span>
          <span class="price-num">{{item.price}}</span>
          <span class="price-desc">起</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HomeHottest',
  props: {
    list: Array
  },
  data () {
    return {
      topList: [
        'http://img1.qunarzz.com/piao/fusion/1710/ab/159673b63e6ca702.png',
        'http://img1.qunarzz.com/piao/fusion/1710/2d/36d0c4adaebbbc02.png',
        'http://img1.qunarzz.com/piao/fusion/1710/67/edc47ffef9e96b02.png'
      ]
    }
  }
}
</script>

<style lang="stylus" scoped>
  @import "~styles/variables.styl";

  .hottest
    margin-top .24rem
    background #fff
    .title
      padding .12rem 0
      height .48rem
      .title-left
        float left
        margin-top .1625rem
        .left-img
          margin-left .20rem
          float left
          width .30rem
          height .30rem
          overflow hidden
          img
            width 100%
        .left-desc
          float left
          padding-left .1rem
      .title-right
        float right
        font-size .12rem
        padding-right .44rem
        .right-desc
          color #6161616
    .content
      height 3.4rem
      padding-left .24rem
      overflow-x scroll
      white-space nowrap
      .item
        height 2.8rem
        padding .06rem 0 .2rem
        width 2rem
        margin-right .12rem
        display inline-block
        position relative
        .top-img
          position absolute
          width .84rem
          height .40rem
          left 0
          top -.05rem
          overflow hidden
          border-radius .02rem
          img
            width 100%
        .item-img
          width 2rem
          height 2rem
          img
            width 100%
        .item-name
          margin-top .12rem
          text-align center
          color $darkTextColor
        .item-price
          font-size .24rem
          height .4rem
          line-height .4rem
          color $priceColor
          text-align center
          .price-desc
            color $darkTextColor
</style>
