<template>
  <div class="list wrapper" v-show="showList" ref="wrapper">
    <div class="list-content">
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
          <div class="area border-rightbottom" v-for="(item, index) in alphabet" :key="index" @click="handler">{{item}}</div>
        </div>
      </div>
      <div class="alphabet-city" v-for="(item, index) in alphabetCity" :key="index">
        <h2 class="title" :id="getId(item.alphabet)">{{item.alphabet}}</h2>
        <div class="content">
          <div class="area border-rightbottom" v-for="(city, index) in item.city" :key="index" @click="clickHandler">{{city}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BScroll from 'better-scroll'

export default {
  name: 'CityList',
  props: {
    alphabet: Array,
    hottestCity: Array,
    alphabetCity: Array,
    scrollY: Number
  },
  methods: {
    changeCity (city) {
      this.$store.commit('changeCity', city)
      this.$store.commit('closeResult')
      this.$router.push('/')
    },
    clickHandler (event) {
      let city = event.target.innerText
      this.changeCity(city)
    },
    getId (alphabet) {
      return 'domestic-' + alphabet
    },
    scrollToHandler (y) {
      this.scroll.scrollTo(0, -y)
    },
    handler (event) {
      var alpha = event.target.innerText
      this.$emit('change', alpha)
    }
  },
  computed: {
    showList () {
      return !this.$store.state.showResult
    },
    currentCity () {
      return this.$store.state.city
    }
  },
  watch: {
    scrollY: function (newVal) {
      this.scrollToHandler(newVal)
    }
  },
  mounted () {
    this.scroll = new BScroll(this.$refs.wrapper, {
      momentum: true
    })
    this.scrollToHandler(this.scrollY)
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
    overflow hidden
    .title
      padding .24rem .30rem
      background rgb(245, 245, 245)
    .content
      overflow hidden
      background #fff
      padding  0 .60rem 0 0
      .area
        float left
        width 25%
        text-align center
        height .90rem
        line-height .90rem
        color #212121
        ellipsis()
</style>
