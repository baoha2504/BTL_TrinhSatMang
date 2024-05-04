from flask import Flask, jsonify, request
from flask_cors import CORS
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
from inforeconnaissance.GetDataContent import get_data_content

import mysql.connector

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {"origins": ["http://localhost:3000", "http://192.168.43.107:3000"]}
})

data_content_from_Web = ''
data_content_from_Youtube = ''
data_content_from_Facebook = ''

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
    def __init__(self, tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo):
        self.tenvideo = tenvideo
        self.thoigianvideo = thoigianvideo
        self.anhdaidienvideo = anhdaidienvideo
        self.lienketvideo = lienketvideo
        self.thoigianluotxem = thoigianluotxem
        self.camxucvideo = camxucvideo
        self.noidungvideo = noidungvideo

    def to_dict(self):
        return {
            "tenvideo": self.tenvideo,
            "thoigianvideo": self.thoigianvideo,
            "anhdaidienvideo": self.anhdaidienvideo,
            "lienketvideo": self.lienketvideo,
            "thoigianluotxem": self.thoigianluotxem,
            "camxucvideo": self.camxucvideo,
            "noidungvideo": self.noidungvideo
        }
        
def create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo):
    datayoutubechannelvideo = []
    for i in range(len(tenvideo)):
        datayoutubechannelvideo.append(DataYoutubeChannelVideo(tenvideo[i], thoigianvideo[i], anhdaidienvideo[i], lienketvideo[i], thoigianluotxem[i], camxucvideo[i], noidungvideo[i]))
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
        datafacebookpagepersonal.append(DataFacebookPagePersonal(thoigiandangbai[i], noidungbai[i], camxuc[i], soluongcamxuc[i], binhluanchiase[i]))
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
    def __init__(self, tieude, duongdanbaiviet, logobaiviet, camxuc):
        self.tieude = tieude
        self.duongdanbaiviet = duongdanbaiviet
        self.logobaiviet = logobaiviet
        self.camxuc = camxuc

    def to_dict(self):
        return {
            "tieude": self.tieude,
            "duongdanbaiviet": self.duongdanbaiviet,
            "logobaiviet": self.logobaiviet,
            "camxuc": self.camxuc
        }
        
def create_DataEventGoogle(tieude, duongdanbaiviet, logobaiviet, camxuc):
    dataeventgoogle = []
    for i in range(len(tieude)):
        dataeventgoogle.append(DataEventGoogle(tieude[i], duongdanbaiviet[i], logobaiviet[i], camxuc[i]))
    return dataeventgoogle

# GET DATA NEWS, YOUTUBE, FACEBOOK
# GET DATA BBC=============================================================
@app.route('/api/GetDataWebBBC', methods=['GET'])
def GetDataWebBBC():
    try:
        linkWeb = "https://www.bbc.com/vietnamese/"
        global data_content_from_Web
        data_content_from_Web = ''
        noidung = ''
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        
        tieude, duongdan, thoigiandang, camxuc, noidung = get_data_bbc(linkWeb)
        data_content_from_Web += noidung

        datawebs = create_DataWeb(tieude, duongdan, thoigiandang, camxuc)
        data = [dataweb.to_dict() for dataweb in datawebs]
        
        return jsonify(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))
        
    
@app.route('/api/GetDataYoutubeChannelBBC', methods=['GET'])
def GetDataYoutubeChannelBBC():
    try:
        linkYoutube = "https://www.youtube.com/@bbctiengviet/"
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
    
@app.route('/api/GetDataYoutubeChannelVideoBBC', methods=['GET'])
def GetDataYoutubeChannelVideoBBC():
    try:
        linkYoutube = "https://www.youtube.com/@bbctiengviet/"
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''
        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
        
    
@app.route('/api/GetDataFacebookPageBBC', methods=['GET'])
def GetDataFacebookPageBBC():
    try:
        linkFacebook = "https://web.facebook.com/BBCnewsVietnamese/"
        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
        

@app.route('/api/GetDataFacebookPagePersonalBBC', methods=['GET'])
def GetDataFacebookPagePersonalBBC():
    try:
        linkFacebook = "https://web.facebook.com/BBCnewsVietnamese/"
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_personal_page(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
        

# GET DATA DANTRI=============================================================
@app.route('/api/GetDataWebDantri', methods=['GET'])
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
        
        return jsonify(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))
    
@app.route('/api/GetDataYoutubeChannelDantri', methods=['GET'])
def GetDataYoutubeChannelDantri():
    try:
        linkYoutube = ""
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
    
