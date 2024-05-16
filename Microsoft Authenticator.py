import os
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
 
# Replace with your SharePoint site URL, list title, and credentials
site_url = "https://ssigroups.sharepoint.com/sites/SSI-ITScouting-KnowledgeSharing/"
list_title = "CL1_S1007_Absence_Request"
username = "git@ssi-steel.com"
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