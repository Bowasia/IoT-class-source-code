import sys
import urllib.request

n = input("Enter your first name: ")
l = input("Enter your last name: ")

url = "http://iotkmitl.ddns.net/rai/Ornwara/sqltable/insert.php?name="+n+"_"+l

response = urllib.request.urlopen(url)

print("Insert "+n+" "+l+" to the table")
if (response.read().decode('utf-8')=="1"):
    print("Success")
else:
    print("Fail")
