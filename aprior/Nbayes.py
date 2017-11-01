# -*- coding:utf-8 -*-
#naive bayes
import sys
import IDBKit
import scUtil
import math
import operator

row=["gender","sp","asti","tear","recom"]
table="dm_id3_trail"
def getDataSet():
    db=IDBKit.IDBKit();
    
    sql="select "+",".join(row)+" from "+table;
    list=db.find(sql)
    return list

 
def calculateProb(dataSet,index,targetIndex):
    siz=len(dataSet)
    prob=float(1/siz)
    targetIndexList={}
    for data in dataSet:
        if data[targetIndex] not in targetIndexList:
           targetIndexList[data[targetIndex]]={};
           if data[index] not in targetIndexList[data[targetIndex]]:
               targetIndexList[data[targetIndex]][data[index]]=prob
           else:
               targetIndexList[data[targetIndex]][data[index]]+=prob
        else:
           if data[index] not in targetIndexList[data[targetIndex]]:
               targetIndexList[data[targetIndex]][data[index]]=prob
           else:
               targetIndexList[data[targetIndex]][data[index]]+=prob
               
    
            #data[value]=float(data[value])/float(siz)
    #print(targetIndexList)
    return targetIndexList
def naive(dataSet):
    naiveList=[]
    for i in [0,1,2,3]:
      naiveList.append(calculateProb(myDat,i,4))
    return naiveList
def testTarget(target,naiveList):
    for tar in target:
        for na in naiveList:
            print(1)
if __name__=="__main__":
    myDat=getDataSet()
    naiveList=naive(myDat)
    print(naiveList)
    #testTarget(["F","H","Y","R","S"],naiveList)