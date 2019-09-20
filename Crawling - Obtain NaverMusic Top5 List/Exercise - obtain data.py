#내장 모듈
from urllib.request import *
import sys
import time

#외부 모듈
from bs4 import *
import matplotlib.pyplot as p

singerList2016=[]
singerList2017=[]
singerList2018=[]



for i in range(6,9):
    singerList=[]
    for j in range(1,13):
        web="https://music.naver.com/listen/history/index.nhn?type=TOTAL&year=201%d&month=%02d&week=0"%(i,j)
        wPage = urlopen(web)
        soup = BeautifulSoup(wPage, 'html.parser')
        
        trList1 = soup.find_all('tr',{'class':'_tracklist_move data1'})
        trList2 = soup.find_all('tr',{'class':'_tracklist_move data0'})

        singertotal1=[]
        for tr in trList1 :
            tdList = tr.find_all('td')
            singerr=tdList[4].get_text()
            #test=tdList[4].get_text()
            #print(singerr)
            singern=singerr.replace('\r','')
            singert=singern.replace('\n','')
            singer=singert.replace('\t','')
            singertotal1.append(singer)
        #print(singertotal1)

        singertotal2=[]
        for tr in trList2 :
            tdList = tr.find_all('td')
            singerr=tdList[4].get_text()
            #test=tdList[4].get_text()
            #print(singerr)
            singern=singerr.replace('\r','')
            singert=singern.replace('\n','')
            singer=singert.replace('\t','')
            singertotal2.append(singer)
        #print(singertotal2)
        
        #print[singertotal]
        for a in range(5):
            singerList.append(singertotal1[a])
            singerList.append(singertotal2[a])
        #singerList.pop()
                
        
        
        #print(singerList)
    if i==6:
        singerList2016=(singerList)
        print(singerList2016)
        print("~ to 2016")
    if i==7:
        singerList2017=(singerList)
        print(singerList2017)
        print("~ to 2017")
    if i==8:
        singerList2018=(singerList)
        print(singerList2018)
        print("~ to 2018")
        
singerList=[]
i=9
for j in range(1,7):
    web="https://music.naver.com/listen/history/index.nhn?type=TOTAL&year=201%d&month=%02d&week=0"%(i,j)
    wPage = urlopen(web)
    soup = BeautifulSoup(wPage, 'html.parser')
    
    trList1 = soup.find_all('tr',{'class':'_tracklist_move data1'})
    trList2 = soup.find_all('tr',{'class':'_tracklist_move data0'})

    singertotal1=[]
    for tr in trList1 :
        tdList = tr.find_all('td')
        singerr=tdList[4].get_text()
        #test=tdList[4].get_text()
        #print(singerr)
        singern=singerr.replace('\r','')
        singert=singern.replace('\n','')
        singer=singert.replace('\t','')
        singertotal1.append(singer)
    #print(singertotal1)

    singertotal2=[]
    for tr in trList2 :
        tdList = tr.find_all('td')
        singerr=tdList[4].get_text()
        #test=tdList[4].get_text()
        #print(singerr)
        singern=singerr.replace('\r','')
        singert=singern.replace('\n','')
        singer=singert.replace('\t','')
        singertotal2.append(singer)
    #print(singertotal2)
    
    #print[singertotal]
    for a in range(5):
        singerList.append(singertotal1[a])
        singerList.append(singertotal2[a])
    #singerList.pop()
singerList2019=singerList
print(singerList2019)
print("~ to 2019")    






