import requests
from bs4 import BeautifulSoup
import re
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://www.voatiengviet.com/p/6159.html"

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
        
        divs = soup.find_all('div', {"class": ["media-block__content media-block__content--h", "media-block__content"]})
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        noidung = ''

        for div in divs:
            link = div.find('a')
        
            # print("Tiêu đề:", remove_long_spaces(div.text))
            # print("Href:", "https://www.voatiengviet.com" + link['href'])
            content, time = get_content("https://www.voatiengviet.com" + link['href'])
            # print("Thời gian: ", time)
            # print("Nội dung: ", content)
            
            tieude.append(remove_long_spaces(div.text))
            duongdan.append("https://www.voatiengviet.com" + link['href'])
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
        
        content_element = soup.find('div', {"class": ["wsw", "intro m-t-md"]})
        content = content_element.text.strip() if content_element else ""
        content_processing = remove_long_spaces(content)
        time_element = soup.find('span', {"class": "date"})
        time = time_element.text.strip() if time_element else ""
        
        return content_processing, time
    else:
        return None, None
    
    
def get_data_voatiengviet(url):
    return get_link(url)