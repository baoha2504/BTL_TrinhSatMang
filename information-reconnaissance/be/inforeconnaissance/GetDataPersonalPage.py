from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://web.facebook.com/viettan"


def remove_long_spaces(input_string):
    # Sử dụng regular expression để tìm và thay thế các khoảng trắng có độ dài lớn hơn 2
    output_string = re.sub(r'\s{3,}', '', input_string)
    # Thay thế ký tự xuống dòng bằng khoảng trắng
    output_string = output_string.replace('\n', ' ')
    return output_string


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
        
        # Cuộn xuống dưới trang để tải thêm nội dung
        for i in range(3):  # Cuộn 3 lần
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(3)  # Đợi để trang tải thêm nội dung
        
        time.sleep(3)
        
        time_posts = []
        content_posts = []
        feeling_posts = []
        number_comment_share_posts = []
        
        # Lấy tất cả các nội dung của thẻ a với class và id tương ứng
        time_post_elements = driver.find_elements(By.CSS_SELECTOR, 'span[class="x4k7w5x x1h91t0o x1h9r5lt x1jfb8zj xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j"]')
        for time_post_element in time_post_elements:
            sub_span_time_post_element = time_post_element
            time_posts.append(sub_span_time_post_element)
            
            
        content_post_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="x1yx25j4 x13crsa5 x6x52a7 x1rxj1xn xxpdul3"]')
        for content_post_element in content_post_elements:
            content_posts.append(content_post_element)
            
        content_post_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a"]')
        for content_post_element in content_post_elements:
            content_posts.append(content_post_element)
        
        feeling_post_elements = driver.find_elements(By.CSS_SELECTOR, 'span[class="x1e558r4"]')
        for feeling_post_element in feeling_post_elements:
            feeling_posts.append(feeling_post_element)
            
        number_comment_share_post_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x1qjc9v5 xozqiw3 x1q0g3np xykv574 xbmpl8g x4cne27 xifccgj"]') 
        for number_comment_share_post_element in number_comment_share_post_elements:
            number_comment_share_posts.append(number_comment_share_post_element)
            

        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        noidung = ''
        
        
        for time_post, content_post, feeling_post, number_comment_share_post in zip(time_posts, content_posts, feeling_posts, number_comment_share_posts):
            # print("Thời gian đăng bài:", time_post.text)
            # print("Nội dung bài:", content_post.text)
            # print("Số lượng thả cảm xúc:", feeling_post.text)
            # print("Bình luận và chia sẻ:", remove_long_spaces(number_comment_share_post.text))
            
            if(time_post.text == ''):
                thoigiandangbai.append("Không xác định")
            else:
                thoigiandangbai.append(time_post.text)
            if(content_post.text == ''):
                noidungbai.append("Bài viết không có nội dung")
            else:
                noidungbai.append(content_post.text)
            camxuc.append(detect_sentiment(content_post.text[:500]))
            soluongcamxuc.append(feeling_post.text)
            binhluanchiase.append(number_comment_share_post.text)
            noidung += content_post.text
        return thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung

    finally:
        # Đóng trình duyệt sau khi hoàn thành công việc
        driver.quit()
        print("Thành công!")

    
def get_data_personal_page(url):
    return get_link(url)