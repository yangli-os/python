# -*- coding: utf-8 -*
from pydub import AudioSegment

sourse="003.43"
numbers_list=['零','一','二','三','四','五','六','七','八','九']
units_list=["拾","佰","仟","万","亿"]
others_list=["已收到","点"]
sourse_int = str(int(eval(sourse)))

def basic_num(basic_int):
    # input a str number
    if len(str(basic_int)) == 4:
        out_int = ""
    else:
        out_int = "零"
    for i in range(len(str(basic_int))):
        if int(basic_int[i]) != 0:
            if i != len(str(basic_int)) - 1:
                out_int = out_int+str(numbers_list[int(basic_int[i])]) + str(units_list[len(str(basic_int)) - i - 2])
            elif i == len(basic_int) - 1:
                out_int = out_int+str(numbers_list[int(basic_int[i])])
        else:
            if i != len(str(basic_int)) - 1:
                out_int = out_int+str(numbers_list[int(basic_int[i])])
    out_int = out_int.strip("零")                                           # delet first and end zero
    for j in range(4):
        out_int = out_int.replace("零零","零")                               # delet double zero
        if "佰" not in out_int:
            out_int = out_int.replace("一拾", "拾")
        out_zhong = out_int
    return out_int

def strip_number(sourse_int):
    if (len(str(sourse_int)) <= 8) & (len(str(sourse_int)) > 4):
        monst = str(int(sourse_int) // 10000)
        basic = str(int(sourse_int) % 10000)
        monst_zh = basic_num(monst)
        basic_zh = basic_num(basic)
        if "仟" not in basic_zh:
            out_zhong = monst_zh +"万"+"零"+basic_zh
        else:
            out_zhong = monst_zh + "万" + basic_zh
    elif len(str(sourse_int)) <= 4:
        basic = sourse_int
        basic_zh = basic_num(basic)
        out_zhong = basic_zh
    elif len(str(sourse_int)) > 8:
        more = str(int(sourse_int) // 100000000)
        monst = str(int(int(sourse_int) - int(more) * 100000000) // 10000)
        basic = str(int(sourse_int) % 10000)
        more_zh = basic_num(more)
        monst_zh = basic_num(monst)
        if "仟" not in monst_zh:
            out_zhong = more_zh+"亿"+"零"+monst_zh + "万"
        elif "仟" in monst_zh:
            out_zhong = more_zh+"亿"+monst_zh + "万"
        basic_zh = basic_num(basic)
        if "仟" not in basic_zh:
            out_zhong = out_zhong + "零" + basic_zh
        elif "仟" in basic_zh:
            out_zhong = out_zhong + basic_zh
    out_zhong =out_zhong + others_list[1]
    #have dot
    sourse_float = eval(sourse)-eval(sourse_int)
    if sourse_float != 0:
        two_dot = ""
        dot_sourse_float = len(str(sourse_float))
        sourse_dot = int((round(sourse_float,2))*100)
        if len(str(sourse_dot)) == 1:
            sourse_dot = "0" + str(sourse_dot)
        for dot in range(len(str(sourse_dot))):
            two_dot = two_dot + numbers_list[int(str(sourse_dot)[dot])] + others_list[2+int(dot)]
        two_dot = two_dot.replace("零角","").replace("零分","")
        out_zhong = out_zhong + two_dot
    out_zhong = out_zhong.replace("零万","")                              #delet_00000
    return out_zhong

def mix_dub(out_zhong):
    song_out = AudioSegment.from_wav(str(others_list[0]+".wav"))
    for sound in sound_out:
        len_index = str(sound) + ".wav"
        song_out = song_out + AudioSegment.from_wav(str(len_index))
    return song_out

out_zhong = strip_number(sourse_int)
song_out = mix_dub(out_zhong)
song_out.export("sound_out.wav".format("wav"))
