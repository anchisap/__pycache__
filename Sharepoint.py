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


import os
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
 
# Replace with your SharePoint site URL, list title, and credentials
site_url = "https://ssigroups.sharepoint.com/sites/SSI-ITScouting-KnowledgeSharing/"
list_title = "CL1_S1007_Absence_Request"
username = "git"
password = "Password123"
 
ctx_auth = AuthenticationContext(site_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(site_url, ctx_auth)
    web = ctx.web
    sp_list = web.lists.get_by_title(list_title)
 
    # Get list items (replace with desired query or actions)
    items = sp_list.get_items().top(10)  # Fetch top 10 items
    ctx.load(items)
    ctx.execute_query()
 
    for item in items:
        print(item.properties["Title"])  # Access list item properties
else:
    print("Authentication failed: ", ctx_auth.get_last_error())