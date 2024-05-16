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

from msal import PublicClientApplication

def get_token(client_id, tenant_id, username, password):
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = PublicClientApplication(client_id, authority=authority)
    result = app.acquire_token_by_username_password(username, password, scopes=["https://graph.microsoft.com/.default"])
    
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception(result.get("error_description"))

# ข้อมูลการตั้งค่า
client_id = "b39fa7365b0d4f0095bd25b49271daa7"  # ใส่ Client ID ที่ได้จากการลงทะเบียนแอปพลิเคชัน
tenant_id = "539e183a-2de4-4fef-8217-904f310d2199"  # Tenant ID
username = "git@ssi-steel.com"  # รับชื่อผู้ใช้งานผ่าน Input
password = "Password123"  # รับรหัสผ่านผ่าน Input

try:
    token = get_token(client_id, tenant_id, username, password)
    print("การยืนยันตัวตนสำเร็จ:", token)
except Exception as e:
    print("การยืนยันตัวตนไม่สำเร็จ:", str(e))