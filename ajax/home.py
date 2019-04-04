import requests
import re
import json
data = {}
def get_home_data():
    try:
        req = requests.get('http://piao.qunar.com/touch')
        text = req.text
        city = re.findall(r'class="mp-nav-city">(.*?)<', text)[0]
        swipeList = re.findall(r'swipe-img.*?src=\'(.*?)\'', text) 
        iconList = re.findall(r'mp-category-img-container.*?src=\'(.*?)\'.*?alt=\'(.*?)\'', text)
        hottestList = re.findall(r'mp-hotsale-imgcon.*?src=\'(.*?)\'.*?alt=\'(.*?)\'.*?price-num">(.*?)<', text)
        recList = re.findall(r'mp-like-img.*?src=\'(.*?)\'.*?alt=\'(.*?)\'.*?data-score="(.*?)".*?mp-comment-num">(.*?)条.*?price-num">.*?<.*?mp-like-address">(.*?)<', text)
        weekList = re.findall(r'product-imgcontainer.*?src=\'(.*?)\'.*?alt=\'(.*?)\'.*?product-desc">(.*?)<', text)
        data['city'] = city
        temp = []
        for i in range(len(swipeList)):
            temp.append({
                "id": i + 1,
                "imgUrl": swipeList[i]
            })
        data['swipeList'] = temp
        temp = []
        for i in range(len(iconList)):
            temp.append({
                "id": i + 1,
                "imgUrl": iconList[i][0],
                "desc": iconList[i][1]
            })
        data['iconList'] = temp
        temp = []

        for i in range(len(hottestList)):
            temp.append({
                "id": i + 1,
                "imgUrl": hottestList[i][0],
                "desc": hottestList[i][1],
                "price": hottestList[i][2]
            })
            if i < 3:
                temp[-1]['order'] = i + 1
        data['hottestList'] = temp
        temp = []

        for i in range(len(recList)):
            temp.append({
                "id": i + 1,
                "imgUrl": recList[i][0],
                "desc": recList[i][1],
                "score": recList[i][2],
                "commentNum": recList[i][3],
                "address": recList[i][4]
            })
        data['recList'] = temp
        temp = []

        for i in range(len(weekList)):
            temp.append({
                "id": i + 1,
                "imgUrl": weekList[i][0],
                "desc": weekList[i][1],
                "detail": weekList[i][2]
            })
        data['weekList'] = temp
        data['ret'] = True
    except Exception as e:
        data['ret'] = False
    return data

if __name__ == '__main__':
    data = get_home_data()
    pass