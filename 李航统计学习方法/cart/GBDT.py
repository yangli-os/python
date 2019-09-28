from numpy import *


# adaBoost算法
# 决策树桩仅分裂一次，也就是说只选择一次特征
# 决策树桩由三部分组成，特征，特征值，不等号的方向

# 读入数据
def loadData():
    dataMat = matrix([[0., 1., 3.],
                      [0., 3., 1.],
                      [1., 2., 2.],
                      [1., 1., 3.],
                      [1., 2., 3.],
                      [0., 1., 2.],
                      [1., 1., 2.],
                      [1., 1., 1.],
                      [1., 3., 1.],
                      [0., 2., 1.]])
    classLabels = matrix([-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, -1.0, -1.0]).T
    return dataMat, classLabels


# 根据当前树桩对数据进行分类
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0], 1))  # 预测矩阵
    # 左叶子 ，整个矩阵的样本进行比较赋值
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    return retArray


'''
# 根据数据，标签和权值分布构造弱分类器，即决策树桩 stump 树桩
# D为数据权重向量
# numStep是步数，据此可算出步长， bestClassEst是最优情况下的分类情况
构造树桩要做的是： 选择合适的特征，选择合适的阈值
bestStump['dim'] 合适的特征所在维度
bestStump['thresh']  合适特征的阈值
bestStump['ineq'] 
'''


def buildStump(dataMatrix, classLabels, D):
    m, n = shape(dataMatrix)
    numStep = 10.0
    bestStump = {}  # 字典
    minError = inf
    bestClasEst = mat(ones((m, 1)))
    # n是特征的种类数
    for i in range(n):
        rangeMin = dataMatrix[:, i].min()  # 求每一种特征的最大最小值
        rangeMax = dataMatrix[:, i].max()
        stepSize = (rangeMax - rangeMin) / numStep
        for j in range(-1, int(numStep) + 1):
            threshVal = rangeMin + j * stepSize
            # 不知左树-1准确率高还是右树，因此有这样一个计算
            for inequal in ['lt', 'rt']:
                predictVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m, 1)))
                errArr[predictVals == classLabels] = 0
                weightedError = D.T * errArr
                if weightedError < minError:
                    minError = weightedError
                    bestClassEst = predictVals
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst


# adaBoost训练过程
def adaBoostTrain(dataMatrix, classLabels, numIter=40):
    weakClassArr = []  # 弱分类器
    m = shape(dataMatrix)[0]  # 样本个数
    D = mat(ones((m, 1)) / m)  # 一开始是均值权重分布
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIter):  # numIter 弱分类器的个数
        bestStump, error, classEst = buildStump(dataMatrix, classLabels, D)
        # 防止除以零溢出
        alpha = float(0.5 * log((1 - error) / max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        expon = multiply(-1 * alpha * classLabels, classEst)
        D = multiply(D, exp(expon))
        D /= D.sum()
        aggClassEst += alpha * classEst  # 弱分类器结果的求和
        # 比较两个矩阵的值得出预测正误情况
        aggError = sign(aggClassEst) != classLabels
        errorRate = aggError.sum() / m
        print(errorRate)
        if errorRate == 0.0:
            break
    return weakClassArr


def adaClassify(dataMatrix, classifierArr):
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    for i in range(len(classifierArr)):
        stump = classifierArr[i]
        classEst = stumpClassify(dataMatrix, stump['dim'], stump['thresh'], stump['ineq'])
        aggClassEst += stump['alpha'] * classEst
    return sign(aggClassEst)


dataMat, classLabels = loadData()
classifiers = adaBoostTrain(dataMat, classLabels, 9)
labels = adaClassify(mat([1, 2, 3]), classifiers)
print(labels)
print('dim\tthresh\tinep\talpha')
for i in range(6):
    print(str(classifiers[i]['dim']) + '\t' + str(classifiers[i]['thresh'])
          + '\t' + str(classifiers[i]['ineq']) + '\t' + str(classifiers[i]['alpha']))
