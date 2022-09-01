import pandas as pd
def li_(index_name,data):
    data_new = pd.DataFrame()
    data_columns=[]
    columns_new = []
    for i in data.columns:
        if i not in index_name:
            data_columns.append(i)
    for i in data_columns:
        index_name.append(i)
        df = data[index_name].copy()
        index_name[:]=index_name[:-1]
        df['datetime']=i
        df.rename(columns={i:'value'},inplace=True)
        data_new = pd.concat([data_new, df])
    for i in data_new.columns:
        if i !='value':
            columns_new.append(i)
    columns_new.append('value')
    return data_new[columns_new]
index_name=['code','name']
data=pd.read_excel('/Users/admin/Desktop/副本测试111.xlsx',parse_dates=True)
data=li_(index_name=index_name,data=data)
print(data)