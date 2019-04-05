<template>
  <div class="list" v-show="showList">
    <div class="current-city">
      <h2 class="title ">当前城市</h2>
      <div class="content">
        <div class="area border-rightbottom">{{currentCity}}</div>
      </div>
      </div>
    <div class="hottest">
      <h2 class="title ">热门城市</h2>
      <div class="content">
        <div class="area border-rightbottom" v-for="(item, index) in hottestCity" :key="index" @click="clickHandler">{{item.city}}</div>
      </div>
    </div>
    <div class="alphabet-list">
      <h2 class="title ">字母排序</h2>
      <div class="content">
        <div class="area border-rightbottom" v-for="(item, index) in alphabet" :key="index">{{item}}</div>
      </div>
    </div>
    <div class="alphabet-city" v-for="(item, index) in alphabetCity" :key="index">
      <h2 class="title ">{{item.alphabet}}</h2>
      <div class="content">
        <div class="area border-rightbottom" v-for="(city, index) in item.city" :key="index" @click="clickHandler">{{city}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CityList',
  props: {
    alphabet: Array,
    hottestCity: Array,
    alphabetCity: Array
  },
  methods: {
    changeCity (city) {
      this.$store.commit('changeCity', city)
      this.$router.push('/')
    },
    clickHandler (event) {
      let city = event.target.innerText
      this.changeCity(city)
    }
  },
  computed: {
    showList () {
      return !this.$store.state.showResult
    },
    currentCity () {
      return this.$store.state.city
    }
  }
}
</script>

<style lang="stylus" scope>
  @import '~styles/variables.styl'
  @import '~styles/mixins.styl'

  .list
    background rgb(245, 245, 245)
    position absolute
    top 1.56rem
    left 0
    right 0
    bottom 0
    .title
      padding .24rem .30rem
      background rgb(245, 245, 245)
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
        ellipsis()
</style>
