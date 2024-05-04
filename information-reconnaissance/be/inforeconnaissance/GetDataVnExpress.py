import requests
from bs4 import BeautifulSoup
import re
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://vnexpress.net/thoi-su/chinh-tri"

def remove_long_spaces(input_string):
    # Sử dụng regular expression để tìm và thay thế các khoảng trắng có độ dài lớn hơn 2
    output_string = re.sub(r'\s{3,}', '', input_string)
    return output_string

def get_link(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        divs = soup.find_all('div', {"class": "thumb-art"})
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        noidung = ''
        
        for div in divs:
            link = div.find('a', {"data-thumb": "1"})
            # print("Tiêu đề:", link['title'])
            # print("Href:", link['href'])
            content, time = get_content(link['href'])
            # print("Thời gian: ", time)
            # print("Nội dung: ", content)
            
            tieude.append(link['title'])
            duongdan.append(link['href'])
            thoigiandang.append(time)
            camxuc.append(detect_sentiment(content[:500]))
            noidung += content
        return tieude, duongdan, thoigiandang, camxuc, noidung
    else:
        print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)


def get_content(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content_element = soup.find('article', {"class": "fck_detail"})
        content = content_element.text.strip() if content_element else ""
        
        time_element = soup.find('span', {"class": "date"})
        time = time_element.text.strip() if time_element else ""
        
        return content, time
    else:
        return None, None
    
def get_data_vnexpress(url):    
    return get_link(url)