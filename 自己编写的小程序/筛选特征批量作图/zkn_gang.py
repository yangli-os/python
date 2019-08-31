# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib as mpl
def plot_save(Grd,thin,scant,is_mean):
    x_index = []
    y_index = []
    for i in scant:
        x_index.append(i[0])
        y_index.append(i[-1])
    #Grd品牌,thin厚度
    N = len(x_index)  # 柱子总数
    if int(N) >= 10:
        # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
        plt.figure(figsize=(8, 6), dpi=80)
        # 再创建一个规格为 1 x 1 的子图
        plt.subplot(1, 1, 1)
        values = y_index                     # 包含每个柱子对应值的序列
        # 包含每个柱子下标的序列
        index = x_index
        width = 0.35                                          # 柱子的宽度
        p2 = plt.bar(index, values, color="#87CEFA")   # 绘制柱状图, 每根柱子的颜色为紫罗兰色
        for a, b in zip(x_index, y_index):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=12)
        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.xlabel('J40BNNB2/2')                              # 设置横纵轴标签
        plt.ylabel('统计个数',fontsize=20)
        plt.title(str(Grd)+"_"+str(thin),fontsize=25)                 # 添加标题
        plt.xticks(index)     # 添加纵横轴的刻度
        plt.yticks(values)
        # # 添加图例
        plt.legend(["mean: "+str(is_mean)],fontsize=20)               # mean写在这里
        plt.subplots_adjust(wspace=0, hspace=0)  # 调整子图间距
        plt.savefig(str(Grd)+"_"+str(thin)+'.png', format='png')
        plt.cla()
        plt.close("all")
data = pd.read_csv(r"allFMData.csv",encoding="gbk")
# print(data)
lead = data.columns                                                     #表头
# print(lead)
# print(data["Grd"])                                                    #打印一列
Grd_list = set(data['Grd'])
# print(Grd_list)
for Grd in Grd_list:
    est = data.loc[(data['Grd'] == Grd)]                                #钢材种类
    thin_list = set(est['thkTgtFmx'])
    for thin in thin_list:
        thick = est.loc[(est['thkTgtFmx'] == thin)]                     #钢材厚度
        is_mean = round(thick["Time"].mean(),2)
        time_list = thick["Time"]
        key = (Counter(time_list))
        scant = (Counter(key).most_common(9999))
        scant = (sorted(scant))
        plot_save(Grd,thin,scant,is_mean)