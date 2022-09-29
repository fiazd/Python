#Daanish Fiaz
#Module 2 Assignment 1
#Olympic Analysis
import pandas as pd #Import statements
import seaborn as sns
import matplotlib.pyplot as plt
#Read in df
df = pd.read_csv('athlete_events.csv')
print(str(df.shape) + '\n')

#how many atheletes won gold metals
numGold = 0
for value in df.Medal:
    if value == 'Gold':
        numGold = numGold + 1
print(str(list(df)) + "\n")
print('The number of gold medals is: ' + str(numGold) + ' medals\n')

#function to find nan percent of a column
def NaN_percent(df, columnName):
    rowCount = df[columnName].shape[0]
    emptyValues = rowCount - df[columnName].count()
    return(100.0*emptyValues)/rowCount
    
for i in list(df):
    print(i + ': ' + str(NaN_percent(df,i))+'%')

#how many different people won a medal since 1900
totalRows = df.shape[0]
uniqueAthletes = len(df.Name.unique())
medalWinners = len(df[df.Medal.fillna('None') != 'None'].Name.unique())
print('\n')
print('totalRows, uniqueAthletes, medalWinners')
print("{0} {1} {2}".format(totalRows,uniqueAthletes,medalWinners) + '\n')

#get medal distribution
#how manay medals have been earned through the years
print(df[df.Medal.fillna('None') != 'None'].Medal.value_counts())

print('Total: ' + str((df[df.Medal.fillna('None') != 'None'].shape[0])) + '\n')


#Distribution by countries
team_medal_count = df.groupby(['Team','Medal']).Medal.agg('count')
#order by quantity
team_medal_count = team_medal_count.reset_index(name='count').sort_values(['count'], ascending = False)
#function to get country stats
def getCountryStats(country):
    return team_medal_count[team_medal_count.Team == country]
print(getCountryStats('United States'))

#Female Participation
uniqueWomen = len(df[df.Sex =='F'].Name.unique())
uniqueMen = len(df[df.Sex =='M'].Name.unique())
womenMedals = df[df.Sex =='F'].Medal.count()
menMedals = df[df.Sex =='M'].Medal.count()
print('\n')
print('Number of men, number of women, number of women medals, number of men medals')
print("{} {} {} {} ".format(uniqueWomen, uniqueMen, womenMedals, menMedals ))
#Since 1900
print(df[df.Sex=='F'].Year.min())

#Female participation vs men participation
fyearCount = df[df.Sex=='F'].groupby('Year').agg('count').Name
myearCount = df[df.Sex=='M'].groupby('Year').agg('count').Name
(sns.scatterplot(data= myearCount),
 sns.scatterplot(data =fyearCount))




