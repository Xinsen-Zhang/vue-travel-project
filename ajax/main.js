var superagent = require('superagent')
var cheerio = require('cheerio')
var requestUrl = 'http://piao.qunar.com/touch'
superagent.get(requestUrl).end((err, res) => {
  if (err) {
    console.log('some thing wrong')
    // return
  } else {
    var $ = cheerio.load(res.text)
    var swipeImgs = $('.swipe-img')
    var swipeItems = []
    var hottestImgs = $('.mp-hotsale-imgcon img')
    var hottestPrice = $('.mp-hotsale-price .mpg-price-num')
    var hottestItems = []
    var recImgs = $('.mp-like-img')
    var recItems = []
    var city = $('.mp-nav-city')[0]['children'][0].data
    swipeImgs.each(function (index, elem) {
      swipeItems.push({
        imgUrl: elem.attribs.src,
        id: index
      })
    })
    hottestImgs.each(function (index, elem) {
      hottestItems.push({
        imgUrl: elem.attribs.src,
        alt: elem.attribs
      })
    })
    hottestPrice.each((index, elem) => {
      console.log(elem)
      hottestItems[index].price = elem['children'][0].data
    })
    recImgs.each(function (index, elem) {
      recItems.push({
        imgUrl: elem.attribs.src,
        alt: elem.attribs.alt
      })
    })
    console.log(city)
  }
})
