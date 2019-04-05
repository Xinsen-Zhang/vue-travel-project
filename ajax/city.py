import requests
import re
from bs4 import BeautifulSoup
import pypinyin

def get_city():
    try:
        url = 'http://piao.qunar.com/touch/toNewCityList.htm'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, features="lxml")
        hottestCity_ = [a.text for a in soup.select('#city-domestic .mp-tr3 a')]
        hottestCity = []
        for city in hottestCity_:
            py = pypinyin.pinyin(city, style=pypinyin.NORMAL)
            py = [p[0] for p in py]
            py = ''.join(py)
            hottestCity.append({
                'city': city,
                'pinyin': py
            })
        alphabet = [a.text for a in soup.select('#city-domestic .mp-tr6 a')]
        alpha = soup.select('#city-domestic h2')[2:]
        alpha_city = soup.select('#city-domestic .mp-list')[1:]
        alpha = [h.text for h in alpha]
        alpha_city = [re.findall(r'<a.*?>(.*?)</a>', str(city)) for city in alpha_city]
        data = {}
        data['hottestCity'] = hottestCity
        data['alphabet'] = alphabet
        temp = []
        for i in range(len(alpha)):
            pinyin_ = alpha_city[i]
            pinyin = []
            for py in pinyin_:
                py = pypinyin.pinyin(py, style=pypinyin.NORMAL)
                py = [p[0] for p in py]
                py = ''.join(py)
                pinyin.append(py)

            temp.append({
                'alphabet': alpha[i],
                'city': alpha_city[i],
                'pinyin': pinyin
            })
        data['alphabat_city'] = temp
        data['ret'] = True
        return data
    except Exception as e:
        return {'ret': False}

if __name__ == '__main__':
    city = get_city()
    for k,v in city.items():
        print(k)
        print(v)
        print('-' * 10)
