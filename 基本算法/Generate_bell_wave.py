#生成钟型波
def Generate_bell_wave(wave_up):
    #inputs：DataFrame类型的前半个波
    #outputs:DataFrame类型的全部波
    last_postion = list(dict(wave_up.tail(1)).keys())[0] #取一个series类型里最后一个的行标
    wave_all = wave_up.copy()                            #硬拷贝以防止原始值也被修改
    #输入为pandas类型数据需要先转为array格式处理
    wave_up_list = list(np.array(wave_up))
    for j in range(2,len(wave_up_list)+1):
        wave_all[last_postion+j-1] = (np.array(wave_up)[len(wave_up)-j])    #最高点只有1个构建整个钟型波
    return wave_all
