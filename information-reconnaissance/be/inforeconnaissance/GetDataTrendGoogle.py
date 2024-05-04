

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




def get_link(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        # Đợi một khoảng thời gian để trang web tải hoàn tất (có thể cần điều chỉnh)
        time.sleep(3)
        current_time = datetime.now()
        formatted_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        print("Thời gian lấy dữ liệu: ", formatted_string)
        
        
        top_words = []
        titles = []
        links = []
        # Lấy tất cả các nội dung của thẻ a với class và id tương ứng
        top_word_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="title"]')
        for top_word_element in top_word_elements:
            top_words.append(top_word_element)
        
        
        title_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="summary-text"]')
        for title_element in title_elements:
            titles.append(title_element)
            
            link_elements = title_element.find_elements(By.CSS_SELECTOR, 'a')
            for link_element in link_elements:
                links.append(link_element)

        tukhoaxuhuong = []
        tieude = []
        duongdan = []
        count = 0
        for top_word, title, link in zip(top_words, titles, links):
            if count == 6:
                break
            else:
                count += 1
            # print("Xu hướng tìm kiếm:", top_word.text)
            # print("Tiêu đề:", title.text)
            # print("Link:", link.get_attribute('href'))
            
            tukhoaxuhuong.append(top_word.text[:15])
            tieude.append(title.text[:40])
            duongdan.append(link.get_attribute('href'))
            
        return tukhoaxuhuong, tieude, duongdan

    finally:
        # Đóng trình duyệt sau khi hoàn thành công việc
        driver.quit()
        print("Thành công!")

def get_data_trend_google():
    url = "https://trends.google.com.vn/trends/trendingsearches/daily?geo=VN&hl=vi"
    return get_link(url)