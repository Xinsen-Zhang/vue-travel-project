<template>
  <div class="list">
    <div class="current-city">
      <h2 class="title ">当前城市</h2>
      <div class="content">
        <div class="area border-rightbottom">北京</div>
      </div>
      </div>
    <div class="hottest">
      <h2 class="title ">热门城市</h2>
      <div class="content">
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>
        <div class="area border-rightbottom">北京</div>

      </div>
      </div>
    <div class="alphabet-list">
      <h2 class="title ">字母排序</h2>
      <div class="content"></div>
      </div>
    <div class="alphabet">
      <h2 class="title ">A</h2>
      <div class="content"></div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'CityList'
}
</script>

<style lang="stylus" scope>
  @import '~styles/variables.styl'

  .list
    background rgb(245, 245, 245)
    position absolute
    top 2.36rem
    left 0
    right 0
    bottom 0
    .title
      margin .24rem .30rem
    .content
      overflow hidden
      background #fff
      .area
        float left
        width 25%
        text-align center
        height .90rem
        line-height .90rem
        color #212121
</style>
