import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://dantri.com.vn/xa-hoi/chinh-tri.htm"

def get_link(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm tất cả các thẻ a có class="dt-text-black-mine"
        links = soup.find_all('a', {"class": "dt-text-black-mine"})
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        noidung = ''
        
        count = 0
        # Lặp qua các thẻ a và in nội dung và href
        for link in links:
            if count == 10:
                break
            else:
                count += 1
            # print("Tiêu đề:", link.text)
            # print("Href:", "https://dantri.com.vn" + link['href'])
            content, time = get_content("https://dantri.com.vn" + link['href'])
            # print("Thời gian: ", time)
            # print("Nội dung: ", content)
            
            tieude.append(link.text)
            duongdan.append("https://dantri.com.vn" + link['href'])
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
        
        content_element = soup.find('div', {"class": "singular-content"})
        content = content_element.text.strip() if content_element else ""
        
        time_element = soup.find('time', {"class": "author-time"})
        time = time_element.text.strip() if time_element else ""
        
        return content, time
    else:
        return None, None

def get_data_dantri(url):   
    return get_link(url)
    
    
# print(get_data_dantri("https://dantri.com.vn/xa-hoi/chinh-tri.htm"))