@app.route('/api/GetDataYoutubeChannelVideoDantri', methods=['GET'])
def GetDataYoutubeChannelVideoDantri():
    try:
        linkYoutube = ""
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''
        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
    
@app.route('/api/GetDataFacebookPageDantri', methods=['GET'])
def GetDataFacebookPageDantri():
    try:
        linkFacebook = ""
        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))
    
@app.route('/api/GetDataFacebookPagePersonalDantri', methods=['GET'])
def GetDataFacebookPagePersonalDantri():
    try:
        linkFacebook = ""
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_personal_page(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))


# GET DATA RFA=============================================================
@app.route('/api/GetDataWebRFA', methods=['GET'])
def GetDataWebRFA():
    try:
        linkWeb = "https://www.rfa.org/vietnamese/"
        global data_content_from_Web
        data_content_from_Web = ''
        noidung = ''
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        tieude, duongdan, thoigiandang, camxuc, noidung = get_data_rfa(linkWeb)

        datawebs = create_DataWeb(tieude, duongdan, thoigiandang, camxuc)
        data = [dataweb.to_dict() for dataweb in datawebs]
        
        data_content_from_Web += noidung
        
        return jsonify(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelRFA', methods=['GET'])
def GetDataYoutubeChannelRFA():
    try:
        linkYoutube = "https://www.youtube.com/@rfavietnamese/"
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVideoRFA', methods=['GET'])
def GetDataYoutubeChannelVideoRFA():
    try:
        linkYoutube = "https://www.youtube.com/@rfavietnamese/"
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''
        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPageRFA', methods=['GET'])
def GetDataFacebookPageRFA():
    try:
        linkFacebook = "https://web.facebook.com/RFAVietnam"
        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPagePersonalRFA', methods=['GET'])
def GetDataFacebookPagePersonalRFA():
    try:
        linkFacebook = "https://web.facebook.com/RFAVietnam"
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_personal_page(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))


