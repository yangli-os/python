# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:26:10 2019

@author: hp
"""
import re,os
file=r"repace.txt"   #转换的文件文件，只能是单个码
def del_resubstart(file,old_str,new_str):    #replace
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            f2.write(re.sub(old_str,new_str,line))
    os.remove(file)
    os.rename("%s.bak" % file, file)
del_resubstart(file, "\"\"", "")

def start_code(file):          #re_startup
    with open(file,'r') as f1:
        data=f1.read()
    start_code=re.finditer("\"startup_code1.*",data)
    number_start_grs=[]
    for start_c in start_code:
        start_cd=start_c.group()
        try:
            start_end_cd=start_cd[-10:]
            number_start=re.compile("\d+")
            number_start_se=number_start.search(start_end_cd)
            number_start_gr=number_start_se.group()
            if int(number_start_gr)>100:
                number_start_grs.append(number_start_gr)
        except:
            continue
    number_start_grs=(" ,").join(number_start_grs)
    staticir="{ \"str1\": \"\ nconst static irda_baisc_bit_t startup_code1 =\ n{\ n    IRDA_LEVEL_H2L, "+str(number_start_grs)+"\ n};\ n\""
    del_resubstart(file,"{\"str1\":",staticir)
    del_resubstart(file,"\"startup_code1.*","")
start_code(file)

def bit_code(file):      #re_bit_data
    with open(file,'r') as f1:
        data=f1.read()
    bit_code=re.finditer("\"bit_.*",data)
    number_bit_grs=[]
    for bit_c in bit_code:
        bit_cd=bit_c.group()
        try:
            bit_end_cd=bit_cd[-10:]
            number_bit=re.compile("\d+")
            number_bit_se=number_bit.search(bit_end_cd)
            number_bit_gr=number_bit_se.group()
            if int(number_bit_gr)>100:
                number_bit_grs.append(number_bit_gr)
        except:
            continue
    number_bit_grs1=number_bit_grs[:4]
    number_bit_grs2=number_bit_grs[4:]
    number_bit_grs1=(" ,").join(number_bit_grs1)
    number_bit_grs2=(" ,").join(number_bit_grs2)
    bit01="\"\ nconst static irda_bit01_t bit01 =\ n{\ n    {IRDA_LEVEL_H2L,  "+number_bit_grs1+"},\ n"+"    {IRDA_LEVEL_H2L, "+number_bit_grs2+"\ n};\ n\""
    del_resubstart(file,"\"local irda_level_e = {}.*\"",bit01)
    del_resubstart(file,"\"bit_.*","")
bit_code(file)

def stream_bit(file):           #re_bit_stream
    with open(file,'r') as f1:
        data=f1.read()
    bit_code=re.finditer("\"local data_stream_bit.*\"",data)
    number_bit_grs=[]
    for bit_c in bit_code:
        bit_cd=bit_c.group()
        try:
            number_bit=re.compile("\(\d.*\d\)")
            number_bit_se=number_bit.search(bit_cd)
            number_bit_gr=number_bit_se.group()
            number_bit_grs.append(number_bit_gr)
        except:
            continue
    number_streams=[]
    for number_stream in range(len(number_bit_grs)):
        number_streamw="\"\ n#define DATA_STREAM_"+str(number_stream+1)+"_BIT "+number_bit_grs[number_stream]+"\ n\""
        number_streams.append(number_streamw)
    number_streams=("\n").join(number_streams)
    del_resubstart(file,"\"local data_stream_bit.*\"","")
    del_resubstart(file,"\"local bit_low = {}.*\"",number_streams)
stream_bit(file)
del_resubstart(file,"\"irda_level_e.*","")
del_resubstart(file,"\n\n","\n")

def end_code(file):            #re_end_code
    with open(file,'r') as f1:
        data=f1.read()
    bit_code=re.finditer("\"end_code1.*\"",data)
    number_bit_grs=[]
    for bit_c in bit_code:
        bit_cd=bit_c.group()
        try:
            bit_end_cd=bit_cd[-10:]
            number_bit=re.compile("\d+")
            number_bit_se=number_bit.search(bit_end_cd)
            number_bit_gr=number_bit_se.group()
            if int(number_bit_gr)>100:
                number_bit_grs.append(int(number_bit_gr))
        except:
            continue
    nuber=len(number_bit_grs)//4
    number_streams=[]
    for number_stream in range(nuber):
        linshi=number_bit_grs[4*(number_stream):4*(1+number_stream)]
        linshi="".join(str(linshi))
        number_streamw="\"\ nconst static irda_baisc_bit_t end_code"+str(number_stream+1)+" =\ n{\ n    IRDA_LEVEL_H2L, "+str((linshi[1:-1]))+"\ n};\ n\""
        number_streams.append(number_streamw)
    number_streams=("\n").join(number_streams)
    del_resubstart(file,"\"local bit_high = {}.*",number_streams)
end_code(file)

#delete_
del_resubstart(file,".*\"local end_code.*","")
del_resubstart(file,"\"end_code.*","")
del_resubstart(file,"\"local startup_code.*","")
del_resubstart(file,"\"str2\":.*",",\n \"str2\":")

def str2_irda_start(file):         #re_merge_basic_logic
    with open(file,'r') as f1:
        data=f1.read()
    bit_code=re.finditer("\"len.*\"",data)
    for bit_c in bit_code:
        bit_cd=bit_c.group()
        try:
            number_bit=re.compile("startup_code1\)")
            number_bit_se=number_bit.search(bit_cd)
            number_bit_gr=number_bit_se.group()
            number_bit_frame="\"\ n    irda_merge_basic_logic(frame, &startup_code1);\""
            if str(number_bit_gr)=="startup_code1)":
                del_resubstart(file,".*startup_code1\).*",number_bit_frame)
        except:
            continue
str2_irda_start(file)

def str2_irda_data(file):
    with open(file,'r') as f1:
        data=f1.read()
    bit_code=re.finditer(".*bit_low, bit_high.*",data)
    for bit_c in bit_code:
        bit_cd=bit_c.group()
        try:
            number_bit=re.compile("data_stream_bit.")
            number_bit_se=number_bit.search(bit_cd)
            number_bit_gr=number_bit_se.group()
            linshitihuan=".*"+str(number_bit_gr)+".*"
            number_bit_frame="\"\ n    irda_merge_data_frame(frame, &bit0"+str(number_bit_gr[-1])+", &data_stream"+str(number_bit_gr[-1])+");\""
            del_resubstart(file,linshitihuan,number_bit_frame)
        except:
            continue
str2_irda_data(file)

def str2_irda_end(file):
    with open(file,'r') as f1:
        data=f1.read()
    end_code=re.finditer("end_code.\)",data)
    for end_c in end_code:
        end_cd=end_c.group()
        try:
            number_end=re.compile("end_code.\)")
            number_end_se=number_end.search(end_cd)
            number_end_gr=number_end_se.group()
            number_end_frame=" \"\ n    irda_merge_basic_logic(frame, &"+str(number_end_gr)+";\""
            linshitihuan_end=".*"+str(number_end_gr[:-1])+"\).*"
            del_resubstart(file,linshitihuan_end,number_end_frame)
        except:
            continue
str2_irda_end(file)
del_resubstart(file,"},\Z",",\n },")
