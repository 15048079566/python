import pandas as pd
import os
dfs=pd.DataFrame()
#os.walk(file_path) 深度遍历file_path下的所有子文件夹及文件
i=0
for root_dir,sub_dir,files in os.walk(r"/Users/admin/Desktop/jupyter/分析报告/骑手分析报告/骑手分析报告/202207/salary-202207-elem"):
    for file in files:
        if file.endswith(".xlsx") & file.startswith("一"):  # file.endswith结束  file.startswith开始 &'value' in file关键字
            #构造绝对路径
            file_name = os.path.join(root_dir, file)
            #读取sheet页
            #pd.read_excel(file_path,sheet_name=None).keys()获取excel表格所有的sheet页名称
            for sheet in pd.read_excel(file_name,sheet_name=None).keys():
                i+=1
                print("已读取"+file_name)
                df=pd.read_excel(file_name,sheet_name=sheet)
                excel_name=file.replace(".xlsx","")
                #新增两列用于记录数据所属excel及sheet页
                df["excel_name"]=excel_name
                df["sheet_name"]=sheet
                dfs=pd.concat([dfs,df])
print('共{}个文件'.format(i))