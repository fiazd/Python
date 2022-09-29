# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:47:00 2020

@author: Daanish Fiaz

DATA SCIENCE SKILLS 391

BALLET HW
"""

import pandas as pd #imports Pandas and assigns the worksheet to the name  pd
import numpy as np  #imports the numpy module and assigns it to the name np
from numpy import cov
import scipy.stats  #imports the scipy.stats library
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import matplotlib.pyplot as plt #imports the plot library

#First part of the assignment
# We are going to set up a dataframe ... think of this as a matrix or a spreadsheet
# Note that if I am in the folder with the .csv file, then I don't need to use the full path. I can
# just put the name of the .csv file. If I am not in the folder, then I have to put the hardwired path to the
# .csv file Personally, I like to cd to the folder in which my code resides. Makes things easier for me.
# Your choice though.
df = pd.read_csv('Book1.csv') # read the .csv file and assign it to the data frame df. The data frame can be
#thought of as a type of spreadsheet with rows and columns.

#Set up some display features for when it prints to the screen or to a file
pd.set_option('display.max_columns',None) #Sets up display of how many columns can be displayed
pd.set_option('display.max_colwidth',-1) #Sets up the maximum column with displayed

# display basic file structure information
print(df) #outputs the dataframe from the file that was read in. 
            #I commented it out but you could uncomment it if you want to to see everything
print(f'\n ------ Print Header Information')
print(df.head(0)) #prints just the column labels
print(df.head()) #prints out first 5 lines so you can check you input and output. If you want to see more
#or less lines, you would put the number of lines you want to see in the parentheses. For example, if I 
#wanted to display only two lines, I would write:
print(df.head(2))

print(f'\n ------ Basic dataframe properties')
# In this section we get some basic structure of the dataframe; rows, columns or what is called
# the shape of the dataframe.
print(df.count()) #prints out the number of elements in each column variable
print('Number of lines is ', len(df)) #the total number of lines in the file
print('Matrix shape = ',df.shape) #prints total number of columns and lines (lines,columns)

# Now we obtain some information about the contents of the dataframe.
print(f'\n ------ Basic dataframe counts')
print(df.columns) #prints column headers (first line of .csv file)
print('number of unique group ids in list=',df["Group"].nunique()) #prints number of experimental 
                                                                   #groups in the dataset
print('number of unique sex ids in list=',df["Sex"].nunique())#prints the number of sexes in the study
print(f'{"Group":<12}Number')
print(df["Group"].value_counts())#prints total number of participants in each experimental group
print(f'\n') #Forces a line break (skip a row) so that the output is more readable.

print(f'{"Sex":<5}Number')
print(df["Sex"].value_counts().sort_index())#prints total number of participants in 
                                            #each sex group

gk = df.groupby('Group')#groups the data into a table by experimental group
print(gk["Sex"].value_counts().sort_index())#prints,for each group, how many of 
                                            #each sex there are


gk.get_group('Ballet')
gk.get_group('Controls')
gkk = df.groupby(['Group', 'Sex'])#creates a table described by Group by Sex
print(f'\n ---------- Group by Sex')
print(gkk.describe())#prints out the statistics for the group by sex table

#There are fancier python panda ways to do the following. However, I will 
#show you the straightforward way. Though tedious, it is very understandable.
#You can try fancier ways when you have the time.
#
#In the following block, we are assigning the data stored in each subgroup.
#For example, the first line extracts the data in Group=Ballet and Sex=Female.
#It then stores that data in the dataframe ballet_female_data. Obviously, the
#rest of the commands follow similar constructs. We then print out each of the
#dataframes.
ballet_female_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="F")]
ballet_male_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="M")]
ballet_female_data=df[(df["Group"]=="Controls") & (df["Sex"]=="F")]
ballet_male_data=df[(df["Group"]=="Controls") & (df["Sex"]=="M")]
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="M")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="M")])

#In the following block, we are assigning the data stored in each subgroup.
#For example, the first line extracts the data in Group=Controls and Sex=Female.
#It then stores that data in the dataframe ballet_female_data. Obviously, the
#rest of the commands follow similar constructs. We then print out each of the
#dataframes.
controls_female_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="F")]
controls_male_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="M")]
controls_female_data=df[(df["Group"]=="Controls") & (df["Sex"]=="F")]
controls_male_data=df[(df["Group"]=="Controls") & (df["Sex"]=="M")]
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="M")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="M")])

#So we have now parsed out the original dataframe into smaller dataframes
#and we want to extract the specific column information from each one.
#For example, in the first line below, we are extracting the data stored
#in the "Age (years)" column stored in the ballet_female_data and we are
#storing the result in the vector ballet_female_data_ages. The rest of the code is
#obviously the same idea for the different subgroups of the data.
ballet_female_data_ages=ballet_female_data["Age (years)"]
ballet_male_data_ages=ballet_male_data["Age (years)"]
ballet_female_data_bodymass=ballet_female_data["Body Mass (kg)"]
ballet_male_data_bodymass=ballet_male_data["Body Mass (kg)"]
ballet_female_data_bodyheight=ballet_female_data["Body Height (cm)"]
ballet_male_data_bodyheight=ballet_male_data["Body Height (cm)"]
ballet_female_data_bmi=ballet_female_data["BMI (kg/m2)"]
ballet_male_data_bmi=ballet_male_data["BMI (kg/m2)"]

controls_female_data_ages=controls_female_data["Age (years)"]
controls_male_data_ages=controls_male_data["Age (years)"]
controls_female_data_bodymass=controls_female_data["Body Mass (kg)"]
controls_male_data_bodymass=controls_male_data["Body Mass (kg)"]
controls_female_data_bodyheight=controls_female_data["Body Height (cm)"]
controls_male_data_bodyheight=controls_male_data["Body Height (cm)"]
controls_female_data_bmi=controls_female_data["BMI (kg/m2)"]
controls_male_data_bmi=controls_male_data["BMI (kg/m2)"]

#Suppose we wish to see what is stored in each of our vectors
#above. We can just use the print command. Note that this prints
#the data one column followed by the other column
print(ballet_female_data_ages)
print(ballet_male_data_ages)

#HOMEWORK: How could we print out the two columns next to each other?
#Perhaps a for loop? How would you do it?

#Insert your answer here
merge = pd.concat([ballet_female_data_ages, ballet_male_data_ages], axis=1)
print("Males     Females")
print(merge)
"""
What this will do is specifying axis 1 will concatenate them side by side
rather than stacked, keep in mind that that when the record id mismatches
pandas will fill in a NaN value, functionally this still works though for
examining both dfs side by side though.
"""

#HOMEWORK: Using pandas, compute the mean, mode, standard deviation and variance 
#for the Female Ballet group, the Male Ballet group, the Female Control group and
#the Male Control group. Add this to the above program. Output the information
#in a readable format with headers.

"""
I used the built in functions to find each one of the values. I then put the values in a list 
For example I found the male means for all quantitative columns and then put that in a list. Each 
value in that list corresponds to the age, mass, height, and bmi in that order. I then utilized print statements
to align these and properly format the information so that it is in a readable format as requested.
I also examined both datasets for control and ballet and it seems like these two datasets have the same information in them.
I double checked my work and I used the correct variables so I'm not sure as to whether or not it's supposed to be like that.
"""
headers = ['Age (Years)', 'Body Mass (kg)', 'Body Height (cm)', 'BMI (kg/m2)']

#MALE BALLET
maleMeanAge = "{:.2f}".format(ballet_male_data.mean()[0])
maleMeanMass = "{:.2f}".format(ballet_male_data.mean()[1])
maleMeanHeight = "{:.2f}".format(ballet_male_data.mean()[2])
maleMeanBMI = "{:.2f}".format(ballet_male_data.mean()[3])

maleModeAge =  "{:.2f}".format(ballet_male_data['Age (years)'].mode()[0])
maleModeMass =  "{:.2f}".format(ballet_male_data['Body Mass (kg)'].mode()[0])
maleModeHeight =  "{:.2f}".format(ballet_male_data['Body Height (cm)'].mode()[0])
maleModeBMI =  "{:.2f}".format(ballet_male_data['BMI (kg/m2)'].mode()[0])

maleSTDAge =  "{:.2f}".format(ballet_male_data.std()[0])
maleSTDMass =  "{:.2f}".format(ballet_male_data.std()[1] )
maleSTDHeight =  "{:.2f}".format(ballet_male_data.std()[2])
maleSTDBMI =  "{:.2f}".format(ballet_male_data.std()[3])

maleVarAge =  "{:.2f}".format(ballet_male_data.var()[0])
maleVarMass =  "{:.2f}".format(ballet_male_data.var()[1])
maleVarHeight =  "{:.2f}".format(ballet_male_data.var()[2])
maleVarBMI =  "{:.2f}".format(ballet_male_data.var()[3])

maleMeanList = []
maleModeList = []
maleSTDList = []
maleVarList = []
maleList = []
maleMeanList.append([str(maleMeanAge), str(maleMeanMass), str(maleMeanHeight), str(maleMeanBMI)])
maleModeList.append([str(maleModeAge),str(maleModeMass),str(maleModeHeight),str(maleModeBMI)])
maleSTDList.append([str(maleSTDAge),str(maleSTDMass),str(maleSTDHeight),str(maleSTDBMI)])   
maleVarList.append([str(maleVarAge),str(maleVarMass),str(maleVarHeight),str(maleVarBMI)])   
maleList.append([maleMeanList,maleModeList,maleSTDList,maleVarList])


print("-----------Male Ballet Group Mean-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleMeanList[0]))
print("-----------Male Ballet Group Mode-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleModeList[0]))
print("-----------Male Ballet Group Standard Deviation-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleSTDList[0]))
print("-----------Male Ballet Group Variance-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleVarList[0]))


#MALE CONTROL BALLET
print('\n\n')
maleCMeanAge = "{:.2f}".format(controls_male_data.mean()[0])
maleCMeanMass = "{:.2f}".format(controls_male_data.mean()[1])
maleCMeanHeight = "{:.2f}".format(controls_male_data.mean()[2])
maleCMeanBMI = "{:.2f}".format(controls_male_data.mean()[3])

maleCModeAge =  "{:.2f}".format(controls_male_data['Age (years)'].mode()[0])
maleCModeMass =  "{:.2f}".format(controls_male_data['Body Mass (kg)'].mode()[0])
maleCModeHeight =  "{:.2f}".format(controls_male_data['Body Height (cm)'].mode()[0])
maleCModeBMI =  "{:.2f}".format(controls_male_data['BMI (kg/m2)'].mode()[0])

maleCSTDAge =  "{:.2f}".format(controls_male_data.std()[0])
maleCSTDMass =  "{:.2f}".format(controls_male_data.std()[1] )
maleCSTDHeight =  "{:.2f}".format(controls_male_data.std()[2])
maleCSTDBMI =  "{:.2f}".format(controls_male_data.std()[3])

maleCVarAge =  "{:.2f}".format(controls_male_data.var()[0])
maleCVarMass =  "{:.2f}".format(controls_male_data.var()[1])
maleCVarHeight =  "{:.2f}".format(controls_male_data.var()[2])
maleCVarBMI =  "{:.2f}".format(controls_male_data.var()[3])

maleCMeanList = []
maleCModeList = []
maleCSTDList = []
maleCVarList = []
maleCList = []
maleCMeanList.append([str(maleCMeanAge), str(maleCMeanMass), str(maleCMeanHeight), str(maleCMeanBMI)])
maleCModeList.append([str(maleCModeAge),str(maleCModeMass),str(maleCModeHeight),str(maleCModeBMI)])
maleCSTDList.append([str(maleCSTDAge),str(maleCSTDMass),str(maleCSTDHeight),str(maleCSTDBMI)])   
maleCVarList.append([str(maleCVarAge),str(maleCVarMass),str(maleCVarHeight),str(maleCVarBMI)])   
maleCList.append([maleCMeanList,maleCModeList,maleCSTDList,maleCVarList])

print("-----------Male Control Ballet Group Mean-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleCMeanList[0]))
print("-----------Male Control Ballet Group Mode-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleCModeList[0]))
print("-----------Male Control Ballet Group Standard Deviation-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleCSTDList[0]))
print("-----------Male Control Ballet Group Variance-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*maleCVarList[0]))


#FEMALE BALLET
print('\n\n')
femaleMeanAge = "{:.2f}".format(ballet_female_data.mean()[0])
femaleMeanMass = "{:.2f}".format(ballet_female_data.mean()[1])
femaleMeanHeight = "{:.2f}".format(ballet_female_data.mean()[2])
femaleMeanBMI = "{:.2f}".format(ballet_female_data.mean()[3])

femaleModeAge =  "{:.2f}".format(ballet_female_data['Age (years)'].mode()[0])
femaleModeMass =  "{:.2f}".format(ballet_female_data['Body Mass (kg)'].mode()[0])
femaleModeHeight =  "{:.2f}".format(ballet_female_data['Body Height (cm)'].mode()[0])
femaleModeBMI =  "{:.2f}".format(ballet_female_data['BMI (kg/m2)'].mode()[0])

femaleSTDAge =  "{:.2f}".format(ballet_female_data.std()[0])
femaleSTDMass =  "{:.2f}".format(ballet_female_data.std()[1] )
femaleSTDHeight =  "{:.2f}".format(ballet_female_data.std()[2])
femaleSTDBMI =  "{:.2f}".format(ballet_female_data.std()[3])

femaleVarAge =  "{:.2f}".format(ballet_female_data.var()[0])
femaleVarMass =  "{:.2f}".format(ballet_female_data.var()[1])
femaleVarHeight =  "{:.2f}".format(ballet_female_data.var()[2])
femaleVarBMI =  "{:.2f}".format(ballet_female_data.var()[3])

femaleMeanList = []
femaleModeList = []
femaleSTDList = []
femaleVarList = []
femaleList = []
femaleMeanList.append([str(femaleMeanAge), str(femaleMeanMass), str(femaleMeanHeight), str(femaleMeanBMI)])
femaleModeList.append([str(femaleModeAge),str(femaleModeMass),str(femaleModeHeight),str(femaleModeBMI)])
femaleSTDList.append([str(femaleSTDAge),str(femaleSTDMass),str(femaleSTDHeight),str(femaleSTDBMI)])   
femaleVarList.append([str(femaleVarAge),str(femaleVarMass),str(femaleVarHeight),str(femaleVarBMI)])   
femaleList.append([femaleMeanList,femaleModeList,femaleSTDList,femaleVarList])


print("-----------Female Ballet Group Mean-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleMeanList[0]))
print("-----------Female Ballet Group Mode-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleModeList[0]))
print("-----------Female Ballet Group Standard Deviation-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleSTDList[0]))
print("-----------Female Ballet Group Variance-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleVarList[0]))


#FEMALE CONTROL BALLET
print('\n\n')
femaleCMeanAge = "{:.2f}".format(controls_female_data.mean()[0])
femaleCMeanMass = "{:.2f}".format(controls_female_data.mean()[1])
femaleCMeanHeight = "{:.2f}".format(controls_female_data.mean()[2])
femaleCMeanBMI = "{:.2f}".format(controls_female_data.mean()[3])

femaleCModeAge =  "{:.2f}".format(controls_female_data['Age (years)'].mode()[0])
femaleCModeMass =  "{:.2f}".format(controls_female_data['Body Mass (kg)'].mode()[0])
femaleCModeHeight =  "{:.2f}".format(controls_female_data['Body Height (cm)'].mode()[0])
femaleCModeBMI =  "{:.2f}".format(controls_female_data['BMI (kg/m2)'].mode()[0])

femaleCSTDAge =  "{:.2f}".format(controls_female_data.std()[0])
femaleCSTDMass =  "{:.2f}".format(controls_female_data.std()[1] )
femaleCSTDHeight =  "{:.2f}".format(controls_female_data.std()[2])
femaleCSTDBMI =  "{:.2f}".format(controls_female_data.std()[3])

femaleCVarAge =  "{:.2f}".format(controls_female_data.var()[0])
femaleCVarMass =  "{:.2f}".format(controls_female_data.var()[1])
femaleCVarHeight =  "{:.2f}".format(controls_female_data.var()[2])
femaleCVarBMI =  "{:.2f}".format(controls_female_data.var()[3])

femaleCMeanList = []
femaleCModeList = []
femaleCSTDList = []
femaleCVarList = []
femaleCList = []
femaleCMeanList.append([str(femaleCMeanAge), str(femaleCMeanMass), str(femaleCMeanHeight), str(femaleCMeanBMI)])
femaleCModeList.append([str(femaleCModeAge),str(femaleCModeMass),str(femaleCModeHeight),str(femaleCModeBMI)])
femaleCSTDList.append([str(femaleCSTDAge),str(femaleCSTDMass),str(femaleCSTDHeight),str(femaleCSTDBMI)])   
femaleCVarList.append([str(femaleCVarAge),str(femaleCVarMass),str(femaleCVarHeight),str(femaleCVarBMI)])   
femaleCList.append([femaleCMeanList,femaleCModeList,femaleCSTDList,femaleCVarList])

print("-----------Female Control Ballet Group Mean-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleCMeanList[0]))
print("-----------Female Control Ballet Group Mode-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleCModeList[0]))
print("-----------Female Control Ballet Group Standard Deviation-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleCSTDList[0]))
print("-----------Female Control Ballet Group Variance-------------")
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*headers))
print('{:>12}  {:>12}  {:>12}  {:>12}'.format(*femaleCVarList[0]))

