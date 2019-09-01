import pandas as pd
import numpy as np
import csv
data = pd.read_csv(r"allFMData(1)(1)+-+副本.csv",encoding="gbk")
col = data['Time'].str.isdigit()            #如果字符串只包含数字则返回 True 否则返回 False
cleaned = data[col].copy()
print(cleaned)
cleaned.to_csv("allFMData.csv")
