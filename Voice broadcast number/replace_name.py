import os
import shutil
path = "/home/liyang/Speech_synthesis/syn_basic"
def translate_zh(zh):
    zh_en_dict = {'零':"zero", '一':"one", '二':"two", '三':"three", '四':"four", '五':"five", '六':"six", '七':"seven", '八':"eight", '九':"nine",
                  "拾":"shi", "佰":"bai", "仟":"qian", "万":"wan", "亿":"yi",
                  "已收到":"received", "元":"yuan", "角":"jiao", "分":"fen"}
    zh_en = zh_en_dict[zh]
    return zh_en
name_list = os.listdir(path)
for name in name_list:
    if name[-4:] == ".wav":
        re_name = ""
        try:
            if "_end" not in name:
                if "已" in name:
                    re_name = translate_zh(name[:-4])
                    re_out = re_name + ".wav"
                elif "过" in name:
                    re_name = "Over number"
                    re_out = re_name + ".wav"
                else:
                    for na in name[:-4]:
                        en = (translate_zh(na))
                        re_name = re_name + en
                    re_out = re_name + ".wav"
            elif "_end" in name:
                for na in name[:-8]:
                    en = (translate_zh(na))
                    re_name = re_name + en
                re_out = re_name + "_end.wav"
                print(re_out)
            shutil.copyfile(name,re_out)
        except:
            continue