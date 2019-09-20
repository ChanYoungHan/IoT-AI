#내장 모듈
from urllib.request import *
import sys
import time
from operator import itemgetter, attrgetter

#외부 모듈
from bs4 import *
import matplotlib.pyplot as p
import matplotlib.font_manager as fm

singerList2016=[]
singerList2017=[]
singerList2018=[]


############## 전년도까지 Data crawling ###############

for i in range(6,9):    # range 범위값을 통해 crawling 범위 조정
    singerList=[]
    for j in range(1,13):
        web="https://music.naver.com/listen/history/index.nhn?type=TOTAL&year=201%d&month=%02d&week=0"%(i,j)
        wPage = urlopen(web)
        soup = BeautifulSoup(wPage, 'html.parser')
        
        trList1 = soup.find_all('tr',{'class':'_tracklist_move data1'})
        trList2 = soup.find_all('tr',{'class':'_tracklist_move data0'})

        # 홀수 순위 data 획득
        singertotal1=[]
        for tr in trList1 :
            tdList = tr.find_all('td')
            singerr=tdList[4].get_text()

            singern=singerr.replace('\r','')
            singert=singern.replace('\n','')
            singer=singert.replace('\t','')
            singertotal1.append(singer)

        # 짝수 순위 data 획득
        singertotal2=[]
        for tr in trList2 :
            tdList = tr.find_all('td')
            singerr=tdList[4].get_text()
            singern=singerr.replace('\r','')
            singert=singern.replace('\n','')
            singer=singert.replace('\t','')
            singertotal2.append(singer)

        
        for a in range(5):
            singerList.append(singertotal1[a])
            singerList.append(singertotal2[a])
                
        
    # 현재(2019년)을 제외한 순위권 가수를 list에 기록       
    if i==6:
        singerList2016=(singerList)

    if i==7:
        singerList2017=(singerList)

    if i==8:
        singerList2018=(singerList)


############## 2019년 6월 까지 Data crawling ###############        
singerList=[]
i=9
for j in range(1,7):    # range 범위값을 통해 crawling 범위 조정(1개월 단위)
    web="https://music.naver.com/listen/history/index.nhn?type=TOTAL&year=201%d&month=%02d&week=0"%(i,j)
    wPage = urlopen(web)
    soup = BeautifulSoup(wPage, 'html.parser')
    
    trList1 = soup.find_all('tr',{'class':'_tracklist_move data1'})
    trList2 = soup.find_all('tr',{'class':'_tracklist_move data0'})

    singertotal1=[]
    for tr in trList1 :
        tdList = tr.find_all('td')
        singerr=tdList[4].get_text()

        singern=singerr.replace('\r','')
        singert=singern.replace('\n','')
        singer=singert.replace('\t','')
        singertotal1.append(singer)


    singertotal2=[]
    for tr in trList2 :
        tdList = tr.find_all('td')
        singerr=tdList[4].get_text()

        singern=singerr.replace('\r','')
        singert=singern.replace('\n','')
        singer=singert.replace('\t','')
        singertotal2.append(singer)
    

# range 범위값의 2배만큼의 순위(rank)까지 data 획득
    for a in range(5):  
        singerList.append(singertotal1[a])
        singerList.append(singertotal2[a])

singerList2019=singerList

#<- 찬영
#Soon_->

# 크롤링 데이터 결과를 한개의 리스트로

Slist = list()
Slist.append(singerList2016)
Slist.append(singerList2017)
Slist.append(singerList2018)
Slist.append(singerList2019)


result = list()
sumdict = dict()
yeardict = dict()


# 결과 리스트에 2016년도 부터 차례대로 dictionary로 넣어준다.

for i in range(len(Slist)):

    yeardict.clear()

    for j in range(len(Slist[i])):
        if yeardict.get(Slist[i][j]) == None:
            yeardict.update({Slist[i][j]:1})    

        else:
            yeardict[Slist[i][j]] += 1
    
        if sumdict.get(Slist[i][j]) == None:
            sumdict.update({Slist[i][j]:1})
        else:
            sumdict[Slist[i][j]] += 1
        
    result.append(yeardict.copy())

result.append(sumdict)

# 임시 변수에 dictionary 내림차순 정렬 해준다.

temp = sorted(sumdict.items(), key=itemgetter(1), reverse = True)

# font, graph color, 가수 별로 list화 

font_path='C:\\Users\\Soon\\Desktop\\sba아카데미\\크롤링\\Nanumsquare_ac_TTF\\Nanumsquare_ac_TTF\\NanumSquare_acL.ttf'
fontprop1 = fm.FontProperties(fname=font_path, size=18)
fontprop2 = fm.FontProperties(fname=font_path, size=10)

xAxis = list(range(2016 , 2020)) 
xAxis.append("result")

templist = list()
ranklist = list()
colorlist = ['red','orangered','yellow','lime','green','aqua','blue','navy','purple','black']


# 선 그리기

for i in range(10):

    templist.clear()
    for j in range(5):

        if result[j].get(temp[i][0]) == None:
            templist.append(0)
        else:
            templist.append(result[j].get(temp[i][0]))
    ranklist.append(templist.copy())
    p.plot (xAxis, ranklist[i],  colorlist[i], label = temp[i][0])        


#그래프의 레이블 및 비주얼 효과 생성
    
p.title('kpop 인기가수는 누구?',fontproperties=fontprop1)
p.xlabel ('year',fontproperties=fontprop1)
p.ylabel ('Top 10',fontproperties=fontprop1)
p.grid (True)
p.legend(loc = 'upper left',prop=fontprop2)
p.show()
