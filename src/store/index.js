import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

var defaultCity = '杭州'

try {
  defaultCity = localStorage.getItem('currentCity') || defaultCity
} catch (e) {}

var state = {
  showResult: false,
  city: defaultCity
}

var mutations = {
  toggleShowResult (state) {
    state.showResult = !state.showResult
  },
  changeCity (state, city) {
    state.city = city
    try {
      localStorage.setItem('currentCity', city)
    } catch (e) {}
  }
}

export default new Vuex.Store({
  state,
  mutations
})
