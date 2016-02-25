# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:10:39 2016

@author: miaopeng
"""
import csv
import requests
from bs4 import BeautifulSoup
mylist = []
rank=0
print('Top250 :\n Movie Name \t Description\t Rating')
def crawl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text)
    for tag in soup.select('.info'):
        try:
            m_name= tag.select('.title')[1].text.replace("/",'')
        except:
            m_name="Null"
        try:
            m_rating_num= tag.select('p')[0].text
        except:
            pass
        try:
            m_comments  =tag.select('.rating_num')[0].text
        except:
            pass
        else:
            #print("%s %s %s " % (m_name, m_comments, m_rating_num))
            mylist.append(( m_name,  m_rating_num, m_comments))
           
 
pagenumber = []
for i in range(10):
    page_number = 25*i
    pagenumber.append(page_number)
pagelist = list(map(str, pagenumber))
#pagelist=['0','25','50','75','100','125','150','175','200','225']
 
BASE_URL = 'http://movie.douban.com/top250?start='
LAST_URL = '&filter=&type='
for url in [ BASE_URL + MID_URL + LAST_URL for MID_URL in pagelist ]:
    crawl(url)
 
import tablib
headers = ( 'Movie Name', 'Description', 'Rating')
mylist = tablib.Dataset(*mylist, headers=headers)
print(mylist.csv)
fileHandle = open('DoubanMoviesTop250.txt','w')
fileHandle.write(str(mylist.csv))
fileHandle.close()


    