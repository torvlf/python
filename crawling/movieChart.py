import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

myparse = 'html.parser'
myurl = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = urlopen(myurl)

soup = BeautifulSoup(response, myparse)

thead_list = soup.select('table.list_ranking > thead > th')

theadlist = []
for th in thead_list:
    summary = th.find('td').text
    theadlist.append(summary)

print(thead_list)