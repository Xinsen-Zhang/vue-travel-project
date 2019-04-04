<template>
  <div>
    <div class="hottest">
      <div class="hottest-title">
        <div class="hottest-title-left">
          <div class="hottest-title-img">
            <img src="http://img1.qunarzz.com/piao/fusion/1711/16/bfbb9874e8f11402.png" alt="" />
          </div>
          <span class="hottest-title-left-desc">本周热门榜单</span>
        </div>
        <div class="hottest-title-right">
          <div class="hottest-title-right-desc">全部榜单</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style lang="stylus" scoped>
  @import '~styles/variables.styl'
  .hottest
    margin-top 0.75rem
    height 12.5rem
    background #fff
    .hottest-title
      height 3rem
      box-sizing border-box
      padding  0.9rem
      .hottest-title-left
        float left
        width 10rem
        .hottest-title-img
          height 1.2rem
          display inline-block
          img
            height 100%
        .hottest-title-left-desc
          line-height 1.2rem
          height 1.2rem
          padding-left .5rem
          color $darkTextColor
      .hottest-title-right
        float right
</style>
