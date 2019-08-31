try:
    model.load_weights("SaveModel/cifarCnnModel.h5")      #模型存储在SaveModel文件夹下
    print('模型加载成功，继续训练模型')
except:
    print("加载模型失败，开始训练新模型")


model.save_weights("SaveModel/cifarCnnModel.h5")       #模型存储在SaveModel文件夹下
print("模型保存成功")