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
