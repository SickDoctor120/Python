import requests
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 定义请求的 URL
url = 'https://*.*.*.*:8443/TIEServerMgmt/performImportFileReputation.do'

# 定义请求头部
headers = {
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryX0tbTZOPEl7bCCNK',
    'Cookie': 'JSESSIONID=A652AD378B854EDDDC1163F25717CAF7.route1; orion.login.language="language:zh&country:CN"; JSESSIONIDSSO=072D8448DAB2F9CDC822C22026858CE4; orion.content.size="width:1829&height=867"'
}

# 生成时间戳
timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")

# 定义请求参数
data = {
    'orion.user.security.token': 'biLMyk4IghaZfV5a',
    'importReps': 'on',
    'filenameId': timestamp,
    'md5Id': '72ad3ccbc81ce60970e93b7bb2908688',
    'reputationLevelSel': '1'
}

# 构造请求体
body = ''
for key, value in data.items():
    body += f'------WebKitFormBoundaryX0tbTZOPEl7bCCNK\r\n'
    body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n'
    body += f'{value}\r\n'
body += f'------WebKitFormBoundaryX0tbTZOPEl7bCCNK--\r\n'

# 发送 POST 请求
response = requests.post(url, headers=headers,  data=body, verify=False)

# 输出响应结果
print(f'Response: {response.status_code}')
print(response.text)
