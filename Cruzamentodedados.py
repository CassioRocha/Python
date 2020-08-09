import csv
import pandas as pd


with open(r'C:\Users\Rocha\Desktop\pre1.csv', newline='') as f:
    reader = csv.reader(f)
    c1 = list(reader)


with open(r'C:\Users\Rocha\Desktop\Auxilio.csv', newline='') as f:
    reader = csv.reader(f)
    c2 = list(reader)


thislist=[]
i = 0
j=0
for i in range(len(c1)):
   for j in range(len(c2)):
         print(c1[i]) 
         if(c1[i]==c2[j]):
           thislist.append(c1[i])

              
print("",thislist)
    
       
       
