# -*- coding:utf-8 -*-
#id3  手工实现
import sys
import IDBKit
from math import log  
import operator


row=["gender","sp","asti","tear","recom"]
table="dm_id3_trail"
def getDataSet():
    db=IDBKit.IDBKit();
    
    sql="select "+",".join(row)+" from "+table;
    list=db.find(sql)
    return list
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)  
    labelCounts={}  
    #给所有可能分类创建字典  
    for featVec in dataSet:  
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel]=0  
        labelCounts[currentLabel]+=1  
    shannonEnt=0.0  
    #以2为底数计算香农熵  
    #print(labelCounts)
    for key in labelCounts:  
        prob = float(labelCounts[key])/numEntries  
        shannonEnt-=prob*log(prob,2)  
    #print(shannonEnt)
    return shannonEnt 
    
#手工实现ID3
def cal(myDat):
    size=len(row)
    shan=[]
    for i in range(0,size):
        tmpDat=[]
        for dataValue in myDat:
          tmpDat+=dataValue[i]
        shan+=[row[i],float(calcShannonEnt(tmpDat))]
    print(shan)
    #第一次
    setA,setB=splitData(myDat,0,"M")
    
    print(setA)
    print(setB)
    #第二次
    print("-------------")
    chooseBestFeatureToSplit(setA)
    print("-------------")
    chooseBestFeatureToSplit(setB)
    print("-------3------")
    setAA,setAB=splitData(setA,3,"R")
    setBA,setBB=splitData(setB,3,"R")
    
    print(setAA)
    print(setAB)
    
    print(setBA)
    print(setBB)
    #
def splitData(dataSet,targetAix,value):
    setA=[]
    setB=[]
    for dataValue in dataSet:
        if value==dataValue[targetAix]:
            setA.append(dataValue)
        else:
            setB.append(dataValue)
    return setA,setB
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec+=featVec[axis+1:]
            retDataSet.append(reducedFeatVec)
    #print(retDataSet)
    return retDataSet
 
def chooseBestFeatureToSplit(dataSet):
    numberFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = -1;
    for i in range(numberFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy =0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        
        print(row[i]," infoGain is:",infoGain)
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    print("best is:",bestInfoGain,row[bestFeature],bestFeature)
    return bestFeature
def cal2(myDat):
    size=len(row)
    shan=[]
    i=chooseBestFeatureToSplit(myDat)
    print("choose ",row[i],i);
if __name__=="__main__":
    myDat=getDataSet()
    print(myDat)
    cal2(myDat)
    
    