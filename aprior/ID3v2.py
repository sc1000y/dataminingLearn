# -*- coding:utf-8 -*-
#id3
import sys
import IDBKit
import math  
import operator


row=["gender","sp","asti","tear","recom"]
table="dm_id3_trail"
def getDataSet():
    db=IDBKit.IDBKit();
    
    sql="select "+",".join(row)+" from "+table;
    list=db.find(sql)
    return list

 
def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] +=1
         
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*math.log(prob, 2)
    
    return shannonEnt
     

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec+=featVec[axis+1:]
            retDataSet.append(reducedFeatVec)
     
    return retDataSet
 
def chooseBestFeatureToSplit(dataSet,labelSet):
    numberFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    print("base entropy is ",baseEntropy)
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
        print(labelSet[i],"'s new entropy is",newEntropy)
        infoGain = baseEntropy - newEntropy
        print(labelSet[i]," infoGain is:",infoGain)
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    print("-------   best is:",labelSet[i-1],bestInfoGain)
    return bestFeature
 
def majorityCnt(classList):
    classCount ={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]=1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
  
 
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet,labels)
    
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
    
if __name__=="__main__":
    myDat=getDataSet()
    myTree=createTree(myDat,row)
    print(myTree)