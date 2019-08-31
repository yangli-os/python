# -*- coding: utf-8 -*
from pydub import AudioSegment
import sys,os

sourse="1045003.42"
numbers_list=['零','一','二','三','四','五','六','七','八','九']
units_list=["拾","佰","仟","万","亿"]
others_list=["已收到","点"]
sourse_int = str(int(eval(sourse)))
#input a str number

def basic_num(basic_int):
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
    out_int = out_int.strip("零")  # delet first and end zero
    for j in range(4):
        out_int = out_int.replace("零零","零")  #delet double zero
        out_int = out_int.replace("一拾", "拾")  # delet double zero
        out_zhong = out_int
    return out_int

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
#have dot
sourse_float = eval(sourse)-eval(sourse_int)
if sourse_float != 0:
    two_dot = numbers_list[int(str(sourse_float)[2])] + numbers_list[int(str(sourse_float)[3])]   #two_dot
    out_zhong +=others_list[1] + two_dot
out_zhong = out_zhong.replace("零万","")         #delet_00000
print(out_zhong)
def mix_wav(sound_out):
    len_index=""
    len_sound=len(sound_out)
    cmd = 'ffmpeg'
    for filename in sound_out :
        cmd = cmd + ' -i ' + filename+".wav"
    for dex in range(len_sound):
        len_index = len_index + "["+str(dex)+":0]" + " "
    cmd = cmd + " -filter_complex '"+str(len_index) + "concat=n="+str(len_sound) + " :v=0:a=1 [a]' -map [a] " +'output.wav'
    print(cmd)
    os.system(cmd)
    # os.system("ffplay output.wav -af atempo=2.0")
    # os.system("ffplay -autoexit output.wav")
def mix_dub(sound_out):
    song_out = AudioSegment.from_wav(str(others_list[0]+".wav"))
    for sound in sound_out:
        len_index = str(sound) + ".wav"
        song_out = song_out + AudioSegment.from_wav(str(len_index))
    return song_out
song_out = mix_dub(out_zhong)
song_out.export("sound_out.wav".format("wav"))
