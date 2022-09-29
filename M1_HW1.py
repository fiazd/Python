#Daanish Fiaz Module 1 HomeWork 1
#Data Science 391 1/31/20
import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt 
import scipy.stats as st
import statsmodels.formula.api as smf
import statsmodels.api as sm
import seaborn as sns;sns.set(color_codes=True)
from numpy import cov
from scipy import stats
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression


# Input dataset called tips.csv
#
df = pd.read_csv('tips.csv')

# Set up some terminal display options
pd.set_option('display.max_columns',None) 
pd.set_option('display.max_colwidth',-1) 


print(f'\n ------ Print Header Information -----------')
print(df.columns.values.tolist()) 
print(f'\n ------ Print First 3 lines of the Data Frame -----------')
print(df[0:3][:])
print(f'\n ------ Print Last 3 lines of the Data Frame -----------')
print(df[-4:-1][:])

print(f'\n ------ Basic dataframe properties')
print() 
print('Number of lines is ', len(df)) 
print('Matrix shape = ', df.shape)

print(f'\n ------ Basic dataframe counts ---------')
print(df.columns) 
print('number of unique sex ids in list=', len(df.sex.unique().tolist()))
print('number of unique smoker ids in list=',len(df.smoker.unique().tolist()))
print(f'{"sex":<9}Number')
print()
print(f'\n') 

print(f'{"smoker":<7}Number')
print(df["smoker"].value_counts().sort_index())

gk = df.groupby('sex')
print(gk["smoker"].value_counts().sort_index())

print('\n ----- Hierarchical breakdown of data -------- ')
print('\n')
gk.get_group('Male')
gk.get_group('Female')
gkk = df.groupby(['sex', 'smoker'])
print(gkk.describe())

#
print('\n')
print('---------------- Dropping Unused Columns --------------')
# create a dataframe in which you have dropped the day, time, size
deleted_df= df.drop(['day','time','size'], axis = 1)
print(deleted_df.head())
print(deleted_df.shape)

# Create dataframes that contain smoker yes/no data for make and female
#Should only contain sex and smoker
smoke_female_data= df[(df.sex == 'Female') & (df.smoker == 'Yes')]
smoke_male_data= df[(df.sex == 'Male') & (df.smoker == 'Yes')]
nosmoke_female_data= df[(df.sex == 'Female') & (df.smoker == 'No')]
nosmoke_male_data= df[(df.sex == 'Male') & (df.smoker == 'No')]
smoke_female_data.drop(df.columns.difference(['sex','smoker']), 1, inplace=True)
smoke_male_data.drop(df.columns.difference(['sex','smoker']), 1, inplace=True)
nosmoke_female_data.drop(df.columns.difference(['sex','smoker']), 1, inplace=True)
nosmoke_male_data.drop(df.columns.difference(['sex','smoker']), 1, inplace=True)

# I put a print statement in here just to make sure that I was
# getting the data correctly. I have commented it out. You should
# uncomment it until you are sure that you are getting the correct
# output.
#
print('\n -----------------------------------------------')
print('         Printing smoke_female/male_data')
print()
print('\n -----------------------------------------------')

#
# I have done this programming in a very straightforward way. However,
# a good programmer would have just used commands to interact directly
# with the initial dataframe and not created all of these subframes.
#I did the same thing as with the nontip data, just didn't drop the tips column this time
smoke_female_data_tip= df[(df.sex == 'Female') & (df.smoker == 'Yes')]
smoke_male_data_tip= df[(df.sex == 'Male') & (df.smoker == 'Yes')]
nosmoke_female_data_tip= df[(df.sex == 'Female') & (df.smoker == 'No')]
nosmoke_male_data_tip= df[(df.sex == 'Male') & (df.smoker == 'No')]
smoke_female_data_tip.drop(df.columns.difference(['sex','smoker', 'tip']), 1, inplace=True)
smoke_male_data_tip.drop(df.columns.difference(['sex','smoker', 'tip']), 1, inplace=True)
nosmoke_female_data_tip.drop(df.columns.difference(['sex','smoker', 'tip']), 1, inplace=True)
nosmoke_male_data_tip.drop(df.columns.difference(['sex','smoker', 'tip']), 1, inplace=True)


 

# Understanding some of the problems that can happen in simple databases. For
# example, null cells or problems with data in a cell NAN for example. So the first
# things that you need to do are to clean up your data. And the following are some
# of the most commonly used commands.
#
# Some other useful commands for beginning your exploratory data analysis
# (1) Import that dataset and then print out a number of lines. For example, 
#     head(10). This will help you to make sure that you read in the
#     correct data and it will give you the header column names.
# (2) Next find out about your data with commands like data.shape() which
#     tells you the number of rows and columns in the dataset.
# (3) After number (2), we look for the number of empties in each column.
#     These are called null values. We use the command data.isnull().sum

print(df.columns) # returns column headings
print(df.shape) # number of rows x columns in the dataframe
print(df.isnull().sum())# number of null entries (empty)
print(df.info()) # what kind of variable each item in the dataframe is
print(df.count()) #non-null values in each column
print(df.describe()) # basic information on values in each column


# Note that the above operators work only on columns that are numeric so
# you will not get information about columns that contain string data.

print('\n --------------------------- END OF PROGRAM -----------------')




