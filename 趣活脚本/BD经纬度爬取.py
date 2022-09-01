import requests
import json
import pandas as pd
def BD_Longitude_and_latitude(poi_name):
    lng=[]
    lat=[]
    city=[]
    mykey = 'DdOyOKo0VZBgdDFQnyhINKYDGkzBkuQr'
    # 请求URL
    url = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s'
    for i in poi_name:
        poi_name_info = json.loads(requests.get(url %(i,mykey)).text)
#         print(i)
        city.append(i)
        lng.append(poi_name_info['result']['location']['lng'])
        lat.append(poi_name_info['result']['location']['lat'])
    return pd.DataFrame({"城市":city,"经度":lng,"纬度":lat})
data=['北京市','天津市','河北省','山西省','内蒙古自治区','辽宁省','吉林省','黑龙江省','上海市','江苏省','浙江省','安徽省','福建省','江西省','山东省','河南省','湖北省','湖南省','广东省','广西壮族自治区','海南省','重庆市','四川省','贵州省','云南省','西藏自治区','陕西省','甘肃省','青海省','宁夏回族自治区','新疆维吾尔自治区','香港特别行政区','澳门特别行政区']
df=BD_Longitude_and_latitude(poi_name=data)
print(df)