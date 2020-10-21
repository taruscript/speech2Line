import speech_recognition as sr
 

def voice_recognize():
    r = sr.Recognizer()
    
    with sr.AudioFile("sample.wav") as source:
        audio = r.record(source)
    
    result = r.recognize_google(audio, language='ja-JP')

    return result