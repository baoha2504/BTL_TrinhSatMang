import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content
from textprocessing.DetectSentiment import detect_sentiment

# URL cần truy vấn
# url = "https://www.rfa.org/vietnamese/"

def get_link(url):
    # Gửi yêu cầu GET đến URL
    response = requests.get(url)

    # Kiểm tra xem yêu cầu có thành công không
    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        titles = []
        links_processing = []
        
        # Duyệt qua tất cả các phần tử span có class là "no_media"
        for title in soup.find_all('span', {"class": ["no_media", "has_audio"]}):
            # Lấy nội dung của tiêu đề và thêm vào mảng titles
            titles.append(title.text.strip())

        div_containers = soup.find_all('article', {"id": "content"})

        # Duyệt qua từng container div
        for div in div_containers:
            # Tìm tất cả các thẻ a trong div hiện tại
            links = div.find_all('a')
            for link in links:
                href = link.get('href')
                if href.startswith("https://www.rfa.org/vietnamese/") and href not in links_processing:
                    links_processing.append(href)
        
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        noidung = ''
        
        # Lặp qua các tiêu đề và in ra nội dung và href
        for title, link in zip(titles, links_processing):
            # print("Tiêu đề:", title)
            # print("Href:", link)
            content, time = get_content(link)
            # print("Thời gian: ", time)
            # print("Nội dung: ", content)
            
            tieude.append(title)
            duongdan.append(link)
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
        
        content_element = soup.find('div', {"id": "storytext"})
        content = content_element.text.strip() if content_element else ""
        
        time_element = soup.find('span', {"id": "story_date"})
        time = time_element.text.strip() if time_element else ""
        
        return content, time
    else:
        return None, None

def get_data_rfa(url):    
    return get_link(url)