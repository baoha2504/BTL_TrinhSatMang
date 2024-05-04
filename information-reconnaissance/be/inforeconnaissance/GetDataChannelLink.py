

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import re
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment
sys.path.append(os.path.abspath('../'))
from audioprocessing.AudioToText import audio_to_text

# URL cần truy vấn
# url = "https://www.youtube.com/@VietTan/videos/"


def remove_long_spaces(input_string):
    # Sử dụng regular expression để tìm và thay thế các khoảng trắng có độ dài lớn hơn 2
    output_string = re.sub(r'\s{3,}', '', input_string)
    # Thay thế ký tự xuống dòng bằng khoảng trắng
    output_string = output_string.replace('\n', ' ')
    return output_string


def get_link(url):
    try:
        
        driver = webdriver.Chrome()
        driver.get(url + "videos")

        # Đợi một khoảng thời gian để trang web tải hoàn tất (có thể cần điều chỉnh)
        time.sleep(3)
        current_time = datetime.now()
        formatted_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        print("Thời gian lấy dữ liệu: ", formatted_string)
        
        # Cuộn xuống dưới trang để tải thêm nội dung
        for i in range(1):  # Cuộn 1 lần
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(3)  # Đợi để trang tải thêm nội dung
        
        name_videos = []
        time_videos = []
        thumbnail_videos = []
        link_videos = []
        date_and_view_number_videos = []
        
        # Lấy tất cả các nội dung của thẻ a với class và id tương ứng
        name_video_elements = driver.find_elements(By.CSS_SELECTOR, 'yt-formatted-string[id="video-title"]')
        for name_video_element in name_video_elements:
            name_videos.append(name_video_element)
        
        time_video_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="badge-shape-wiz__text"]')
        for time_video_element in time_video_elements:
            time_videos.append(time_video_element)
        
        thumbnail_video_elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="yt-core-image yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded"]') # lấy src
        for thumbnail_video_element in thumbnail_video_elements:
            thumbnail_videos.append(thumbnail_video_element)
            
        link_video_elements = driver.find_elements(By.CSS_SELECTOR, 'a[id="video-title-link"]') # lấy href
        for link_video_element in link_video_elements:
            link_videos.append(link_video_element)
            
        date_and_view_number_video_elements = driver.find_elements(By.CSS_SELECTOR, 'div[id="metadata"]')
        for date_and_view_number_video_element in date_and_view_number_video_elements:
            date_and_view_number_videos.append(date_and_view_number_video_element)

        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        noidung = ''
        count = 0
        for name_video, time_video, thumbnail_video, link_video, date_and_view_number_video in zip(name_videos, time_videos, thumbnail_videos, link_videos, date_and_view_number_videos):
            if count == 2:
                break
            else:
                count += 1
            # print("Tên video:", name_video.text)
            # print("Thời gian video:", time_video.text)
            # print("Link thumbnail:", thumbnail_video.get_attribute('src'))
            # print("Link video:", link_video.get_attribute('href'))
            # print("View-Date:", remove_long_spaces(date_and_view_number_video.text))
            
            tenvideo.append(name_video.text)
            thoigianvideo.append(time_video.text)
            anhdaidienvideo.append(thumbnail_video.get_attribute('src'))
            lienketvideo.append(link_video.get_attribute('href'))
            thoigianluotxem.append(remove_long_spaces(date_and_view_number_video.text))
            text = audio_to_text(link_video.get_attribute('href'))
            noidungvideo.append(text)
            if(text != 'Không có giọng nói'):
                camxucvideo.append(detect_sentiment(text[:500]))
            else:
                camxucvideo.append(detect_sentiment(tenvideo))
            
            noidung += text
            
        return tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung

    finally:
        # Đóng trình duyệt sau khi hoàn thành công việc
        driver.quit()
        print("Thành công!")

def get_link_channel(url):       
    return get_link(url)