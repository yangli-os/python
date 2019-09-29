import pandas as pd
source = "/home/liyang/Speech_synthesis/测试数据.xlsx"
data = pd.read_excel(source)
df = data.groupby(["企业名称","班次名称整理"])["服务公里数"].apply(lambda x:x.median())
df2 = data.groupby(["企业名称","班次名称整理"])["服务公里数"].median()
# out = pd.merge(df,df2,left_on=["企业名称","班次名称整理"],right_index=True,how="outer")
print(df)