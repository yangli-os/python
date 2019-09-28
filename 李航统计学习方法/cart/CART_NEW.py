import pandas as pd
import numpy as np
from collections import Counter
def create_samples():
    #功能函数，读表格的数据转换成list和list标签，最后一列为y
    data=pd.read_excel("data.xlsx")
    feat_list=list(data.columns)              #取第一行为特征标签
    return data,feat_list
def Ginidata(data,feature):
    #数据集切分成[单个特征；y_label格式，返回值为DataFrame格式
    dataSet=data[feature]
    return dataSet
def Gini(data,feat_list,y_label):
    #循环调用GetGini得到基尼指数，并返回list格式的基尼指数表
    all_Gini=[]
    all_data_set = {}
    for feat in range(len(feat_list)-1):        #切分成单个列与标签的形式，以计算Gini指数
        feature=[]
        feature.append(feat_list[feat])         #featture为单列特征的标签，以转到Ginidata中进行列切分
        feature.append(feat_list[-1])           #最后一列为y_label标签
        data_list=Ginidata(data,feature)        #将数据切分成一列特征和一列y_label标签的数据
        GetGini(data_list, y_label)
    #     Gini,data_list_set=GetGini(data_list,y_label)         #根据y_label计算Gini指数,Gini返回值为列表形式
    #     # 注意，字典中key是唯一的，如果特征中有相同的标签，转换成list格式进行处理可以避免key合并
    #     all_Gini.append(Gini)
    #     all_data_set.update(data_list_set)
    # return all_Gini,all_data_set                             #返回值为二维列表[[()],[()]]形式
def GetGini(data_list,y_label):
    #data_list为单列特征和特征和特征对应的标签,y_label为左子树的标签，也就是分类条件
    data_list_set = {}
    feature_label=data_list.columns[0]      #表头
    data_list=np.array(data_list)           #将DataFrame数据转换成array格式方便处理
    data_set=set(data_list[:,0])            #特征的集合
    data_right=data_list[data_list[:, -1]==y_label]    #所有特征中满足y_label条件的特征
    data_label=set(data_list[:, -1])                   #最后一列的所有标签种类
    feature_list,feature_lift,feature_right={},{},{}                     #初始化特征的字典形式，方便计算和存储特征数目#初始化符合条件的特征的字典形式
    for data_li in data_list:
        feature_list[data_li[0]]=feature_list.get(data_li[0],0)+1        #计算每种特征的数目，写成字典形式
    for data_ri in data_right:
        feature_lift[data_ri[0]]=feature_lift.get(data_ri[0],0)+1        #计算每种特征中符合y_label标签的数目，左子树写成字典形式
    for feature in feature_lift:
        feature_right[feature]=feature_list[feature] - feature_lift[feature]     # 计算每种特征中不符合y_label标签的数目，右子树写成字典形式
    print(feature_list,feature_lift,feature_right)
    feat_p={}
    gini={}
    min_gini = {feature_label:{}}
    for feature_p in feature_list :                                          #遍历特征数目的字典
        feat_p[feature_p]=feature_lift[feature_p]/feature_list[feature_p]   #特征中符合y_label条件的概率，对应式中D1的pk
        no_feat_p=(len(data_right)-feature_lift[feature_p])/(len(data_list)-feature_list[feature_p])   #非特征中，符合y_label条件的D2的pk
        #式5.25gini指数全公式，计算基尼指数并保存成字典形式
        gini[feature_p]=(feature_list[feature_p]/len(data_list))*(2*feat_p[feature_p]*(1-feat_p[feature_p]))+((1-(feature_list[feature_p]/len(data_list)))*2*no_feat_p*(1-no_feat_p))
        gini[feature_p]=round(gini[feature_p],2),round(feat_p[feature_p],2)         #将gini指数保留两位小数，记录概率值，概率值为1则为叶节点
        #寻找最优切分点，每个特征中的最优切分点
        print(gini)
    data_list_set[feature_label] = data_set
    print(min_gini)
    min_gini[feature_label]=sorted(gini.items(), key=lambda x: x[1], reverse=False)          #字典根据键值进行内部根据Gini指数从小到大排序，也就找到了内部的最优切分点
    # data_list_set[feature_label]=data_set
    # print(min_gini)
    # return min_gini,data_list_set

def Optimal_cut(all_Gini,feat_list,all_data_set,y_label):
    #划分最优切分点，也就是对比Gini指数的大小
    #计算特征中每一列Gini指数最小的特征和其Gini指数，输出为[(),()]形式的新列表
    optimal={}
    min_gini=1
    #冒泡排序，要加其它规则
    for Gini in range(len(all_Gini)-1):                                      #给含有Gini指数的数据加上表头，并转化成字典形式，防止错乱
        for Gini2 in range(len(all_Gini)-Gini-1):
            # print(list(all_Gini[Gini2].values())[0][0][-1][0])                                                            #取字典的第一个值
            if float(list(all_Gini[Gini2].values())[0][0][-1][0])>float(list(all_Gini[Gini2+1].values())[0][0][-1][0]):     #比较每个字典中的第一个也就是最小的那个的Gini指数
                all_Gini[Gini2+1],all_Gini[Gini2]=all_Gini[Gini2],all_Gini[Gini2+1]                                         #从小到大冒泡排序
            elif float(list(all_Gini[Gini2].values())[0][0][-1][0])==float(list(all_Gini[Gini2+1].values())[0][0][-1][0]):  #如果Gini指数相同，就选择切分点少的那个
                if len(all_Gini[Gini2])>len(all_Gini[Gini2+1]):
                    all_Gini[Gini2+1], all_Gini[Gini2] = all_Gini[Gini2], all_Gini[Gini2+1]
    # print(all_Gini)
    dict_tree={}
    for i in all_Gini:
        cc="".join(i.keys())
        for j in i.values():
            for m in j:
                if (m[-1][-1])==1:
                    dict_tree[cc]=m[0]
                    # dict_tree[cc][m[0]]=y_label
            # print(dict_tree)
    # print(all_Gini)
    # print(data)
    # for op in min_optimal:
    #     dict_tree[op[0]]=all_data_set[op[0]]
    #     # dict_tree[op[0]][y_label] = op[1]
    #     print(dict_tree)


# # 通过判断是否只有同一类样本点（概率是否为1）确定是否是叶子节点，概率为1则为y_label
# if len(all_Gini[Gini]) == 2:
#     for two_gini in all_Gini[Gini]:
#         print(two_gini[-1][-1])
#     print("只有一个最优切分点")
# else:
#     print("最优切分点需要选择")


if __name__ == '__main__':
    data,feat_list=create_samples()             #获取数据集，数据集为DataFrame格式，feat_list为全部标签
    y_label = "agree"  # 分类的左子树为agree
    Gini(data, feat_list, y_label)
    # all_Gini,all_data_set=Gini(data, feat_list,y_label)                       #计算Gini指数，返回值为二维列表[[()],[()]]形式
    # Optimal_cut(all_Gini,feat_list,all_data_set,y_label)