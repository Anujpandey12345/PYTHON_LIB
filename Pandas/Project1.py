"""Feature Extraction Poject"""
import pandas as pd
import numpy as np
#loading the data -> Loading the Data , we are uisng read_csv(r'anime.csv')
df = pd.read_csv(r'anime.csv') #r is for row String
print(df)
print(df.head()) #Print Top Five Data


"""make a new column for episode count"""
# print(df.loc[2]) # this Show whole row Data
# print(df.loc[2]['Title']) #This Show Only title of the 2nd Row(o/p -> Bleach: Sennen Kessen-henTV (13 eps)Oct 2022 - Dec 2022474,138 members)
#Now i want to Extract episode column from the Data(13 eps in Bleach)
def extract_episode(txt):
    check = False
    data = ""
    for i in txt:
        if i == ")":
            check = False
            return data
        if check == True:
            data = data + i
        if i == "(":
            check = True

df["Episodes"] = df["Title"].apply(extract_episode)
print(df)
df["Episodes"] = df["Episodes"].str.replace(" eps","") #Replace the eps to empty string
print(df)
df["Episodes"] = df["Episodes"].astype(int)  #Chnage string into Integer
print(df)
print(type(df.loc[4]["Episodes"]))


"""-------make a new column for time stamp--------"""
print(df.loc[1]["Title"]) #This is timestamp Apr 2011 - Sep 2011
def extract_time(txt):
    check = False
    data = ""
    for i in range(len(txt)):
        if txt[i] == ")":
            for j in range(i+1, i+20):
                data += txt[j]
        
            return data
df["Time Stamp"] = df["Title"].apply(extract_time)
print(df)

"""which anime has the highest score"""
ans = df[df['Score'] == df['Score'].max()]['Title']
print(ans)


"""give me top 5 highest scoring anime"""
print(df['Score'].unique)
print(df['Score'].value_counts)
print(df['Title'].head())


"""which anime has the highest episode count"""

ans = df[df['Episodes'] == df['Episodes'].max()]
print(ans)

#animes with top 5 episode count
#which is the longest running anime