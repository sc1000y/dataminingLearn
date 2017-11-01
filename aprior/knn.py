# k-NN算法
import sys
import IDBKit
import math


def getDataSet():
    db=IDBKit.IDBKit();
    sql="select ID,number,mile,day,decision from DM_KNN";
    list=db.find(sql)
    return list
def getMaxMin(rawData,index):
    t=0.0;
    tmpList=[]
    for item in rawData:
        tmpList.append(float(item[index]));
    t=max(tmpList)-min(tmpList)
    return t;

def kNN(data,target):
    list=[]
    s1=getMaxMin(data,1);
    s2=getMaxMin(data,2);
    s3=getMaxMin(data,3);
    for item in data:
        #list.append([math.sqrt(pow(float(item[1])-target[0],2)+pow(float(item[2])-target[1],2)+pow(float(item[3])-target[2],2)),item])
        
        tmp1=(float(item[1])-target[0])/s1;
        tmp2=(float(item[2])-target[1])/s2
        tmp3=(float(item[3])-target[2])/s3
        list.append([math.sqrt(pow(tmp1,2)+pow(tmp2,2)+pow(tmp3,2)),item])
        
    list.sort()
    return list;
    
def kNN2(data,target):
    list=[]
    s1=getMaxMin(data,1);
    s3=getMaxMin(data,3);
    for item in data:
        list.append([math.sqrt(pow((float(item[1])-target[0])/s1,2)+pow((float(item[3])-target[1])/s3,2)),item])
    list.sort()
    return list;
if __name__=="__main__":
    myDat=getDataSet()
    #print(myDat)
    #print(getMaxMin(myDat,1))
    
    target=[25,2050,790]
    
    retr=kNN(myDat,target);
    for item in retr:
        print(item)
        
    
    
    print("---------------")
    target=[58,650]
    retr=kNN2(myDat,target);
    for item in retr:
        print(item)
    temp=0;
    print((2867.3+3370.0+2437.8+2804.9+1929.7)/5)
    
    print(15,"is",math.sqrt(15))
    