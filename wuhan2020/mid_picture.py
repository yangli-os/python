# -*- coding:utf-8 -*-
from PIL import Image , ImageDraw , ImageFont


def write_to_pic (name_pre ,name , project,price):  # 执行完这个方法后生成一个 result.png 图片
    im = Image.open("picture.jpg")
    draw = ImageDraw.Draw(im)
    font_name = ImageFont.truetype('font/1.ttf' , 100)  # 名字的字体和字号
    imwidth , imheight = im.size
    font_width_pre , font_height_pre = draw.textsize(name_pre , font_name)  # 获取名字的大小
    font_width , font_height = draw.textsize(name , font_name)  # 获取名字的大小
    font_width_project , font_height_project = draw.textsize(project , font_project)  # 获取名字的大小
    draw.text(((imwidth - font_width_pre - font_name.getoffset(name)[0]) / 2 , 620) , text = name_pre , font = font_name ,
        fill = (0 , 0 , 0))  # 写上名字 x使用了居中
    draw.text((1725 , 1325) , price , font = SetFontPrice , fill = (0 , 0 , 0))  # 日期
    im.save(name + ".png")

write_to_pic("William Heath,He Huang,Joann Arce,Wendy Liu","Junior McGrath,Binod Bajracharya,Jang Leong Chia,Ismail Shuaau" , "autovax","二等奖")
