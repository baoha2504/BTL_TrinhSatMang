

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://www.youtube.com/@VietTan/"



def get_link(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        # Đợi một khoảng thời gian để trang web tải hoàn tất (có thể cần điều chỉnh)
        time.sleep(3)
        current_time = datetime.now()
        formatted_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        print("Thời gian lấy dữ liệu: ", formatted_string)
        
        # Lấy tất cả các nội dung của thẻ a với class và id tương ứng
        name_channel = driver.find_element(By.CSS_SELECTOR, 'yt-formatted-string[id="text"]')

        count_subscriber = driver.find_element(By.CSS_SELECTOR, 'yt-formatted-string[id="subscriber-count"]')

        count_video = driver.find_element(By.CSS_SELECTOR, 'span[class="style-scope yt-formatted-string"]')

        name = name_channel.text
        countsubscriber = count_subscriber.text.replace('subscribers', '')
        countvideo = count_video.text
        # print("Tên kênh:", name)
        # print("Số đăng ký:", countsubscriber)
        # print("Số video:", countvideo)
        
        return name, countsubscriber, countvideo

    finally:
        # Đóng trình duyệt sau khi hoàn thành công việc
        driver.quit()
        print("Thành công!")

def get_data_channel(url):    
    return get_link(url)
