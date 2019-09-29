import requests
from pydub.audio_segment import AudioSegment
import json
import wave

#下载服务器的指定文件
file = {'number': "500.3"}
r = requests.post('http://10.200.13.222:7778',data = json.dumps(file))
file = r.content    #获取文件内容
print(file)
with open("song_out.wav","wb") as f:
    f.write(file)