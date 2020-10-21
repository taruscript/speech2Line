import speech_recognition as sr
 
import numpy as np
import pyaudio  #録音機能を使うためのライブラリ
import wave     #wavファイルを扱うためのライブラリ
 

def voice_recode():
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 48000 # 録音は48kHz
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME ="sample.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        buf = np.frombuffer(data, dtype="int16") # 読み込んだストリームデータを2byteのInt型のリストに分離
        frames.append(b''.join(buf[::3])) # 記録するデータを1/3に間引いてリストを結合してフレームに追加

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE / 3) # ヘッダのサンプリングレートを16kHzにする
    wf.writeframes(b''.join(frames))
    wf.close()


def voice_recognize(): 
    r = sr.Recognizer()
    with sr.AudioFile("sample.wav") as source:
        audio = r.record(source)
    result = r.recognize_google(audio, language='ja-JP')
    return result