# GET DATA VIETTAN=============================================================
@app.route('/api/GetDataWebViettan', methods=['GET'])
def GetDataWebViettan():
    try:
        linkWeb = "https://viettan.org/"
        global data_content_from_Web
        data_content_from_Web = ''
        noidung = ''
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        tieude, duongdan, thoigiandang, camxuc, noidung = get_data_viettan(linkWeb)

        datawebs = create_DataWeb(tieude, duongdan, thoigiandang, camxuc)
        data = [dataweb.to_dict() for dataweb in datawebs]
        
        data_content_from_Web += noidung
        
        return jsonify(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelViettan', methods=['GET'])
def GetDataYoutubeChannelViettan():
    try:
        linkYoutube = "https://www.youtube.com/@VietTan/"
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVideoViettan', methods=['GET'])
def GetDataYoutubeChannelVideoViettan():
    try:
        linkYoutube = "https://www.youtube.com/@VietTan/"
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''

        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPageViettan', methods=['GET'])
def GetDataFacebookPageViettan():
    try:
        linkFacebook = "https://web.facebook.com/viettan"
        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPagePersonalViettan', methods=['GET'])
def GetDataFacebookPagePersonalViettan():
    try:
        linkFacebook = "https://web.facebook.com/viettan"
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_personal_page(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

# GET DATA VNEXPRESS=============================================================
@app.route('/api/GetDataWebVnexpress', methods=['GET'])
def GetDataWebVnexpress():
    try:
        linkWeb = "https://vnexpress.net/thoi-su/chinh-tri"
        global data_content_from_Web
        data_content_from_Web = ''
        noidung = ''
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        tieude, duongdan, thoigiandang, camxuc, noidung = get_data_vnexpress(linkWeb)

        datawebs = create_DataWeb(tieude, duongdan, thoigiandang, camxuc)
        data = [dataweb.to_dict() for dataweb in datawebs]
        
        data_content_from_Web += noidung
        
        return jsonify(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVnexpress', methods=['GET'])
def GetDataYoutubeChannelVnexpress():
    try:
        linkYoutube = ""
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVideoVnexpress', methods=['GET'])
def GetDataYoutubeChannelVideoVnexpress():
    try:
        linkYoutube = ""
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''
        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPageVnexpress', methods=['GET'])
def GetDataFacebookPageVnexpress():
    try:
        linkFacebook = ""
        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPagePersonalVnexpress', methods=['GET'])
def GetDataFacebookPagePersonalVnexpress():
    try:
        linkFacebook = ""
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_personal_page(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))


# GET DATA VOA TIENGVIET=============================================================
@app.route('/api/GetDataWebVoatiengviet', methods=['GET'])
def GetDataWebVoatiengviet():
    try:
        linkWeb = "https://www.voatiengviet.com/p/6159.html"
        global data_content_from_Web
        data_content_from_Web = ''
        noidung = ''
        
        tieude = []
        duongdan = []
        thoigiandang = []
        camxuc = []
        tieude, duongdan, thoigiandang, camxuc, noidung = get_data_voatiengviet(linkWeb)

        datawebs = create_DataWeb(tieude, duongdan, thoigiandang, camxuc)
        data = [dataweb.to_dict() for dataweb in datawebs]
        
        data_content_from_Web += noidung
        
        return jsonify(data)
    
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVoatiengviet', methods=['GET'])
def GetDataYoutubeChannelVoatiengviet():
    try:
        linkYoutube = "https://www.youtube.com/@VOATiengViet/"
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVideoVoatiengviet', methods=['GET'])
def GetDataYoutubeChannelVideoVoatiengviet():
    try:
        linkYoutube = "https://www.youtube.com/@VOATiengViet/"
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''

        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPageVoatiengviet', methods=['GET'])
def GetDataFacebookPageVoatiengviet():
    try:
        linkFacebook = "https://web.facebook.com/VOATiengViet"
        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPagePersonalVoatiengviet', methods=['GET'])
def GetDataFacebookPagePersonalVoatiengviet():
    try:
        linkFacebook = "https://web.facebook.com/VOATiengViet"
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_personal_page(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))


# GET DATA OTHER SOUCES=============================================
@app.route('/api/GetDataYoutubeChannelOtherSources', methods=['GET'])
def GetDataYoutubeChannelOtherSources():
    try:
        linkYoutube = request.args.get('linkYoutube')
        if linkYoutube is None:
            return jsonify({"error": "Thiếu tham số 'linkYoutube'"}), 400
        tenkenh, sodangky, sovideo = get_data_channel(linkYoutube)
        # print(get_data_channel(linkYoutube))
        data = {
            "tenkenh": tenkenh,
            "sodangky": sodangky,
            "sovideo": sovideo
        }
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataYoutubeChannelVideoOtherSources', methods=['GET'])
def GetDataYoutubeChannelVideoOtherSources():
    try:
        linkYoutube = request.args.get('linkYoutube')
        if linkYoutube is None:
            return jsonify({"error": "Thiếu tham số 'linkYoutube'"}), 400
        
        global data_content_from_Youtube
        data_content_from_Youtube = ''
        noidung = ''
        
        tenvideo = []
        thoigianvideo = []
        anhdaidienvideo = []
        lienketvideo = []
        thoigianluotxem = []
        camxucvideo = []
        noidungvideo = []
        
        tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo, noidung = get_link_channel(linkYoutube)
        
        datayoutubechannelvideos = create_DataYoutubeChannelVideo(tenvideo, thoigianvideo, anhdaidienvideo, lienketvideo, thoigianluotxem, camxucvideo, noidungvideo)
        data = [datayoutubechannelvideo.to_dict() for datayoutubechannelvideo in datayoutubechannelvideos]
        
        data_content_from_Youtube += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPageOtherSources', methods=['GET'])
def GetDataFacebookPageOtherSources():
    try:
        linkFacebook = request.args.get('linkFacebook')
        if linkFacebook is None:
            return jsonify({"error": "Thiếu tham số 'linkFacebook'"}), 400

        tentrang, sotheodoi = get_data_page(linkFacebook)
        
        data = {
            "tentrang": tentrang,
            "sotheodoi": sotheodoi
        }

        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataFacebookPagePersonalOtherSources', methods=['GET'])
def GetDataFacebookPagePersonalOtherSources():
    try:
        linkFacebook = request.args.get('linkFacebook')
        if linkFacebook is None:
            return jsonify({"error": "Thiếu tham số 'linkFacebook'"}), 400
        
        global data_content_from_Facebook
        data_content_from_Facebook = ''
        noidung = ''
        
        thoigiandangbai = []
        noidungbai = []
        camxuc = []
        soluongcamxuc = []
        binhluanchiase = []
        
        thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase, noidung = get_data_trend_google(linkFacebook)

        datafacebookpagepersonals = create_DataFacebookPagePersonal(thoigiandangbai, noidungbai, camxuc, soluongcamxuc, binhluanchiase)
        data = [datafacebookpagepersonal.to_dict() for datafacebookpagepersonal in datafacebookpagepersonals]
        
        data_content_from_Facebook += noidung
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))


