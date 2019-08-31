# -*- coding: utf-8 -*
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '17084747'
API_KEY = 'DBz2N6iV9tCrCGVeoBYWNBAa'
SECRET_KEY = 'QwmbnPwyEugy7RZ10xuANl82WSiAMzuB'

sourse="12321.42"
numbers_list=['零','一','二','三','四','五','六','七','八','九']
units_list=["拾","佰","仟","万","亿"]
others_list=["已收到","点"]

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def create_sound_basic(basic):
    result  = client.synthesis(basic, 'zh', 1, {'vol': 5,'per':0})
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(basic+'.wav', 'wb') as f:
            f.write(result)

#creat basic sound
for numbers in numbers_list:
    create_sound_basic(numbers)
for numbers in units_list:
    create_sound_basic(numbers)
for numbers in others_list:
    create_sound_basic(numbers)