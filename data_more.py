import json
import map_draw
import data_get

datas = data_get.Get_data()
datas.get_data()
update_time = datas.get_time()
datas.parse_data()
map = map_draw.Draw_map()
with open('data.json','r') as file:
    data = file.read()
    data = json.loads(data)

example_data = {'黑龙江': [127.9688, 45.368], '上海': [121.4648, 31.2891],
             '内蒙古': [110.3467, 41.4899], '吉林': [125.8154, 44.2584],
             '辽宁': [123.1238, 42.1216], '河北': [114.4995, 38.1006],
             '天津': [117.4219, 39.4189], '山西': [112.3352, 37.9413],
             '陕西': [109.1162, 34.2004], '甘肃': [103.5901, 36.3043],
             '宁夏': [106.3586, 38.1775], '青海': [101.4038, 36.8207],
             '新疆': [87.9236, 43.5883], '西藏': [91.11, 29.97],
             '四川': [103.9526, 30.7617], '重庆': [108.384366, 30.439702],
             '山东': [117.1582, 36.8701], '河南': [113.4668, 34.6234],
             '江苏': [118.8062, 31.9208], '安徽': [117.29, 32.0581],
             '湖北': [114.3896, 30.6628], '浙江': [119.5313, 29.8773],
             '福建': [119.4543, 25.9222], '江西': [116.0046, 28.6633],
             '湖南': [113.0823, 28.2568], '贵州': [106.6992, 26.7682],
             '广西': [108.479, 23.1152], '海南': [110.3893, 19.8516],
             '广东': [113.28064, 23.125177], '北京': [116.405289, 39.904987],
             '云南': [102.71225, 25.040609], '香港': [114.165460, 22.275340],
             '澳门': [113.549130, 22.198750], '台湾': [121.5200760, 25.0307240]}

#中国疫情地图数据
def china_map():
    area = []
    confirmed = []
    for each in data:
        area.append(each['area'])
        confirmed.append(each['confirmed'])

    for item in [list(z) for z in zip(area, confirmed)]:
        example_data[item[0]].append((int)(item[1]))
    print(example_data)

    map.to_map_china(area,confirmed,update_time)
    map.to_map_3D_china(example_data,update_time)

# 省份疫情数据
def provinced_map():
    for each in data:
        city = []
        confirmeds = []
        province = each['area']
        for each_city in each['subList']:
            city.append(each_city['city'])
            confirmeds.append(each_city['confirmed'])

china_map()

# https://www.jianshu.com/p/d2474e9bce6e