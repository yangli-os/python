使用环境：
# baidu_aip_voice.py
pip install baidu-aip。

# synthesis_win.py
在Windows环境下运行，需要ffmpeg。
pip install ffmpeg
语音使用baidu-aip生成，无法使用ffmpeg进行合成，基础音频采用迅捷文字转语音生成。

# syn_syn.en.py
是英语生成的最终版本，需要将中文命名好的音频文件和rename_en.py放到同一文件夹下进行运行，生成英文名的基础音频文件，以供服务器等设备调用。

# reload_song.py
#编辑wav格式的音频文件，将音频文件添加上头，该头可以直接在web端播放

# reload_syn_syn_en.py
通过requests方式获取post服务中的文件并下载

# replace_name.py
之前使用中文作为音频名，通过字典将中文音频名替换成为英文音频

# TODO
最终的几个版本的音频文件和音频程序后续整理上传
