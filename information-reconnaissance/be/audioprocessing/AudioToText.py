import speech_recognition as sr
import sys
import os
sys.path.append(os.path.abspath('../'))
from audioprocessing.GetAudio import get_audio

def audio_to_text(url):
    try:
        get_audio(url)
        print("Đang lấy mp3 của: ", url)
        # Khởi tạo recognizer
        r = sr.Recognizer()

        # Mở file đã được chuyển đổi
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio')
        with sr.AudioFile(directory + "/temped.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="vi-VN")
            return text
    except Exception as e:
        print("Đã xảy ra lỗi không có giọng nói:", str(e))   
        return 'Không có giọng nói'   
