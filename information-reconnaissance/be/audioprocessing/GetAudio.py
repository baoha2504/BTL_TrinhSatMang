from __future__ import unicode_literals
import os
from pydub import AudioSegment
from urllib.parse import urlparse, parse_qs
from pytube import YouTube


def download_audio_from(url, name="temp.wav"):
    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        
        # Tạo đường dẫn đến thư mục audio
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio')

        # Kiểm tra nếu thư mục không tồn tại thì tạo mới
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Đường dẫn file đầy đủ
        wav_path = os.path.join(directory, name)

        stream.download(output_path=directory, filename=name)
        
        # Đọc file âm thanh bằng pydub
        audio = AudioSegment.from_file(wav_path)
        
        wav_processing_path = os.path.join(directory, wav_path.split('.')[0] + "ed.wav")
        # Chuyển đổi âm thanh sang định dạng PCM WAV
        audio.export(wav_processing_path, format="wav")
        print("Video đã được tải xuống thành công")
        
        os.remove(wav_path)


    except Exception as e:
        print("Đã xảy ra lỗi:", str(e))

def extract_youtube_video_url(url):

    parsed_url = urlparse(url)
    
    # Extract the video ID from the query parameters
    query_parameters = parse_qs(parsed_url.query)
    video_id = query_parameters.get('v')
    
    if video_id:
        return "https://www.youtube.com/watch?v=" + video_id[0]
    else:
        # Check if the URL directly contains the video ID
        path_components = parsed_url.path.split('/')
        if len(path_components) > 1 and path_components[1] == 'watch':
            return "https://www.youtube.com/watch?v=" + path_components[2]
    
    # If no video ID found
    return None

def get_audio(url):
    # url ='https://www.youtube.com/watch?v=ZkToD82OzsI'

    print("downloading %s"%extract_youtube_video_url(url))
    try:
        download_audio_from(extract_youtube_video_url(url))
    except Exception as e:
        print(f"An exception occurred: {e}")
        

        