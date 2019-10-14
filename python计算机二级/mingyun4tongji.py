# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:22:02 2018

@author: liyang
"""

names = ["命运", "寻梦"]
for name in names:
    fi = open(name+"-网络版.txt", "r", encoding="utf-8")
    fo = open(name+"-字符统计.txt", "w", encoding="utf-8")
    txt = fi.read()
    d = {}
    for c in txt:
        d[c] = d.get(c, 0) + 1
    del d['\n']
    ls = list(d.items())
    ls.sort(key=lambda x:x[1], reverse=True)
    for i in range(100):
        ls[i] = "{}:{}".format(ls[i][0], ls[i][1])
    fo.write(",".join(ls[:100]))
    fi.close()
    fo.close()
def getList(name):
    f = open(name+"-字符统计.txt", "r", encoding="utf-8")
    words = f.read().split(',')
    print(words)
    for i in range(len(words)):
        words[i] = words[i].split(':')[0]
    f.close()
    return words
def main():
    fo = open("相同字符.txt", "w")
    ls1 = getList("命运")
    ls2 = getList("寻梦")
    ls3 = []
    for c in ls1:
        if c in ls2:
            ls3.append(c)
    fo.write(",".join(ls3))
    fo.close()
main()