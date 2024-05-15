import requests
import json

# ขั้นตอนที่ 1: ร้องขอรหัสผ่านเพิ่มเติมผ่านทางอีเมลหรือ SMS
def request_additional_password(username):
    endpoint = "https://login.microsoftonline.com/common/password/add"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": username
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("ร้องขอรหัสผ่านเพิ่มเติมสำเร็จ")
    else:
        print("การร้องขอรหัสผ่านเพิ่มเติมไม่สำเร็จ")

# ขั้นตอนที่ 2: ใช้รหัสผ่านเพิ่มเติมในการยืนยันตัวตนใน Microsoft Authenticator
def verify_with_additional_password(username, additional_password):
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
username = "your_username"
request_additional_password(username)

additional_password = input("กรุณาใส่รหัสผ่านเพิ่มเติมที่คุณได้รับ: ")
verify_with_additional_password(username, additional_password)
