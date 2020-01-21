import numpy as np
import pandas as pd

#导入数据表csv、xlsx等
#dfXlsl=pd.DataFrame(pd.read_excel('data/pay.xlsx'))
dfCsv=pd.DataFrame(pd.read_csv('data/pay.csv',encoding='gbk'))

#控制台打印文件基本信息
print(dfCsv.info())

#按用户统计，并输出统计结果高xls
dfUserSum = dfCsv.groupby('userId')['orderAmount'].agg([len,np.sum, np.mean])
dfUserSum.to_excel('data/payUserSum.xlsx')
