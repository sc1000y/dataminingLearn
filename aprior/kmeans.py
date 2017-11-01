# -*- coding:utf-8 -*-
#id3
import sys
import IDBKit
import scUtil
import math
import operator

row=["ref","age","sex","monthly_income","marital_status","service_plan","extra_usage"]
dict={'m':0,'f':1}
dict2={'y':1,'n':0}
table="dm_kmeans"
def getDataSet():
    db=IDBKit.IDBKit();
    
    sql="select "+",".join(row)+" from "+table;
    list=db.find(sql)
    #处理数据
    
    list=scUtil.translateData(list,  dict,2)
    
    list=scUtil.translateData(list,  dict2,4)
    return list

def calcEuk(data,target):
    siz=len(data)
    tmp=0
    for i in range(1,siz):#  除去第一行ID号
        tmp+=pow((float(data[i])-float(target[i])),2)
    return math.sqrt(tmp)
def chooseHigh(data,targets):
    distList={}
    
    for target in targets:
        distList.setdefault(target[0],[])#只设定ID
        
    for value in data:
        tmp=["",[],99999];
        tmpLabel="";
        for target in targets:
          if tmp[2]>calcEuk(value,target):
              tmp=[target[0],value,calcEuk(value,target)]
        #print(tmp)
        distList[tmp[0]].append(tmp[1])
    return distList
def kmeans(dataSet,taregertValues):
    dealDate=chooseHigh(dataSet,taregertValues)
    #print(dealDate)
    siz=len(dataSet[0])
    newK=[]
    lenSet=len(dataSet)
    for values in dealDate:
        #print(dealDate[values])
        tmp=[values]
        for i in range(1,siz):
            tmp2=0
            for value in dealDate[values]:
                tmp2+=value[i]
            tmp2=tmp2/lenSet
            tmp.append(tmp2)
        #print(i)
        newK.append(tmp)
    print("------------")
    print(newK)
    print("----round 2")
    dealDate2=chooseHigh(dataSet,newK)
    print(dealDate2)
    newK2=[]
    for values in dealDate2:
        #print(dealDate[values])
        tmp=[values]
        for i in range(1,siz):
            tmp2=0
            for value in dealDate2[values]:
                tmp2+=value[i]
            tmp2=tmp2/lenSet
            tmp.append(tmp2)
        #print(i)
        newK2.append(tmp)
    print(newK2)
if __name__=="__main__":
    myDat=getDataSet()
    normDat=scUtil.norm(myDat)
    kmeans(normDat,[normDat[0],normDat[1]])
    kmeans(normDat,[normDat[0],normDat[1],normDat[2]])
    