import pandas as pd
import numpy as np
import requests

def GD_Longitude_and_latitude(address):
    location=[]
    city=[]
    for i in address:
        parameters = {'address': i, 'key': '12f8b103e3bcdc6e136203dd45b04829'}
        base = 'http://restapi.amap.com/v3/geocode/geo'
        response = requests.get(base, parameters)
        answer = response.json()
    #     print(i)
        if answer['count'] == '0':
            continue
        city.append(i)
        location.append(answer['geocodes'][0]['location'])
    df=pd.DataFrame({"城市":city,"location":location})
    df['经度']=df['location'].apply(lambda x:str(x).split(',')[0])
    df['纬度']=df['location'].apply(lambda x:str(x).split(',')[1])
    return df[['城市','经度','纬度']]
address=['北京市','天津市','河北省','山西省','内蒙古自治区','常州市','辽宁省','吉林省','黑龙江省','上海市','江苏省','浙江省','安徽省','福建省','江西省','山东省','河南省','湖北省','湖南省','广东省','广西壮族自治区','海南省','重庆市','四川省','贵州省','云南省','西藏自治区','陕西省','甘肃省','青海省','宁夏回族自治区','新疆维吾尔自治区','香港特别行政区','澳门特别行政区']
df=GD_Longitude_and_latitude(address)