# API GET TOP WORD=============================================================
@app.route('/api/GetDataTopWordWeb', methods=['GET'])
def GetDataTopWordWeb():
    try:
        global data_content_from_Web
        
        top_6_word = []
        top_6_word = get_data_content(data_content_from_Web)
        
        return jsonify(top_6_word)
    except Exception as e:
        print("Lỗi: ", str(e))
        
@app.route('/api/GetDataTopWordYoutube', methods=['GET'])
def GetDataTopWordYoutube():
    try:
        global data_content_from_Youtube
        
        top_6_word = []
        top_6_word = get_data_content(data_content_from_Youtube)
        
        return jsonify(top_6_word)
    except Exception as e:
        print("Lỗi: ", str(e))
        
@app.route('/api/GetDataTopWordFacebook', methods=['GET'])
def GetDataTopWordFacebook():
    try:
        global data_content_from_Facebook
        
        top_6_word = []
        top_6_word = get_data_content(data_content_from_Facebook)
        
        return jsonify(top_6_word)
    except Exception as e:
        print("Lỗi: ", str(e))


# API GET DATA GOOGLE=============================================================
@app.route('/api/GetDataTrendInGoogle', methods=['GET'])
def GetDataTrendInGoogle():
    try:        
        tukhoaxuhuong = []
        tieude = []
        duongdan = []
        
        tukhoaxuhuong, tieude, duongdan = get_data_trend_google()

        datatrendgoogles = create_DataTrendGoogle(tukhoaxuhuong, tieude, duongdan)
        data = [datatrendgoogle.to_dict() for datatrendgoogle in datatrendgoogles]
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))

@app.route('/api/GetDataEventInGoogle', methods=['GET'])
def GetDataEventInGoogle():
    try:
        event = request.args.get('event')
        if event is None:
            return jsonify({"error": "Thiếu tham số 'event'"}), 400
        
        tieude = []
        duongdanbaiviet = []
        logobaiviet = []
        camxuc = []
        
        tieude, duongdanbaiviet, logobaiviet, camxuc = get_data_event(event)

        dataeventgoogles = create_DataEventGoogle(tieude, duongdanbaiviet, logobaiviet, camxuc)
        data = [dataeventgoogle.to_dict() for dataeventgoogle in dataeventgoogles]
        
        return jsonify(data)
    except Exception as e:
        print("Lỗi: ", str(e))


# API GET DATA TABLE OBJECTS AND EVENTS=============================================================
@app.route('/api/GetAllDoituong', methods=['GET'])
def GetAllDoituong():
    # Kết nối đến MySQL
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",  # Thay username bằng tên đăng nhập của bạn
        # password="password",  # Thay password bằng mật khẩu của bạn
        database="trinhsatthongtin"  # Thay databasename bằng tên cơ sở dữ liệu bạn muốn truy cập
    )

    cursor = connection.cursor()

    try:
        # Truy vấn để lấy tất cả dữ liệu từ bảng "object"
        cursor.execute("SELECT * FROM object")

        # Lấy tất cả các dòng dữ liệu từ kết quả của truy vấn
        rows = cursor.fetchall()

        # Chuyển đổi kết quả thành danh sách các từ điển
        results = []
        for row in rows:
            result = {
                "id": row[0],
                "name": row[1],
                "linkWeb": row[2],
                "linkYoutube": row[3],
                "linkFacebook": row[4],
                # Thêm các trường khác nếu cần
            }
            results.append(result)

        return jsonify(results)

    except mysql.connector.Error as error:
        print("Error:", error)
        return jsonify({"error": str(error)}), 500

    finally:
        # Đóng kết nối
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/GetAllSukienTheodoi', methods=['GET'])
def GetAllSukienTheodoi():
    # Kết nối đến MySQL
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",  # Thay username bằng tên đăng nhập của bạn
        # password="password",  # Thay password bằng mật khẩu của bạn
        database="trinhsatthongtin"  # Thay databasename bằng tên cơ sở dữ liệu bạn muốn truy cập
    )

    cursor = connection.cursor()

    try:
        # Truy vấn để lấy tất cả dữ liệu từ bảng "object"
        cursor.execute("SELECT * FROM events")

        # Lấy tất cả các dòng dữ liệu từ kết quả của truy vấn
        rows = cursor.fetchall()

        # Chuyển đổi kết quả thành danh sách các từ điển
        results = []
        for row in rows:
            result = {
                "id": row[0],
                "eventname": row[1],
            }
            results.append(result)

        return jsonify(results)

    except mysql.connector.Error as error:
        print("Error:", error)
        return jsonify({"error": str(error)}), 500

    finally:
        # Đóng kết nối
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)