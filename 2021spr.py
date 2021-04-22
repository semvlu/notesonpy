j= "christmas eve"
print(j[2:5])
print(j[3:])
print(j[:3])   # alphabet is included if its number is written before the colun, excluded if after
print(j[3:7])

x= input("x is: ")
y= input("y is: ")
if x>y:
    print("x(" + x + ") is the maximum")
elif x==y:
    print("both values are " + x)
else:
    print("y(" + y + ") is the maximum")

list1 = [55,42,99,36]
list1 = list1 + [22]
list1[0] = 11         #list [11,42,99,36,22]
print(list1)
print(len(list1))
list1[2:4] = []
print(list1)          #list [11,42,22]  

seat = [[33,44,55],[12,13,14]]
print(seat[1][2])

giga = {37,39,41}
gigb = {37,41,45}
s1= giga&gigb #and
s2= giga|gigb #or
s3= giga^gigb #xor
s4= giga-gigb #a not b

dic = {"apple":"appel", "banana":"banaan"}
dic["apple"] = "apppp" 
print(dic["apple"])
print("apple" in dic)
del dic["banana"]

for x in range(2):
    for y in range(7):
        print(y,end="    ") #"end" and the following (" ")means that the output follows the rule with the space or blank in ("  ")
print()

f= [2,89,29,83,268]
for w in range(len(f)):
    print(f[w]) #loop1

for i in f:
    print(i) #loop2
#loop1=loop2

def recur(n):
    if n<2:
        return n
    return recur(n-1) + recur(n-2)
print(recur(3)) #recurse 3 times, run from: 1, 12 ,112
print(recur(4)) #recurse 4 times, run from: 1, 12, 112, 1123

def mult(g, h):
    return(g*h)
a= mult(3,6)
b= mult(2,8)
print(a+b)

n= int(input("press the button "))

if n%2==1:
    for o in range(1,n+1):
        if o%2==0:
            continue
        print("the floors we got are %d" %(o),end=", ")

elif n%2==0:
    for p in range(1,n+1):
        if p%2==1:
            continue
        print("the floors we got are %d" %(p),end=", ")
        
import os
os.chdir("change to the dir u want")
import json
with open("filename.json", mode="r") as file:
    scorelist = json.load(file)
scorelist["score"]="23"
with open("filename.json", mode="w") as file:
    json.dump(scorelist, file)

for i in (scorelist):
    print(i["name"],"'s score is", i["score"])
    
with open("filename.txt", "rb") as ogfile:
    with open("filename-1.txt", "wb") as newfile:
        for i in ogfile:
            newfile.write(i)


print("B10933001")
from datetime import datetime as dt
print(dt.now())

import os
os.chdir("fileHand")
file= open("0330.txt", mode="w", encoding="utf-8")
file.write("test")
file.close()

with open("0330-1.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n42\n15")

counts=0
with open("0330-1.txt", mode="r", encoding="utf-8") as file:
    for i in file:
        counts+= int(i)
print(counts)

# -*- coding:UTF-8 -*-
import sqlite3
conn= sqlite3.connect("filename.db")
cur= conn.cursor()
exe= cur.execute

sqlstr="insert into books values('1006', '差異與重複', '1092')" #update "table" set "column to be changed" where "location"
sqlstr1="update books set name='猿猴、賽伯格和女人：重新發明自然' where id='1003'"
sqlstr2="select * from books where sms='1092'" #select * from table 
sqlstr3="select * from books order by id asc" #order by "column" desc,asc
sqlstr4="select * from books order by id desc limit 4" #order by "column" desc limit "'record' num"
sqlstr5="select * from books where name like '%悲劇%' " #where "column" like %str%
sqlstr6="delete from bnkrupt where id='1004'" #delete from "table" where "location"
exe(sqlstr1) 
books=cur.fetchall()
for i in books:
    print(i)

conn.commit()
conn.close()
