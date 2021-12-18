import requests,urllib3
from bs4 import BeautifulSoup
import ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#네이버 기사 가져오기 연습용


url='https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=104&oid=008&aid=0004684920'
h={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
ret= requests.get(url,verify=False,headers=h)
bs = BeautifulSoup(ret.content, 'html.parser')
title=bs.select('h3#articleTitle')[0].text
#print(title)


# response = requests.get("https://www.naver.com/",verify=False)
# data = response.content
# print(data)