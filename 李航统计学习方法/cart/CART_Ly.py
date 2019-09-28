# -*- coding: utf-8 -*-
"""
@author: 蔚蓝的天空Tom
Aim:给定样本集和特征列表，计算每个特征的基尼指数，选取最优特征，选取最优分切点
Aim:生成CART决策树的字典形式
Aim:根据决策树字典绘制CART决策树图形
cart_dtree.py
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter


def print_dict(src_dict, level, src_dict_namestr=''):
    '''
    逐行打印dict
    :param self:类实例自身
    :param src_dict:被打印的dict
    :param level:递归level，初次调用为level=0
    :param src_dict_namestr:对象变量名称字符串
    '''
    if isinstance(src_dict, dict):  # if src_dict的类型是dict字典
        tab_str = '\t'
        for i in range(level):
            tab_str += '\t'
        if 0 == level:
            print(src_dict_namestr, '= {')
        for key, value in src_dict.items():
            if isinstance(value, dict):
                has_dict = False
                for k, v in value.items():
                    if isinstance(v, dict):
                        has_dict = True
                if has_dict:
                    print(tab_str, key, ":{")
                    print_dict(value, level + 1)
                else:
                    print(tab_str, key, ':', value)
            else:
                print(tab_str, key, ': ', value, )
        print(tab_str, '}')


'''
裁剪规格简介
#每个样本example的特征列表
feature_type_list = ['youth','work','hourse','credit']
即每个样本=[age_value, work_value, housr_value, crdit_value, class_label]
如下一个样本集：
samples_list = [ ['youth', 'work_no', 'house_no', '1', 'refuse']
                 ['youth', 'work_no', 'house_no', '2', 'refuse']
                 ['youth', 'work_yes', 'house_no', '2', 'agree']
                 ['youth', 'work_yes', 'house_yes', '1', 'agree']
                 ['youth', 'work_no', 'house_no', '1', 'refuse']
                 ['mid', 'work_no', 'house_no', '1', 'refuse']
                 ['mid', 'work_no', 'house_no', '2', 'refuse']
                 ['mid', 'work_yes', 'house_yes', '2', 'agree']
                 ['mid', 'work_no', 'house_yes', '3', 'agree']
                 ['mid', 'work_no', 'house_yes', '3', 'agree']
                 ['elder', 'work_no', 'house_yes', '3', 'agree']
                 ['elder', 'work_no', 'house_yes', '2', 'agree']
                 ['elder', 'work_yes', 'house_no', '2', 'agree']
                 ['elder', 'work_yes', 'house_no', '3', 'agree']
                 ['elder', 'work_no', 'house_no', '1', 'refuse'] ]
假设已经通过信息增益选出此样本集的决策树的最优根节点为特征housre
如果想求子决策树的最优根节点的话，就需要对原始样本集进行裁剪了，然后用新的样本集筛选新的最优根节点
#通过如下规则得到新的样本集
step1:删除hourse特征值为house_yes所在的所有行
step2:然后再删除hourse特征值列
'''


class CTailorSamples(object):
    '''裁剪样本集'''

    def __init__(self, data_list, feat_type_list, feat_type_index, feat_value):
        self.data_list = data_list
        self.feat_type_list = feat_type_list
        self.feat_type_index_tailed = feat_type_index
        self.feat_value_tailed = feat_value
        self.tailer_work()  # 裁剪

    def get_samples(self):
        '''
        返回裁剪后的样本集，特征类型列表
        '''
        return self.data_list, self.feat_type_list

    def get_all_indexs(self, src_list, dst_value):
        '''
        返回给定值的所有元素的下标
        src_list = [10,20,30,30,30,50]
        e = 30
        indexs_list = tailor.get_all_indexs(src_list, e)
        print(indexs_list) #[2, 3, 4]
        '''
        dst_val_index = [i for i, x in enumerate(src_list) if x == dst_value]
        return dst_val_index

    def tailer_work(self):
        '''裁剪得到新的特征列表'''
        del self.feat_type_list[self.feat_type_index_tailed]

        '''裁剪数据集'''
        # 摘取被删除的特征列
        colum_to_del = self.feat_type_index_tailed
        self.feat_value_list = [example[colum_to_del] for example in self.data_list]
        # 找出含有self.feat_value_tailed特征值的所有样本所在行的下标
        rows_to_del = self.get_all_indexs(self.feat_value_list, self.feat_value_tailed)

        # 删除row_index_list中行下标对应的self.src_data_list的行
        # 技巧：从大的行下标开始依次删除
        # for row in list(reversed(rows_to_del)):
        # for row in rows_to_del[::-1]:
        rows_to_del.reverse()
        for row in rows_to_del:
            del self.data_list[row]

        # 删除给定的特征列
        for row in range(len(self.data_list)):
            del self.data_list[row][colum_to_del]

        return self.data_list, self.feat_type_list


class CCartTree(object):
    def __init__(self, samples, feat_list, div_label, max_n_feats):
        self.samples = samples  # 特征空间
        self.feat_list = feat_list  # 特征标签
        self.div_label = div_label  # 划分条件
        self.max_n_feats = max_n_feats  # 树最大深度
        self.tree_dict = {}  # 字典树
        self.create_tree()  # 创建字典树

    def get_tree_dict(self):
        return self.tree_dict

    def work(self, samples, feat_list, div_label, max_n_feats):
        '''
        给定样本数据集+特征列表，找出最优特征，最优切分点，最优叶节点，次优切分点
        samples:样本数据集
        feat_list:特征列表, 比如['age','work','house','credit']
        return 样本集的最优特征，最优切分点最优叶节点
        Note,每个样本=[ageVal, workVal, houseVal, creditVal, classLabel]
        '''
        stat, n_samples = {}, len(samples)
        class_vals = [e[-1] for e in samples]  # 获取samples的最后一列作为输出
        #        print(class_vals)
        class_set = set(class_vals)  # 特征refuse或者agree
        for i in range(len(feat_list)):
            f, stat[f] = feat_list[i], {}  # f分别为几个feature
            for e in samples:
                v, c = e[i], e[-1]  # youth refuse,yes agree的单个特征对应的label
                # print(v,c)
                if v not in stat[f].keys():  # stat[f].keys()是所有可能的特征，如果v不在特征里，就添加
                    print("stat",(stat[f]))
                    stat[f][v], stat[f][v]['n'], stat[f][v]['p'] = {}, 0, 0.0  # 三层嵌套字典n，p
                    stat[f][v][c], stat[f][v][c]['n'], stat[f][v][c]['p'] = {}, 0, 0.0
                #                    print(v,c,stat[f][v][c])
                elif c not in stat[f][v].keys():  # stat[f][v]是特征所对应的标签
                    stat[f][v][c], stat[f][v][c]['n'], stat[f][v][c]['p'] = {}, 0, 0.0
                stat[f][v]['n'] += 1  # 计算youth等的特征个数
                stat[f][v]['p'] = stat[f][v]['n'] / n_samples  # youth等特征所占的比例
                # print(stat[f][v][c])
                stat[f][v][c]['n'] += 1  # 计算每个特征的个数
                # print(stat[f])
                # update stat[f][v][every c]['p']
                for x in class_set:
                    if x not in stat[f][v].keys():  # 判断如果x为refuse或者agree在star[f][v]里
                        stat[f][v][x], stat[f][v][x]['n'], stat[f][v][x]['p'] = {}, 0, 0
                    stat[f][v][x]['p'] = stat[f][v][x]['n'] / stat[f][v]['n']  # 计算在全部youth特征中，refuse所占的比例
                    # print(stat[f][v],stat[f][v][x]['p'])
                    p = float(stat[f][v][x]['p'])
                    stat[f][v][x]['gini'] = 2 * p * (1 - p)  # 二分类的基尼指数公式，P83式5.23
                # update stat[f][v]['gini']
                d1_p, d2_p = stat[f][v]['p'], 1 - stat[f][v]['p']
                prob = (class_vals.count(div_label) - stat[f][v][div_label]['n']) / (
                            n_samples - stat[f][v]['n'])  # （满足划分条件的总数-youth中满足划分条件）/（总数-youth个数）
                d1_gini, d2_gini = stat[f][v][div_label]['gini'], 2 * prob * (1 - prob)
                stat[f][v]['gini'] = d1_p * d1_gini + d2_p * d2_gini  # 这4行，公式5.25P83
                # print("count",class_vals.count(div_label),"stat",stat[f][v][div_label]['n'],n_samples,stat[f][v]['n'])
                # print(stat[f], "prob", prob,d1_p*d1_gini,2*prob*(1-prob),stat[f][v]['gini'])
        # 选取最优特征，最优切分点, 最优叶子节点
        min_v_gini, bf_bv = 9527, []
        for i in range(len(feat_list)):  # 寻找基尼指数最小的集合,基尼指数最小则为最优切分点
            f = feat_list[i]  # show every feature
            for v in set([e[i] for e in samples]):  # show every value of feature
                if min_v_gini > stat[f][v]['gini']:
                    min_v_gini, bf_bv = stat[f][v]['gini'], [(f, v)]
                elif min_v_gini == stat[f][v]['gini']:
                    bf_bv.append((f, v))
        min_c_gini, bf, bv, bc = 9527, None, None, None  # best,min_c_gini的初值设置足够大即可
        for (f, v) in bf_bv:  # 存在多个相等gini的特征时，需要比较更细的条件进行筛选出一个最优特征
            for c in class_set:
                if min_c_gini > stat[f][v][c]['gini']:
                    min_c_gini = stat[f][v][c]['gini']
                    bf, bv, bc = f, v, c
                elif min_c_gini == stat[f][v][c]['gini']:
                    if stat[f][v][c]['p'] > stat[bf][bv][bc]['p']:
                        bf, bv, bc = f, v, c  # 选择基尼指数最小的特征

        # 找最优特征的次优分切点
        min_c_gini, better_v = 9527, None  # better value
        bf_v_set = set([e[feat_list.index(bf)] for e in samples])
        bf_v_set.remove(bv)
        for v in bf_v_set:  # 存在多个相等gini的特征时，需要比较更细的条件进行筛选出一个最优特征
            if min_c_gini > stat[bf][v]['gini']:
                min_c_gini, better_v = stat[bf][v]['gini'], v
            # print(bf,bv,bc,stat[bf], better_v)
        # 找最优特征的次优分切点的最优叶节点
        min_c_gini, better_c = 9527, None
        for c in class_set:
            # print(stat[bf][better_v])
            if min_c_gini > stat[bf][better_v][c]['gini']:
                min_c_gini, better_c = stat[bf][better_v][c]['gini'], c
            elif min_c_gini == stat[bf][better_v][c]['gini']:
                if stat[bf][better_v][c]['p'] > stat[bf][better_v][better_c]['p']:
                    better_c = c
        # print(bf, bv, bc, better_v, better_c, stat)
        return bf, bv, bc, better_v, better_c, stat

    def create_tree(self):
        if len(self.feat_list) < self.max_n_feats:
            return None  # 特征减少的异常处理
        # get current tree
        bf, bv, bc, better_v, better_c, stat = self.work(self.samples, self.feat_list, self.div_label, self.max_n_feats)
        root, rcond, rnode, lcond, lnode = bf, bv, bc, better_v, better_c
        # print('better_c:', better_c)
        # get child tree, first to tailor samles
        tailor = CTailorSamples(self.samples,
                                self.feat_list,
                                self.feat_list.index(bf),
                                bv)
        new_samples, new_feat_list = tailor.get_samples()  # new_samples去掉了house的最优节点，new_feat_list是去掉最优节点和次优节点的特征label
        # print("sample",new_samples, "feat_list",new_feat_list)
        cart = CCartTree(new_samples,
                         new_feat_list,
                         self.div_label,
                         self.max_n_feats)
        child_node = cart.get_tree_dict()  # 就是为了运行一下字典树tree_dict的函数，child_node为最优节点的右子树
        # print('child_node',child_node)
        # update current tree left-child-tree
        if child_node != None and child_node != {}:
            lnode = child_node

        # current tree dict
        self.tree_dict = {}
        self.tree_dict[root] = {}
        self.tree_dict[root][rcond] = rnode
        self.tree_dict[root][lcond] = lnode
        # print(self.tree_dict)
        return self.get_tree_dict()


# 定义判断结点形状,其中boxstyle表示文本框类型,fc指的是注释框颜色的深度
decisionNode = dict(boxstyle="round4", color='r', fc='0.9')
# 定义叶结点形状
leafNode = dict(boxstyle="circle", color='m')
# 定义父节点指向子节点或叶子的箭头形状
arrow_args = dict(arrowstyle="<-", color='g')


def plot_node(node_txt, center_point, parent_point, node_style):
    ''' 内部函数，外部不要调用
    绘制父子节点，节点间的箭头，并填充箭头中间上的文本
    :param node_txt:文本内容
    :param center_point:文本中心点
    :param parent_point:指向文本中心的点
    '''
    createPlot.ax1.annotate(node_txt,
                            xy=parent_point,
                            xycoords='axes fraction',
                            xytext=center_point,
                            textcoords='axes fraction',
                            va="center",
                            ha="center",
                            bbox=node_style,
                            arrowprops=arrow_args)


def get_leafs_num(tree_dict):
    '''内部函数，外部不要调用
    获取叶节点的个数
    :param tree_dict:树的数据字典
    :return tree_dict的叶节点总个数
    '''
    # tree_dict的叶节点总数
    leafs_num = 0
    if len(tree_dict.keys()) == 0:
        print('input tree dict is void!!!!!')
        return 0
    # 字典的第一个键，也就是树的第一个节点
    root = list(tree_dict.keys())[0]
    # 这个键所对应的值，即该节点的所有子树。
    child_tree_dict = tree_dict[root]
    for key in child_tree_dict.keys():
        # 检测子树是否字典型
        if type(child_tree_dict[key]).__name__ == 'dict':
            # 子树是字典型，则当前树的叶节点数加上此子树的叶节点数
            leafs_num += get_leafs_num(child_tree_dict[key])
        else:
            # 子树不是字典型，则当前树的叶节点数加1
            leafs_num += 1
    # 返回tree_dict的叶节点总数
    return leafs_num


def get_tree_max_depth(tree_dict):
    ''' 内部函数，外部不要调用
    求树的最深层数
    :param tree_dict:树的字典存储
    :return tree_dict的最深层数
    '''
    # tree_dict的最深层数
    max_depth = 0
    if len(tree_dict.keys()) == 0:
        print('input tree_dict is void!')
        return 0
    # 树的根节点
    root = list(tree_dict.keys())[0]
    # 当前树的所有子树的字典
    child_tree_dict = tree_dict[root]
    for key in child_tree_dict.keys():
        # 树的当前分支的层数
        this_path_depth = 0
        # 检测子树是否字典型
        if type(child_tree_dict[key]).__name__ == 'dict':
            # 如果子树是字典型，则当前分支的层数需要加上子树的最深层数
            this_path_depth = 1 + get_tree_max_depth(child_tree_dict[key])
        else:
            # 如果子树不是字典型，则是叶节点，则当前分支的层数为1
            this_path_depth = 1
        if this_path_depth > max_depth:
            max_depth = this_path_depth
    # 返回tree_dict的最深层数
    return max_depth


def plot_mid_text(center_point, parent_point, txt_str):
    '''内部函数，外部不要调用: 计算父节点和子节点的中间位置，并在父子节点间填充文本信息
    :param center_point:文本中心点
    :param parent_point:指向文本中心点的点
    '''
    x_mid = (parent_point[0] - center_point[0]) / 2.0 + center_point[0]
    y_mid = (parent_point[1] - center_point[1]) / 2.0 + center_point[1]
    createPlot.ax1.text(x_mid, y_mid, txt_str)
    return


def plotTree(tree_dict, parent_point, node_txt):
    '''内部函数，外部不要调用：绘制树
    :param tree_dict:树
    :param parent_point:父节点位置
    :param node_txt:节点内容
    '''
    leafs_num = get_leafs_num(tree_dict)
    root = list(tree_dict.keys())[0]
    # plotTree.totalW表示树的深度
    center_point = (plotTree.xOff + (1.0 + float(leafs_num)) / 2.0 / plotTree.totalW, plotTree.yOff)
    # 填充node_txt内容
    plot_mid_text(center_point, parent_point, node_txt)
    # 绘制箭头上的内容
    plot_node(root, center_point, parent_point, decisionNode)
    # 子树
    child_tree_dict = tree_dict[root]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    # 因从上往下画，所以需要依次递减y的坐标值，plotTree.totalD表示存储树的深度
    for key in child_tree_dict.keys():
        if type(child_tree_dict[key]).__name__ == 'dict':
            plotTree(child_tree_dict[key], center_point, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plot_node(child_tree_dict[key],
                      (plotTree.xOff, plotTree.yOff),
                      center_point, leafNode)
            plot_mid_text((plotTree.xOff, plotTree.yOff), center_point, str(key))
    # h绘制完所有子节点后，增加全局变量Y的偏移
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD
    return


def createPlot(tree_dict):
    '''唯一对外函数：绘制决策树图形
    :param tree_dict
    :return 无
    '''
    # 设置绘图区域的背景色
    fig = plt.figure(1, facecolor='white')
    # 清空绘图区域
    fig.clf()
    # 定义横纵坐标轴,注意不要设置xticks和yticks的值!!!
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    # 由全局变量createPlot.ax1定义一个绘图区，111表示一行一列的第一个，frameon表示边框,**axprops不显示刻度
    plotTree.totalW = float(get_leafs_num(tree_dict))
    plotTree.totalD = float(get_tree_max_depth(tree_dict))
    if plotTree.totalW == 0:
        print('tree_dict is void~')
        return
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(tree_dict, (0.5, 1.0), '')
    plt.show()


def create_samples():
    #功能函数，读表格的数据转换成list和list标签，最后一列为y
    ''''' 
    提供训练样本集 
    每个example由多个特征值+1个分类标签值组成 
    比如第一个example=['youth', 'no', 'no', '1', 'refuse'],此样本的含义可以解读为： 
    如果一个人的条件是：youth age，no working, no house, 信誉值credit为1
    则此类人会被分类到refuse一类中，即在相亲中被拒绝(也可以理解为银行拒绝为此人贷款)
    每个example的特征值类型为： 
    ['age', 'working', 'house', 'credit'] 
    每个example的分类标签class_label取值范围为：'refuse'或者'agree' 
    '''
    data=pd.read_excel("data.xlsx")
    data_list=list((data.values.tolist()))        #将读入的DataFrame格式的数据转换成list格式
    feat_list=list(data.columns[:-1])             #取第一行为特征标签
    return data_list, feat_list


if __name__ == '__main__':
    data_list, feat_list = create_samples()
    # 由CART算法得到决策树字典
    cart = CCartTree(data_list, feat_list, 'agree', 3)
    tree_dict = cart.get_tree_dict()
    # print_dict(tree_dict, 0, 'tree_dict')
    # # 绘制决策树
    # createPlot(tree_dict)