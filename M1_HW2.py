#M1_HW2
#Daanish Fiaz CMSC 391

import pandas as pd
import numpy as np

#1. Read in the dataset
#acs_ny.csv
df = pd.read_csv('acs_ny.csv')

#determine basic properties of dataset shape, existence of null variables
#(22745 rows, 18 columns), haven't seen any null variables
#utilized notnull and isnull and both determined that there aren't any null or NaN values

#df.shape
#print(df.notnull().values.any())

#output header variable names
df_head = list(df.columns.values)
print('Column Names')
for name in df_head:
    print(name + " ", end = '')
print("" , end = "\n")

#Output the 'type for each of the columns
print("Types of the Columns")
print(df.dtypes)
#there are multiple objects and integers in the dataframe
print('-------------------------------------------------------------')

#create new datafile called NewFamilyType which has the sorted values of
#FamilyType
#Select the family type, put that in new df
#Then sort that df
familyTypeOnly = df.FamilyType
sortFTO = familyTypeOnly.sort_values()
#Now we have to create a new datafile called NewFamilyType
header = ['IDs','FamilyType']
#Created csv datafile that contains sortFTO (single column)
sortFTO.to_csv(r'NewFamilyType.csv', header = 'FamilyType')

#Output the first five lines and the last five lines of the dataset
print(df.head())
print(df.tail())

print('-------------------------------------------------------------')
#Determine how many unique var names are in the acres columns
acresList = df['Acres'].unique().tolist()
print('The number of unique variable names in acres is: ' + str(len(acresList)))
#Determine how many unique var names are in the FamilyType
famTypeList = df['FamilyType'].unique().tolist()
print('The number of unique vairable names in FamilyType is: ' + str(len(famTypeList)))

#Group FamilyType x Number of Bedrooms and comment what you found
gDF = df[['FamilyType','NumBedrooms']]
groupedDF = gDF.groupby(['FamilyType','NumBedrooms'])

#for key, item in groupedDF:
    #print(groupedDF.get_group(key), "\n\n")
"""
When there is a female head the most common number of bedrooms
is 1630 occurences with 3 bedrooms
The least common
is 4 occurences with 0 bedrooms.

When there is a male head
most common number of bedrooms is: 3 (571 occurences)
least common number of bedrooms is: 0 (3 occurences)

When married
most common number of bedrooms is: 3 (8832 occurences)
followed closely by 4 bedrooms (5413) and 2 bedrooms (2105)
least common number of bedrooms is: 0 (26 occurences)
"""
print('-------------------------------------------------------------')
#remove column labeled Family Income and output the header list to show that it is gone
dropFI = df.drop(columns = ['FamilyIncome'])
newColumnLabels = list(dropFI.columns.values)
print(newColumnLabels) #FamilyIncome is not in this list 

#Create new dataframe called new_df, extract FamilyType and NumPeople to new_df in one line
new_df = df[['FamilyType','NumPeople']]

# what does .nunique do
#
#obtain how many people who own or rent also do or do not use FoodStamps.
#OwnRent or FoodStamp or NumPeople
print('-------------------------------------------------------------')

new_df2 = df[['OwnRent','FoodStamp','NumPeople']]
groupedDF2 = new_df2.groupby(['OwnRent','FoodStamp'])
#print(new_df2.nunique())
#nunique just returns the number of unique values for each column
#OwnRent is 3 unique vals, FoodStamp is 2 unique vals
#and NumPeople has 15 unique values
for key, item in groupedDF2:
    print(groupedDF2.get_group(key)[0:1][:]) 
    print('The number of people in this category is: ' + str(groupedDF2.get_group(key).NumPeople.sum()),'\n\n')
"""
I summed the numpeople for each family to get the total number of people within the family

Mortgage No Foodstamp: 63451 People
Mortgage Yes FoodStamp: 4234 People

Outright No Foodstampe: 329 People
Outright Yes FoodStamp 28 People

Rented No FoodStamp: 5855
Rented Yes FoodStamp: 3219 People
"""
