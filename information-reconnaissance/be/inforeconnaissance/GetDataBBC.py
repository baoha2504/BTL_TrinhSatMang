import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://www.bbc.com/vietnamese"

def get_link(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm tất cả các thẻ a có class="dt-text-black-mine"
        links = soup.find_all('a', {"class": "focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0"})
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        noidung = ''
        
        # Lặp qua các thẻ a và in nội dung và href
        count = 0
        for link in links:
            if count == 10:
                break
            else:
                count += 1
            # print("Tiêu đề:", link.text)
            # print("Href:", link['href'])
            content, time = get_content(link['href'])
            # print("Thời gian: ", time)
            # print("Nội dung: ", content)
            
            tieude.append(link.text[:100])
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
        
        content_element = soup.find('div', {"class": "bbc-1cvxiy9"})
        content = content_element.text.strip() if content_element else ""
        
        time_element = soup.find('time', {"class": "bbc-j3wi5n e1mklfmt0"})
        time = time_element.text.strip() if time_element else ""
        
        return content, time
    else:
        return None, None
    
def get_data_bbc(url): 
    return get_link(url)
    
# get_data_bbc("https://www.bbc.com/vietnamese")