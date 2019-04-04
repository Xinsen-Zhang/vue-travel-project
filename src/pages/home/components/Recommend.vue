<template>
  <div class="recommend">
    <div class="title">
      <div class="title-img">
        <img src="http://img1.qunarzz.com/piao/fusion/1711/89/ebc329f16c55bb02.png" alt="">
      </div>
      <div class="title-detail">猜你喜欢</div>
    </div>
    <div class="content">
      <div class="item border-bottom" v-for="item in list" :key="item.id">
        <div class="img-left">
          <img :src="item.imgUrl" :alt="item.desc">
        </div>
        <div class="item-detail">
          <div class="item-name">{{item.desc}}</div>
          <div class="item-rate">
            <div class="item-score">{{item.score}}</div>
            <div class="item-comment">{{item.commentNum}}条评论</div>
          </div>
          <div class="item-info">
            <div class="item-price">
              <span>¥</span><strong>{{item.price}}</strong><span class="black-font">起</span>
            </div>
            <div class="item-address">{{item.address}}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="bottom">
      查看所有产品
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeRecommend',
  props: {
    list: Array
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variables.styl'

  .recommend
    margin-top .24rem
    background #fff
    .title
      height .44rem
      .title-img
        display inline-block
        width .30rem
        height .30rem
        margin-left .20rem
        margin-top .07rem
        overflow hidden
        img
          width 100%
      .title-detail
        display inline-block
        font-size .32rem
        height .44rem
        line-height .44rem
    .content
      display block
      .item
        height 2.4rem
        padding .20rem 0 .20rem .24rem
        display flex
        .img-left
          width 2rem
          height 2rem
          margin-top .20rem
          overflow hidden
          img
            width 100%
        .item-detail
          flex 1
          padding-left .22rem
          .item-name
            margin .26rem 0 0
            height .44rem
            line-height .44rem
            font-size .32rem
          .item-rate
            margin .14rem 0 0
            .item-score
              display inline
              color #ffb436
              font-size .28rem
              height .28rem
              line-height .28rem
            .item-comment
              display inline-block
              color #616161
              font-size .24rem
              height .28rem
              line-height .28rem
              margin-left .5rem
          .item-info
            margin .22rem 0 0
            height .46rem
            .item-price
              color $priceColor
              float left
              span
                font-size .24rem
              strong
                font-size .40rem
              .black-font
                color #616161
            .item-address
              float right
              height .40rem
              line-height .40rem
              margin .03rem .5rem 0
              font-size .24rem
              font-size #616161
    .bottom
      text-align center
      height .80rem
      padding .20rem 0
      font-size .28rem
      line-height .80rem
      color #00AFC7
</style>
