#编辑wav格式的音频文件，将音频文件添加上头，该头可以直接在web端播放
import struct
from pydub.audio_segment import AudioSegment
import wave
with open("oneyuan.wav","rb") as f1:
    data = f1.read()
old_data = AudioSegment.from_wav("oneyuan.wav")
def writeframesraw(b):
    WAVE_FORMAT_PCM = 0x0001
    headers = bytes()
    headers += b'RIFF'
    nframes = int(b.frame_count())
    datalength = nframes * b.channels * b.sample_width
    #添加头
    headers += struct.pack('<L4s4sLHHLLHH4s',
                           36 + datalength, b'WAVE', b'fmt ', 16,
                           WAVE_FORMAT_PCM, b.channels, b.frame_rate,
                           b.channels * b.frame_rate * b.sample_width,
                           b.channels * b.sample_width,
                           b.sample_width * 8, b'data')
    headers += struct.pack('<L', datalength)
    ret = headers + b.raw_data
    return ret
new_data = writeframesraw(old_data)
with open("int.wav","wb") as f1:
    f1.write(new_data)
