<template>
  <div>
    <city-header></city-header>
    <city-search :alphabetCity="alphabetCity"></city-search>
    <city-list :alphabet="alphabet" :alphabetCity="alphabetCity" :hottestCity="hottestCity" :scrollY="scrollY" @change="changeHandler"></city-list>
    <city-alphabet :alphabet="alphabet" @change="changeHandler"></city-alphabet>
  </div>
</template>

<script>
import axios from 'axios'

import CityHeader from './components/Header'
import CitySearch from './components/Search'
import CityList from './components/List'
import CityAlphabet from './components/Alphabet'

export default {
  name: 'City',
  data () {
    return {
      hottestCity: [],
      alphabet: [],
      alphabetCity: [],
      scrollY: 0
    }
  },
  components: {
    CityHeader,
    CitySearch,
    CityList,
    CityAlphabet
  },
  methods: {
    handleResponse (response) {
      if (response.data && response.data.ret) {
        var data = response.data
        this.hottestCity = data.hottestCity
        this.alphabet = data.alphabet
        this.alphabetCity = data.alphabat_city
      }
    },
    changeHandler (alphabet) {
      var y = document.getElementById('domestic-' + alphabet).offsetTop
      // this.$emit('scrollTo', y)
      this.scrollY = y
    }
  },
  mounted () {
    axios.get('/api1/city').then(this.handleResponse)
  }
}
</script>

<style lang="stylus" scoped>
</style>
