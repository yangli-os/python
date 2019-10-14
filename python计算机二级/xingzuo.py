fi=open("SunSign.csv","r",encoding="utf-8")
ls=[]
for line in fi:  
    line=line.replace("\n","")
    ls.append(line.split(","))
fi.close()
print(ls)
while True:
    inputstr=input()
    inputstr.strip()
    flag=False
    if inputstr=="exit":
        break
    for line in ls:
        if inputstr==line[0]:
            print("{}座的生日位于{}-{}之间".format(chr(eval(line[3])),line[1],line[2]))
            flag=True
    if flag==False:
        print("星座名字输入有误")
