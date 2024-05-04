import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content

def get_data_content(text):
    try:
        top_6_word = []
        top_6_word = detect_content(text)
        
        return top_6_word
    except Exception as e:
        print("Lỗi: ", str(e))