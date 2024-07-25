#Please note that this code is not finished and is currently only a skeleton

#The goal of this program is to open up an EIS data file from an excel sheet, find resisitivity at 
#different temperatures from nyquist plots, and plot a graph containing activation energy for that sample.
#After that is done, the program will then take all the information and import it into another excel file

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Variable List
fileName = ""
infile = ""
df = []
headers = []
Datadict = {}
x=[]
y=[]


#Enter file name here
fileName = "2024-07-02  x=0.5 y=0.8 LiNaB Pearlman Wlochal"

#Creates a pandas dataframe from an excel sheet
infile = f"{fileName}.xlsx"
df = pd.read_excel(infile) 

#Grabs the colunms names from the data frame
for col in df.columns:
    col = col.strip()
    headers.append(col)
    

#Takes info from data frame and puts it into a dictionary
#This is done to seperate the tempurature values and resistivity
for i in df.values:
    xy = i[2], -i[3]
    temp = i[1]
    try:
        Datadict[temp].append(xy)
    except(KeyError):
        Datadict[temp] = []
        Datadict[temp].append(xy)



tempRes = []
for i in Datadict.keys():
    data = Datadict[i]
    x = []
    y = []
    for j in data:
        Zs_real, Zs_imagine = j
        x.append(Zs_real)
        y.append(Zs_imagine)

    maxLoc = 0
    start = y[maxLoc]
    maximum = start

    while y[maxLoc + 2] > maximum and y[maxLoc + 1] > maximum and y[maxLoc - 2] < maximum and y[maxLoc - 1] < maximum:
        maxLoc += 1
        maximum = y[maxLoc]

    halfMax = maximum/2
    hMaxLoc = maxLoc
    while hMaxLoc <= len(y) and y[hMaxLoc] > halfMax:
        hMaxLoc +=1

    if(hMaxLoc < len(y)):
        result = i , maxLoc*2
        tempRes.append(result)
        print(result)
    else:
        print("No result")
    
print(tempRes)
