##  后端压缩包文件concat   获取压缩包路径
from dask import dataframe as dd
import os
import pandas as pd

def to_excel(input_path,out_path):
    for root, dirs, files in os.walk(input_path):  # 遍历统计
        print(root)
        report_result = dd.read_parquet(root, index=False)
        result = report_result.compute()

    result.to_excel(out_path)


if __name__ == "__main__":
    input_path='/Users/admin/Desktop/报告数据/tmp/mt_worker_order_common_kpi_by_monthly_t2'
    out_path='/Users/admin/Desktop/jupyter/邮件发送/202207月/mt_worker_order_common_kpi_by_monthly_t2.xlsx'
    to_excel(input_path,out_path)

# input_path='/Users/admin/Desktop/tmp/ele_day_middle_table'
# out_path='/Users/admin/Desktop/tmp/ele_day_middle_table.xlsx'
# for root, dirs, files in os.walk(input_path):  # 遍历统计
#     print(root)
#     report_result = dd.read_parquet(root, index=False)
#     result = report_result.compute()

# result.to_excel(out_path)
