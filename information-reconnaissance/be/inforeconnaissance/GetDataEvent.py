from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment
import time


# Khởi tạo trình duyệt Chrome


def transfer_text_to_link(text):
    link = 'https://www.google.com/search?q=' + text.replace(' ', '+')
    return link


def click_more_results(driver):
    more_results_elements = driver.find_elements(By.CSS_SELECTOR, 'div.GNJvt.ipz2Oe')
    
    for more_results_element in more_results_elements:
        # Sử dụng JavaScript để click thay vì Selenium
        driver.execute_script("arguments[0].click();", more_results_element)
        print("Đã click vào nút 'More results'")

def get_url(text):
    try:
        driver = webdriver.Chrome()
        driver.get(transfer_text_to_link(text))

        # Đợi một khoảng thời gian để trang web tải hoàn tất (có thể cần điều chỉnh)
        time.sleep(3)
        
        # Cuộn xuống dưới trang để tải thêm nội dung
        for i in range(2):  # Cuộn 3 lần
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(3)  # Đợi để trang tải thêm nội dung
            click_more_results(driver)
        
        
        links = []
        news_titles = []
        images = []
        
        tieude = []
        duongdanbaiviet = []
        logobaiviet = []
        camxuc = []
        
        link_elements = driver.find_elements(By.CSS_SELECTOR, 'a[jsname="UWckNb"]')
        for link_element in link_elements:
            links.append(link_element)
            
        news_title_elements = driver.find_elements(By.CSS_SELECTOR, 'h3[class="LC20lb MBeuO DKV0Md"]')
        for news_title_element in news_title_elements:
            news_titles.append(news_title_element)
    
        image_elements = driver.find_elements(By.CSS_SELECTOR, 'img[class="XNo5Ab"]')
        for image_element in image_elements:
            images.append(image_element)

        for news_title, link, image in zip(news_titles, links, images):
            # print("Tiêu đề:", news_title.text)
            # print("Href:", link.get_attribute('href'))
            # print("Ảnh:", image.get_attribute('src'))
            
            tieude.append(news_title.text)
            duongdanbaiviet.append(link.get_attribute('href'))
            logobaiviet.append(image.get_attribute('src'))
            camxuc.append(detect_sentiment(news_title.text))
        
        return tieude, duongdanbaiviet, logobaiviet, camxuc

    finally:
        # Đóng trình duyệt sau khi hoàn thành công việc
        driver.quit()
        print("Thành công!")

def get_data_event(text): 
    return get_url(text)