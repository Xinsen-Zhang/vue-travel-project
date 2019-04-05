<template>
  <div class="header">
    <router-link to="/">
      <div class="header-back">
        <div class="iconfont back-icon">&#xe624;</div>
      </div>
    </router-link>
    <div class="header-title">城市选择</div>
    <div class="header-tabs-region">
      <ul class="header-tabs">
        <li class="header-tab header-tab-active">境内</li>
        <li class="header-tab">境外`港澳台</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CityHeader'
}
</script>

<style lang="stylus" scope>
@import '~styles/variables.styl'

.header
  background: $bgColor;
  color: #fff;
  position relative
  .header-back
    line-height: 0.88rem
    width: 0.80rem;
    position absolute
    left 0
    top 0
    color: #fff;
    .back-icon
      text-align: center
      font-size: 0.36rem
  .header-title
    line-height: 0.88rem
    width 100%
    color: #fff
    height .88rem
    text-align center
    font-size .32rem
  .header-tabs-region
    padding 0 1.0rem
    height .60rem
    box-sizing border-box
    .header-tabs
      border .01rem solid #fff
      height .40rem
      border-radius .1rem
      .header-tab
        float left
        width 49%
        height .38rem
        line-height .38rem
        text-align center
        background $bgColor
        color #fff
      .header-tab-active
        color $bgColor !important
        background #fff !important
</style>
