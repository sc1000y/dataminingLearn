import IDBKit
import math
def getDataSet():
    db=IDBKit.IDBKit()
    sql="select DRYFRUIT,NUT,NOODLE,SHAMPOO,DIAPER,BEER,MILK from DATAMINING_ASS1_APRIOR"
    return db.find(sql)

class apriori2():
    support=0.2
    confident=0.7
    dataSet=[]
    minMap={}
    rowCount=0
    def __init__(self,dataSet,support=0.2,confident=0.7):#初始化apriori算法
        self.dataSet=dataSet
        self.support=support
        self.confident=confident

    def apriori(self):
        self.minMap=self.findMinMap(self.dataSet,self.support)
        print("Min support map is ",self.minMap)
        dict=self.generateCollect(self.minMap,self.minMap)
        #print(self.dataSet)
        print("Next stepCollect is ",dict)
        #dict2=self.generateCollect(dict,self.minMap)
        #print("Next stepCollect is ",dict2)
        self.sumSupport(self.dataSet,dict,self.confident)
     
    @staticmethod
    def findMinMap(dataSet,support):#获取最小集
        rowNum=len(dataSet[0])
        minMap={}
        for row in dataSet:
            for i in range(0,len(row)):
                if row[i] is not None:
                    if row[i] not in minMap:
                        print("A new element ", row[i]," is found")
                        minMap[row[i]]=1
                    else:
                        minMap[row[i]]=minMap[row[i]]+1
                    
                    
        dataCount=len(dataSet)
        minCount=math.ceil(dataCount*support)
        print("Min count is",minCount)#算出最小support对应的count
        
        minMapCopy=minMap.copy()#删掉不够数的
        for (key,value) in minMap.items():
                #print(key," is ",value)
                if value < minCount:
                      del minMapCopy[key]
                else:
                      minMapCopy[key]=minMapCopy[key]/dataCount#将dict中count换算为support
        
        return minMapCopy
        
    @staticmethod
    def generateCollect(stepCollect,minMap):
        collect={}
        count=1
        for (key,value) in stepCollect.items():
            for(minKey,minValue) in minMap.items():
                if key is not minKey and (key,minKey) not in collect and (minKey,key) not in collect:
                    collect[key,minKey]=0
                
        return collect
    
    @staticmethod
    def sumSupport(dataSet,stepCollect,minConfident):
        for (key,value) in stepCollect.items():
            tempTo=key[-1]
            tempFrom=key[0]
            #print(tempFrom,tempTo)
            for transaction in dataSet:
                if tempFrom in transaction and tempTo in transaction:#  两个都存在
                    #print(stepCollect[key])
                    stepCollect[key]=stepCollect[key]+1
                    
             nextCollect=stepCollect.copy()
             for (key,value) in stepCollect.items():
                 
        return stepCollect
    def execute(self):
        #print("apriori")
        self.apriori()
    

if __name__=="__main__":
    ap=apriori2(getDataSet())
    ap.execute()
    #print(ap.dataSet)
