import sqlite3
'''
Shu Chang
2017-9-23 PolyU

get a easy connect to sqllit3
'''


class IDBKit:
   path="C:\\work\python\\aprior\\";#default path
   name="poly.db";#defalut dbname
   conn="";
   cursor="";
   
   def __init__(self,path=path,name=name):
       self.conn=sqlite3.connect(self.path+self.name);
       self.cursor=self.conn.cursor();
   
   def instance():
       return self.cursor;
   
   def execute(self,sql,*arg):
       cur= self.cursor.execute(sql,arg);
       return cur.commit;
       
   def find(self,sql,*arg):
       cur = self.cursor.execute(sql,arg);
       return cur.fetchall();
       
  
   def findone(self,sql):
       cur = self.cursor.execute(sql);
       return cur.fetchone();
       