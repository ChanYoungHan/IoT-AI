#내장 모듈
from urllib.request import *
import sys
import time

#외부 모듈
from bs4 import *
import matplotlib.pyplot as p
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as mat
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

url=['http://las.kiost.ac/las/output/46DCE983CA419E9D4F4A3FD134EFA604_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/169313B7480B52BB467DAAAC1A6F7EA9_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/F77E005213D7E26913E53314DC86AE8E_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/0717C0DF837D1775B3830D76E2929C29_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/EFC205471366536101F304F377D34521_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/697A5A8545A1ABCA1F35A344927A085A_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/D883718B90BF8702127E44C9BEA4DAA2_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/87478F15482877B456B8E5353F58C5FE_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/FEE7AED370F7E6F35BA98FC7FBD748F3_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/46DCE983CA419E9D4F4A3FD134EFA604_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/169313B7480B52BB467DAAAC1A6F7EA9_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/13AB20C6A1BD8CF53B852485B409AFC4_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/563BCA28505B71A9EE63AA5DF47E0486_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/AF67412A813CE9B5386EE5E4242F1FA9_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/E9647E216AFCA74B4BAB9B05E3FC3B29_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/552D82FC93BF283BF2B67F6DEEB8DEF4_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/6510609519E3F33E4F66D8F5263F5F2C_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/8882A8F63359541DCEE4D3909FB5ABA6_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/0D87E1EB5D16680D3BF9F126EC836E15_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/2570E438DE225CB02916B9F3DB3D06D5_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/1A001A79A42FF43E3C6FDEC9170866AF_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/82213E9142DFC80A1A511E8BBCA28547_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/D9BE4D337B70535A119B8420F2EA838C_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/84577321BAAFB4A7D4A1B19BA9B49071_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/802BBD8034E861C1C5F314645F64B5A2_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/92B566D88A64DB809F68D05AA0B3E738_ferret_listing.txt',\
     'http://las.kiost.ac/las/output/45D0D221F6CDAE4C701E5AFC9ECDAA9A_ferret_listing.txt']

def obtainXYT (web):

    wPage = urlopen(web)
    soup = BeautifulSoup(wPage, 'html.parser')
    UNdata = soup.get_text()



    data=UNdata.find("DATETIME,TIME,LON,LAT,SST")
    data=data+len("DATETIME,TIME,LON,LAT,SST")
    data = UNdata[data:]
    data = data.splitlines()


    #data[0]=[] index 1 부터 시작
    #print(data)

    loca_com=[]
    dictime= dict()
    XYZ=[]
    X=[]
    Y=[]
    Z=[]
    #len(data)-1
    for a in range(1,len(data)-1):
        loca_com_spl=data[a+1].split(',')
        #print(loca_com_spl)
        
        #print(type(loca_com_spl), len(loca_com_spl))
        local_temper=[]

        
        local_temper.append(loca_com_spl[2])
        X.append(float(loca_com_spl[2]))
        local_temper.append(loca_com_spl[3])
        Y.append(float(loca_com_spl[3]))
        local_temper.append(loca_com_spl[4])
        Z.append(float(loca_com_spl[4]))
        XYZ.append(local_temper)
    return X,Y,Z,XYZ





#X : 경도 리스트, Y : 위도 리스트, coord : 검색해볼 좌표, s : 년, 월
def Graph(X, Y, T, coord, s):
    latitude = list()
    longitude = list()
    temp = list()
    x, y = coord.split()
    #celsius = "X : %s, Y : %s, Celsius : 32.3" %(x, y)
    x = float(x)
    y = float(y)

    for i in range(len(X)):             #육지에서의 좌표는 음수, plotting하기 위해 육지일때의 인덱스 및 값들 제거
        if T[i] > 0:
            longitude.append(X[i])
            latitude.append(Y[i])
            temp.append(T[i])
        else:
            continue

    latitude = np.array(latitude)
    longitude = np.array(longitude)

    colormap = temp
    plt.figure()
    plt.scatter(longitude, latitude, s = 100, cmap = 'jet', c = colormap, marker = 's', vmax = 20, vmin = 2)
    plt.title(s+'  Sea Surface Temperature')
    plt.colorbar(label = 'Temperature')

    #딕셔너리에서 불러오기. 온도.(str tpype으로)
    #plt.xlabel(celsius)

    plt.scatter(x, y, marker = '.')
    
    plt.show()
    
    
datafw=open("data.txt",'w')

Temper_=dict() 
TempbyXY=[]
edt = datetime(2012,2,1)
time=[]
subtime=[]

#range(27) defalut, 링크 갯수 조절
for a in range(len(url)):
    
    # 크롤러 함수, 타임스텝 1에 대한 X, Y, T 를 리스트로 저장
    X,Y,Z,XYZ= obtainXYT(url[a])

    #cor_xy = input("좌표를 입력하세요")
    #cor_xy= '130.375 35.625'   #제주
    #cor_xy= '129.875 37.125'    #동해
    cor_xy= '125.875 35.875'    #서해

    ####3 계절별로 그래프 plot   ####
    if(a+1)%4==1:
        Graph(X,Y,Z,cor_xy,str(edt)[:7])
    
    Temper_.update({str(edt):XYZ})      #key가 날짜인 dict
    LocationT = dict()

    #key가 좌표, value가 t-T 리스트인 dict
    for b in range(len(X)):
        LocationT.update({str(X[b])+' '+str(Y[b]):Z[b]})

    #x,y 좌표에 해당하는 T 값 추출하기
    TempbyXY.append(LocationT.get(cor_xy))
    
    time.append(str(edt)[:7])   # 날짜 표시
    edt = edt + relativedelta(months=3)

    subtime.append([2+a])       # legression plot 사용할 x축

######### LinearRegression ###########
model=LinearRegression()
model.fit(X=subtime,y=TempbyXY)
mat.plot(subtime, model.predict(subtime),color='r')

# plot
mat.scatter(subtime, TempbyXY) 
mat.ylabel('Temperature($^{\circ}$C)')
mat.xlabel('the number of monthes after 2012')
mat.title('Temperatur plot of Cordinate {}'.format(cor_xy))
mat.show()

datafw.close


