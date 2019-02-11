import base64
import re
import requests
import json

AK = 'zWezr2iRFcxkw8DRSffdGBGv'
SK = 'F1aX3xAEQCLMa6kw5GGjofqjKATE3mgQ'
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + AK + '&client_secret=' + SK
request = requests.get(host)
# print(request.text)
content_json = json.loads(request.text)
access_token = content_json['access_token']
# print(access_token)

url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + access_token  # accurate_basic

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}
# img本地图片
f = open('D:\\Software\\pythonload\\' + 'image.png', 'rb')  # 二进制方式打开图文件
img = base64.b64encode(f.read())

body = {
    # "url":"https://img-blog.csdn.net/2018060214171639"
    "image": img
}

r = requests.post(url, data=body)
# print(r.text)
# r_json=json.loads(r.text)
# result=r_json["words_result"]
# print(result)
world = re.findall('"words": "(.*?)"}', str(r.text), re.S)
for each in world:
    print(each)
    last = re.sub('[^a-zA-Z_0-9]', '', each)
    print(last)

f.close()
