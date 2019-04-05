<template>
  <div class='search'>
    <div class='search-input'>
      <input type='text' placeholder='输入城市/拼音' v-model='kw'>
    </div>
    <div class="search-content wrapper" v-show="showResult" ref="searchWrapper">
      <div class="search-item border-bottom" v-for="(item, index) in result" :key="index" @click="clickHandler">{{item.city}}</div>
      <div class="search-item border-bottom" v-if="hasNoData">没有匹配的城市</div>
    </div>
  </div>
</template>

<script>
import { clearTimeout, setTimeout } from 'timers'
import BScroll from 'better-scroll'

export default {
  name: 'CitySearch',
  props: {
    hottestCity: Array,
    alphabetCity: Array
  },
  data () {
    return {
      kw: '',
      timer: null,
      result: []
    }
  },
  watch: {
    kw: function (newVal) {
      var result = []
      if (!newVal) {
        this.result = result
        return
      }
      if (this.timer) {
        clearTimeout(this.timer)
      }
      this.timer = setTimeout(() => {
        for (let i = 0; i < this.alphabetCity.length; i++) {
          let cities = this.alphabetCity[i]
          for (let j = 0; j < cities['city'].length; j++) {
            if (cities['city'][j].indexOf(newVal) > -1) {
              result.push({
                city: cities['city'][j],
                pinyin: cities['pinyin'][j]
              })
            }
            if (cities['pinyin'][j].indexOf(newVal) > -1) {
              result.push({
                city: cities['city'][j],
                pinyin: cities['pinyin'][j]
              })
            }
          }
        }
        this.result = result
      }, 100)
    },
    showResult: function (newVal) {
      if (newVal) {
        this.$store.commit('openResult')
      } else {
        this.$store.commit('closeResult')
      }
    }
  },
  computed: {
    showResult () {
      return this.kw.length > 0
    },
    hasNoData () {
      return this.result.length === 0
    }
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
    }
  },
  mounted () {
    this.searchScroll = new BScroll(this.$refs.searchWrapper, {
      momentum: true
    })
  }
}
</script>

<style lang='stylus' scope>
@import '~styles/variables.styl'

.search
  background: $bgColor
  width: 100%
  position: relative
  height: 0.68rem
  .search-input
    position: absolute
    left: 0
    right: 0
    height: 0.68rem
    width: 100%
    box-sizing: border-box
    padding: 0.1rem 0.8rem
    background-color: $bgColor
    color: #666
    input
      background: #fff
      width: 100%
      text-align: center
      box-sizing: border-box
      padding: 0 0.2rem
  .search-content
    position absolute
    left 0
    right 0
    top .68rem
    z-index 1
    .search-item
      background rgb(245, 245, 245)
      height .60rem
      line-height .60rem
      font-size .28rem
      text-align center
</style>
