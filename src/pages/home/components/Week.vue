<template>
  <div class="week">
    <div class="title">
      <div class="title-detail">周末去哪儿</div>
    </div>
    <div class="content">
      <div class="item" v-for="item in list" :key="item.id">
        <div class="item-img">
          <img :src="item.imgUrl" :alt="item.desc">
        </div>
        <div class="item-info">
          <div class="item-name">{{item.desc}}</div>
          <div class="item-desc">{{item.detail}}</div>
        </div>
      </div>
    </div>
    <!-- <div class="bottom">
      查看所有产品
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'HomeWeek',
  props: {
    list: Array
  }
}
</script>

<style lang="stylus" scoped>
  @import '~styles/variables.styl'

  .title
    height .80rem
    font-size .28rem
    line-height .80rem
    padding 0 0 0 .26rem
    color #212121
  .content
    display block
    .item
      background #fff
    .item-img
      height 0
      padding-bottom 38.9%
      overflow hidden
      img
        width 100%
    .item-info
      padding .14rem .20rem .20rem
      height 1.24rem
      .item-name
        font-size .28rem
        height .48rem
        line-height .48rem
        padding 0 1.40rem 0 0
        color #212121
      .item-desc
        height .42rem
        color #616161
        font-size .24rem
        padding 0 1.40rem 0 0
</style>
