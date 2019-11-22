# -*- coding: utf-8 -*
from pydub import AudioSegment
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=["POST"])
def regist():
    data = request.data
    dic = eval(data)
    source = dic["number"]
    numbers_list = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    units_list = ["拾", "佰", "仟", "万", "亿"]
    others_list = ["已收到", "元", "角", "分"]
    sourse_int = str(int(eval(source)))
    try:
        if int(sourse_int) >= 100000:  # Over one hundred thousand
            song_out = AudioSegment.from_wav("您的交易数额过大.wav")
        else:
            out_zhong = strip_number(sourse_int)
            song_out = mix_dub(out_zhong)
        song_out.export("sound_out.wav", format("wav"))
    except:
        print("您输入的数值有误")
    return "sound_out.wav"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7778)

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
    #mix all sound
    song_out = AudioSegment.from_wav(str(translate_zh(str(others_list[0])) + ".wav"))
    len_zhong = int(len(out_zhong))
    if len_zhong > 2:
        for sim in range(len_zhong-2):                                                                       #if not end
            if (out_zhong[sim] in numbers_list) & (out_zhong[sim] != "零") & (out_zhong[sim] != "元"):
                sim_two = out_zhong[sim] +out_zhong[sim+1]
                two_sound_path = str(translate_zh(str(sim_two))) + ".wav"
                two_sound = AudioSegment.from_wav(two_sound_path)
                song_two = two_sound[30:-30]
                song_out = song_out.append(song_two,crossfade=40)
            elif (out_zhong[sim] == "零"):
                sim_two = out_zhong[sim]
                two_sound_path = str(translate_zh(str(sim_two))) + ".wav"
                two_sound = AudioSegment.from_wav(two_sound_path)
                song_two = two_sound[20:-20]
                song_out = song_out.append(song_two, crossfade=10)
            elif (out_zhong[sim] == "元"):
                if (out_zhong[sim-1]) in units_list:
                    sim_two = out_zhong[sim]
                    two_sound_path = str(translate_zh(str(sim_two))) + ".wav"
                    two_sound = AudioSegment.from_wav(two_sound_path)
                    song_two = two_sound[20:-20]
                    song_out = song_out.append(song_two, crossfade=10)
        if out_zhong[-2] in units_list:                                                            #if simple end
            end_path = str(translate_zh(str((out_zhong[-1:])))) + "_end.wav"
        else:
            end_path = str(translate_zh(str((out_zhong[-2:])))) + "_end.wav"
    else:
        end_path = str(translate_zh(str((out_zhong[-2:])))) + "_end.wav"
    end_sound = AudioSegment.from_wav(end_path)
    end_song = end_sound[30:-30]
    song_out = song_out.append(end_song, crossfade=10)
    return song_out

# Chinese translate English
def translate_zh(zh):
    zh_en_dict = {'零':"zero", '一':"one", '二':"two", '三':"three", '四':"four", '五':"five", '六':"six", '七':"seven", '八':"eight", '九':"nine",
                  "拾":"shi", "佰":"bai", "仟":"qian", "万":"wan", "亿":"yi",
                  "已收到":"received", "元":"yuan", "角":"jiao", "分":"fen"}
    if "已" not in zh:
        zh_en = ""
        for z in zh:
            zh_en = zh_en + zh_en_dict[z]
    else:                                                              #已到账.wav translate
        zh_en = zh_en_dict[zh]
    return zh_en