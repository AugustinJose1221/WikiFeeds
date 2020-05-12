import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("requests")
install("bs4")
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Portal:Current_events'
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')
text = soup.find_all(text=True)
text1 = ""
start = 0
end = 0
flag=0
for i in range(86,len(text)):

    if text[i]=="Portal":
        if flag==1:
            continue
        start=i
        flag = 1
    if text[i]=="Recent deaths":
        end = i
        break

text1 = text[(start+1):end]
t = ""
for i in text1:
    t += i
x = t.split("\n")
list = []
for j in x:
    if j!='':
        list.append(j)
list.pop(0)
for i in list:
    print(i)
'''
for i in range(1, len(list)):
    print(list[i])
'''
