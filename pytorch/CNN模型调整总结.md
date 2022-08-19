
本篇博客是一个简单的记录，记录CNN模型调整过程当中的一些问题。

# 1，transforms.Compose的一些用法
```
self.transform = transforms.Compose([transforms.Resize([351,240]), transforms.CenterCrop([351,240]), transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
```
transforms的这个折腾了很长事件，它transforms.Compose是一个集合，在这个集合里面可以设置图片缩放大小，裁剪大小，归一化等等操作。

这里需要注意，当Resize只有一个参数时，是将图片的短边拉成Resize的大小，再进行中心裁剪CenterCrop时按照从中心计算的区域进行裁剪。  
ToTensor是将向量进行Tensor的归一化计算。  
transforms.Normalize则是规定了具体归一化的均值和方差。

# 2.模型训练
```
loss_list = []
acc_list = []

class Network(nn.Module):
    def __init__(self):
        super(Network,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=7,stride=2)
        self.conv2 = nn.Conv2d(in_channels=256, out_channels=16, kernel_size=7,stride=2)
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=5)
        self.conv4 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[8,4])

        self.fc1 = nn.Linear(in_features=16, out_features=16)
        self.out = nn.Linear(in_features=16, out_features=2)
    def forward(self, t):
        #Layer 1
        t = t
        #Layer 2
        t = self.conv1(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)#output shape : (6,14,14)
        #Layer 3
        t = self.conv2(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)#output shape : (6,14,14)
        #Layer 4
        t = self.conv3(t)
        t = F.relu(t)
        t = F.max_pool2d(t, kernel_size=2, stride=2)#output shape : (6,14,14)
        #Layer 5      
        t = self.conv4(t)
        t = F.relu(t)
        
        #Layer 5
        t=t.flatten(start_dim=1)
        t = self.fc1(t)
        t = F.relu(t)#output shape : (1,120)
        #Layer 5
        t = self.out(t)

        return t

network = Network()

print(network)
optimizer = optim.Adam(network.parameters(), lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
```
我batch_size的设置更改的比较多，再调整模型参数时主要调整了卷积的层数，神经元个数，卷积核的尺寸以及stride等。这里对参数需要注意的地方逐一记录一下。
```
 nn.Conv2d(in_channels=3, out_channels=256, kernel_size=7,stride=2)
 ```
每一层的卷积都跟它上一层的输入输出有关，在第一层的卷积时，有几个参数需要注意。  
in_channels 为输入的维度，是图片的通道数
out_channels 是自己可以随意设置的第一层卷积的输出
kernel_size 是卷积核的尺寸
stride 是卷积步长
卷积图片尺寸的计算为
（W - kernel——size）/stride+1
因为我的图片较大，所以设置stride为2，可以快速的提取特征，经过池化后缩小尺寸。

注意：在此可以设置kernel_size为原始图像大小，但是输出的图片为X*X*1*1，就无法进行池化运算了。一般卷积核大小kernel_size设置为3，5，7为宜。

在卷积层之后，输入到线性层之前，使用了t.flatten(start_dim=1)，这里是因为卷积核输出后的数据格式是[x*x*1*1]，相当于是一个四维数据，输入linear的时候需要是[x*x]的形式，所以用了flatten展平，start_dim=1是不改变原有的尺寸。

还有一点，在输入linear的时候实际上与数据做的是矩阵运算，所以，对于[x*y]维度的数据，需要[y*x]的权重矩阵进行乘法运算才行。


# 3.实际训练
```
for epoch in range(epochs):
    time_start = time.time()
    total_correct = 0
    total_loss = 0
    for batch in train_loader:  # Get batch
        images, labels = batch  # Unpack the batch into images and labels

        preds = network(images)  # Pass batch
        loss = F.cross_entropy(preds, labels)  # Calculate Loss

        optimizer.zero_grad()
        loss.backward()  # Calculate gradients
        optimizer.step()  # Update weights

        total_loss += loss.item()
        total_correct += preds.argmax(dim=1).eq(labels).sum().item()
    time_end = time.time() - time_start
    print('time',time_end)
    loss_list.append(total_loss)
    acc_list.append(total_correct)
    print('epoch:', epoch, "total_correct:", total_correct, "loss:", total_loss)
print('>>> Training Complete >>>')
```
训练过程就是把数据放到我们已经搭建好的模型里面跑一下，这里需要注意的是损失函数的设置，将会印象分类的准确度。也就是F.cross_entropy()

这里的total_correct是整体准确的个数，用它除以总数就是准确率了。

# 4.准确率的计算
```
# 保存模型
PATH = './NIR.pth'
torch.save(network.state_dict(), PATH)
# 加载模型
network = Network()
network.load_state_dict(torch.load(PATH))

@torch.no_grad()
def get_all_preds(model, loader):
    all_preds = torch.tensor([])
    print(len(loader))
    for batch in loader:
        images, labels = batch

        preds = model(images)
        all_preds = torch.cat((all_preds, preds) ,dim=0)

    return all_preds

test_preds = get_all_preds(network, test_loader)
actual_labels_test = torch.Tensor(test_data.labels)
preds_correct_test = test_preds.argmax(dim=1).eq(actual_labels_test).sum().item()

print('total correct:', preds_correct_test)
print('accuracy_test:', preds_correct_test / len(test_data))
```
这里注意一个问题，我想知道我在训练集上的模型准确率，直接按照accuracy_test的计算方式进行计算，我适用的是train_data.laber。但是这里我发现，因为我设置了batch_size为16，而数据总数是415，所以我发现在经过batch_size后，我的train_loader为25个batch_size，即为400个，train_data为415，这个就是在batch_size无法整除数据时所造成的问题。

那么从另一个点上也就是说，我实际上只有400个数据参与了模型训练，而不是415个。

# 5.画一个matrix图，展示正确时错误的数据
```
# 画一个matrix图展示正确和错误的数据
import itertools
import numpy as np
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

cm = confusion_matrix(test_data.labels, test_preds.argmax(dim=1))
classes = ('0','1')
plt.figure(figsize=(10,10))
plot_confusion_matrix(cm, classes)
```
这篇作为深度学习的第二篇文章，还是有很多需要学习和调整的东西。CNN太久没用过了，连基础的理论知识都忘记了。而pytorch边学边用，也发现了很多的问题。

做的多了，调试的多了，甚至报错多了，也都能够发现一些问题，总结经验，才能更好的理解。

下一篇会介绍模型调优，finetune相关的内容。