# k-NN算法
import sys
import math

def getMaxMin(rawData,index):
    t=0.0;
    tmpList=[]
    for item in rawData:
        tmpList.append(float(item[index]));
    t=max(tmpList)-min(tmpList)
    return t;
def getMin(rawData,index):
    t=0.0;
    tmpList=[]
    for item in rawData:
        tmpList.append(float(item[index]));
    return min(tmpList)
def norm(dataSet):
    retList=[]
    normList=[]
    norm=0
    siz=len(dataSet[0])
    for i in range(1,siz):
        norm=getMaxMin(dataSet,i)
        mi=getMin(dataSet,i)
        normList.append([norm,mi])
    #print(normList)
    for data in dataSet:
        tmp=[data[0]]
        for i in range(1,siz):
            tmp.append((float(data[i])-normList[i-1][1])/normList[i-1][0])
        retList.append(tmp)
    return retList
def translateData(rawData,targetData,targetIndex):
    retData=[]
    for dataValue in rawData:
        tmpData=list(dataValue)
        #print(tmpData)
        #print(targetData[dataValue[targetIndex]])
        tmpData[targetIndex]=targetData[dataValue[targetIndex]]
        retData.append(tmpData)
    return retData