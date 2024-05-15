from shareplum import Site, office365
from shareplum.site import Version

import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_filename = 'config.json'
config_path = os.path.join(ROOT_DIR, config_filename)

# อ่านข้อมูลการเข้าสู่ SharePoint จากไฟล์ config.json
with open(config_path, encoding='utf-8') as config_file:
    config = json.load(config_file)
    config = config['share_point']

USERNAME = config['user']
PASSWORD = config['password']
SHAREPOINT_URL = config['url']
SHAREPOINT_SITE = config['site']

class SharePoint:
    def auth(self):
        self.authcookie = office365.Office365(
            SHAREPOINT_URL,
            username=USERNAME,
            password=PASSWORD,
        ).GetCookies()
        self.site = Site(
            SHAREPOINT_SITE,
            version=Version.v365,
            authcookie=self.authcookie,
        )
        return self.site
    
    def connect_to_list(self, list_name):
        self.auth_site = self.auth()
        list_data = self.auth_site.List(list_name=list_name).GetListItems()
        return list_data



import requests
import json

# ขั้นตอนที่ 1: ร้องขอรหัสผ่านเพิ่มเติมผ่านทางอีเมลหรือ SMS
def request_additional_password(AnchisaP):
    endpoint = "https://login.microsoftonline.com/common/password/add"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": AnchisaP
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("ร้องขอรหัสผ่านเพิ่มเติมสำเร็จ")
    else:
        print("การร้องขอรหัสผ่านเพิ่มเติมไม่สำเร็จ")

# ขั้นตอนที่ 2: ใช้รหัสผ่านเพิ่มเติมในการยืนยันตัวตนใน Microsoft Authenticator
def verify_with_additional_password(Anchisa P, additional_password):
    endpoint = "https://login.microsoftonline.com/common/password/verify"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": username,
        "additional_password": additional_password
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("การยืนยันตัวตนผ่าน Microsoft Authenticator เสร็จสิ้น")
    else:
        print("การยืนยันตัวตนผ่าน Microsoft Authenticator ไม่สำเร็จ")

# การใช้งาน
username = "Anchisa P"
request_additional_password(username)

additional_password = input("กรุณาใส่รหัสผ่านเพิ่มเติมที่คุณได้รับ: ")
verify_with_additional_password(username, additional_password) 