from flask import Flask, jsonify, request
import sys
import os
sys.path.append(os.path.abspath('../'))
from inforeconnaissance.GetDataBBC import get_data_bbc
from inforeconnaissance.GetDataDantri import get_data_dantri
from inforeconnaissance.GetDataEvent import get_data_event
from inforeconnaissance.GetDataPage import get_data_page
from inforeconnaissance.GetDataPersonalPage import get_data_personal_page
from inforeconnaissance.GetDataTrendGoogle import get_data_trend_google
from inforeconnaissance.GetDataRFA import get_data_rfa
from inforeconnaissance.GetDataVietan import get_data_viettan
from inforeconnaissance.GetDataVnExpress import get_data_vnexpress
from inforeconnaissance.GetDataVoatiengviet import get_data_voatiengviet
from inforeconnaissance.GetDataChannel import get_data_channel
from inforeconnaissance.GetDataChannelLink import get_link_channel

sys.path.append(os.path.abspath('../'))
from textprocessing.DetectContent import detect_content

# Class data WEB=============================================================
class DataWeb:
    def __init__(self, tieude, duongdan, thoigiandang, camxuc):
        self.tieude = tieude
        self.duongdan = duongdan
        self.thoigiandang = thoigiandang
        self.camxuc = camxuc

    def to_dict(self):
        return {
            "tieude": self.tieude,
            "duongdan": self.duongdan,
            "thoigiandang": self.thoigiandang,
            "camxuc": self.camxuc
        }
        
def create_DataWeb(tieude, duongdan, thoigiandang, camxuc):
    dataweb = []
    for i in range(len(tieude)):
        dataweb.append(DataWeb(tieude[i], duongdan[i], thoigiandang[i], camxuc[i]))
    return dataweb

# # Class data Youtube=============================================================
class DataYoutubeChannelVideo:
    def __init__(self, tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo):
        self.tenvideo = tenvideo
        self.thoigianvideo = thoigianvideo
        self.anhdaidienvideo = anhdaidienvideo
        self.lienketvideo = lienketvideo
        self.thoigianluotxem = thoigianluotxem
        self.camxucvideo = camxucvideo

    def to_dict(self):
        return {
            "tenvideo": self.tenvideo,
            "thoigianvideo": self.thoigianvideo,
            "anhdaidienvideo": self.anhdaidienvideo,
            "lienketvideo": self.lienketvideo,
            "thoigianluotxem": self.thoigianluotxem,
            "camxucvideo": self.camxucvideo
        }
        
def create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo):
    datayoutubechannelvideo = []
    for i in range(len(tenvideo)):
        datayoutubechannelvideo.append(DataYoutubeChannelVideo(tenvideo[i], thoigianvideo[i], anhdaidienvideo[i], lienketvideo[i], thoigianluotxem[i], camxucvideo[i]))
    return datayoutubechannelvideo

# Class data Facebook=============================================================
class DataFacebookPagePersonal:
    def __init__(self, thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase):
        self.thoigiandangbai = thoigiandangbai
        self.noidungbai = noidungbai
        self.camxuc = camxuc
        self.soluongcamxuc = soluongcamxuc
        self.binhluanchiase = binhluanchiase

    def to_dict(self):
        return {
            "thoigiandangbai": self.thoigiandangbai,
            "noidungbai": self.noidungbai,
            "camxuc": self.camxuc,
            "soluongcamxuc": self.soluongcamxuc,
            "binhluanchiase": self.binhluanchiase
        }
        
def create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase):
    datafacebookpagepersonal = []
    for i in range(len(noidungbai)):
        datafacebookpagepersonal.append(DataFacebookPagePersonal(thoigiandangbai[i], thoigiandangbai[i], camxuc[i], soluongcamxuc[i], binhluanchiase[i]))
    return datafacebookpagepersonal

# Class data DataTrendGoogle=============================================================
class DataTrendGoogle:
    def __init__(self, tukhoaxuhuong, tieude, duongdan):
        self.tukhoaxuhuong = tukhoaxuhuong
        self.tieude = tieude
        self.duongdan = duongdan

    def to_dict(self):
        return {
            "tukhoaxuhuong": self.tukhoaxuhuong,
            "tieude": self.tieude,
            "duongdan": self.duongdan,
        }
        
def create_DataTrendGoogle(tukhoaxuhuong, tieude, duongdan):
    datatrendgoogle = []
    for i in range(len(tukhoaxuhuong)):
        datatrendgoogle.append(DataTrendGoogle(tukhoaxuhuong[i], tieude[i], duongdan[i]))
    return datatrendgoogle


# Class data DataTrendGoogle=============================================================
class DataEventGoogle:
    def __init__(self, tieude, duongdanbaiviet, logobaiviet):
        self.tieude = tieude
        self.duongdanbaiviet = duongdanbaiviet
        self.logobaiviet = logobaiviet

    def to_dict(self):
        return {
            "tieude": self.tieude,
            "duongdanbaiviet": self.duongdanbaiviet,
            "logobaiviet": self.logobaiviet
        }
        
def create_DataEventGoogle(tieude, duongdanbaiviet, logobaiviet):
    dataeventgoogle = []
    for i in range(len(tieude)):
        dataeventgoogle.append(DataEventGoogle(tieude[i], duongdanbaiviet[i], logobaiviet[i]))
    return dataeventgoogle

def GetDataWebDantri():
    try:
        linkWeb = "https://dantri.com.vn/xa-hoi/chinh-tri.htm"
        global data_content_from_Web
        data_content_from_Web = ''
        noidung = ''

        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        tieude, duongdan, thoigiandang, camxuc, noidung = get_data_dantri(linkWeb)

        datawebs = create_DataWeb(tieude, duongdan, thoigiandang, camxuc)
        data = [dataweb.to_dict() for dataweb in datawebs]
        
        data_content_from_Web += noidung
        
        print(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))

    
    
    
    
GetDataWebDantri()