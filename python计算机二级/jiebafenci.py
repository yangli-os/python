import jieba
f=open("红楼.txt","r")
txt=f.read()
f.close()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)#从大到小排序，按照列表中第二个元素排序，
#第二个元素也就是个数，第一个元素是名字
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))#左对齐，宽度为10，右对齐，宽度为5
