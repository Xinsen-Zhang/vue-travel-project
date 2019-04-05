<template>
  <div class="alphabet" v-show="showAlphabet" @touchstart="touchstartHandler" @touchend="touchendHandler" @touchmove="touchmoveHandler">
    <div class="alphabet-item" v-for="(item, index) in alphabet" :key="index" @click="clickHandler(item)">{{item}}</div>
  </div>
</template>

<script>
import { setTimeout, clearTimeout } from 'timers'

export default {
  name: 'CityAlphabet',
  props: {
    alphabet: Array
  },
  data () {
    return {
      isTouched: false,
      initY: 0,
      timer: null
    }
  },
  computed: {
    showAlphabet () {
      return !this.$store.state.showResult
    }
  },
  methods: {
    clickHandler (alphabet) {
      // alert(alphabet)
      this.$emit('change', alphabet)
    },
    touchstartHandler (event) {
      this.isTouched = true
      // console.log('start')
    },
    touchendHandler (event) {
      this.isTouched = false
    },
    touchmoveHandler (event) {
      if (this.timer) {
        clearTimeout(this.timer)
      }
      if (this.isTouched) {
        this.timer = setTimeout(() => {
          try {
            var targetY = event.targetTouches[0].clientY
            var diffY = targetY - this.initY
            var index = Math.floor(diffY / 22)
            this.$emit('change', this.alphabet[index])
          } catch (e) {}
        }, 100)
      }
    }
  },
  mounted () {
    setTimeout(() => {
      this.initY = document.getElementsByClassName('alphabet-item')[0].offsetTop
    }, 500)
  }
}
</script>

<style lang="stylus" scope>
  @import '~styles/variables.styl';

  .alphabet
    position absolute
    right 0
    top 0rem
    bottom 0
    display flex
    flex-direction column
    justify-content center
    .alphabet-item
      color $bgColor
      font-size .36rem
      height .44rem
      line-height .44rem
      text-align center
      width .60rem
</style>
