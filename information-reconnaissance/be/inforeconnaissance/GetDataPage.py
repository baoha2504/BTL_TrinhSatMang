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
# url = "https://web.facebook.com/viettan"


def get_link(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        # Đợi một khoảng thời gian để trang web tải hoàn tất (có thể cần điều chỉnh)
        time.sleep(3)
        
        try:
            # Tìm và click vào nút submit
            close_intro_button = driver.find_element(By.CSS_SELECTOR, 'div[class="x92rtbv x10l6tqk x1tk7jg1 x1vjfegm"]')
            close_intro_button.click()
            print("Đã click vào thẻ close")
        except Exception as e:
            print("Không tìm thấy thẻ close: ", e)
        
        
        name_pages = []
        flowlower_pages = []
        
        # Lấy tất cả các nội dung của thẻ a với class và id tương ứng
        name_page_elements = driver.find_elements(By.CSS_SELECTOR, 'h1[class="html-h1 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1vvkbs x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"]')
        for name_page_element in name_page_elements:
            name_pages.append(name_page_element)
            
        
        flowlower_page_elements = driver.find_elements(By.CSS_SELECTOR, 'span[class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xi81zsa"]')
        for flowlower_page_element in flowlower_page_elements:
            flowlower_pages.append(flowlower_page_element)
        
        
        tentrang = ''
        sotheodoi = ''

        for name_page, flowlower_video in zip(name_pages, flowlower_pages):
            # print("Tên trang FB:", name_page.text)
            # print("Số theo dõi FB:", flowlower_video.text)
            
            tentrang = name_page.text
            sotheodoi = flowlower_video.text
        
        return tentrang, sotheodoi

    finally:
        # Đóng trình duyệt sau khi hoàn thành công việc
        driver.quit()
        print("Thành công!")

def get_data_page(url):
    return get_link(url)