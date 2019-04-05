<template>
  <div>
    <city-header></city-header>
    <city-search :alphabetCity="alphabetCity" :hottestCity="hottestCity"></city-search>
    <city-list :alphabet="alphabet" :alphabetCity="alphabetCity" :hottestCity="hottestCity"></city-list>
  </div>
</template>

<script>
import axios from 'axios'

import CityHeader from './components/Header'
import CitySearch from './components/Search'
import CityList from './components/List'

export default {
  name: 'City',
  data () {
    return {
      hottestCity: [],
      alphabet: [],
      alphabetCity: []
    }
  },
  components: {
    CityHeader,
    CitySearch,
    CityList
  },
  methods: {
    handleResponse (response) {
      if (response.data && response.data.ret) {
        var data = response.data
        this.hottestCity = data.hottestCity
        this.alphabet = data.alphabet
        this.alphabetCity = data.alphabat_city
      }
    }
  },
  mounted () {
    axios.get('/api1/city').then(this.handleResponse)
  }
}
</script>

<style lang="stylus" scoped>
</style>
