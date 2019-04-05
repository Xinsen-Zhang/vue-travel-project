<template>
  <div class="search">
    <div class="search-input">
    <input type="text" placeholder="输入城市/拼音">
    </div>
  </div>
</template>

<script>
export default {
  name: 'CitySearch'
}
</script>

<style lang="stylus" scope>
@import '~styles/variables.styl'

.search
  background: $bgColor
  width: 100%
  position: relative
  height  .68rem
  .search-input
    position: absolute
    left 0
    right 0
    height .68rem
    width 100%
    box-sizing border-box
    padding .10rem .80rem
    background-color $bgColor
    color #666
    input
      background #fff
      width 100%
      text-align center
      box-sizing border-box
      padding 0 0.2rem
</style>
