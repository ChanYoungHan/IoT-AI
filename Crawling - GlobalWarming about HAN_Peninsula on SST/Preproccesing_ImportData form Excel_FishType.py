import pandas as pd         # excel_come=이름과 년도리스트
import operator as o        # 편차
import matplotlib.pyplot as p
import numpy as n
from sklearn.linear_model import LinearRegression
from matplotlib import font_manager, rc

font_location = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname = font_location).get_name()
rc('font',family = font_name)       #폰트 한글 설정

def excel_top(tb, dirR):
    print(tb)
    model=LinearRegression()
    for i in tb:
        time=[]
        
        for a in range(len(dirR[i])):
            time.append([a+1])
        model.fit(X=time,y=dirR[i])

        p.plot(time, model.predict(time),color='r')

        p.scatter(time, dirR[i])
        p.title(i)
        p.show()
        

def excel_plus(dir):
    dirR=dir
    N_list=list(dir.keys())
    Num_list=list(dir.values())
    A=[]        #앞뒤의 차이를 저장할 리스
    Top=[]      #top5
    Bottom=[]   #bottom5
    for i in range(len(Num_list)):
        mx=int(sum(Num_list[i][:5])/5)                  #앞년도5개평균값
        mn=int(sum(Num_list[i][len(Num_list[i])-5:])/5) #뒷년도5개평균값
        A.append(mx-mn)
    dir_plus={}
    for i in range(len(N_list)):
        dir_plus[N_list[i]]=A[i]
    dir_result=sorted(dir_plus.items(), key=o.itemgetter(1), reverse=True)
    
    for i in range(5) :
        Top.append(dir_result[i][0])
        
    for i in range(len(dir_result)-5,len(dir_result)):
        Bottom.append(dir_result[i][0])

    TB = Top+Bottom
    excel_top(TB, dirR)

    
def excel_come(come):
    c1=come.iloc[1:,0]  #1행 0열 = 이름

    N=[]                #이름을 저장할거야
                        #갯수들의리스트를저장할거야
    dir={}              #이름을입력하면년도를 보여줘 6=0index,6-18년도
    b=0                 #dir에 넣을때 필요한 변수
    print(c1)
    for i in c1:
        i=i.replace("\u3000","")        #얘는 반환해와야대
        i=str(i)
        N.append(i)                     #이름

    for a in range(1,len(c1)+1):
        Nu=[]
        for c in range(1,len(come.columns)):
            c2=come.iloc[a,c]           #행고정->열돌려
            c2=float(str(c2).replace('-','0')) 
            Nu.append(c2)               #년도를 리스트화
        dir[N[b]]=Nu                    #key,value
        b+=1
    excel_plus(dir)
    return dir


go=pd.read_excel("어업별_품종별_어법별_통계_20190730131811.xlsx")  #일단 불러온다

Fin= excel_come(go)
#print(Fin)
