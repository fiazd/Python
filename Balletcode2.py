"""
Daanish Fiaz
CMSC 391 
Linear Regression HW
"""
import pandas as pd #imports Pandas and assigns the worksheet to the name  pd
import numpy as np  #imports the numpy module and assigns it to the name np
from numpy import cov
from scipy import stats #imports the scipy library
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt #imports the plot library
import seaborn as sns;sns.set(color_codes=True)

#In Part 2 of the Ballet assignment, you will be learning how to perform some basic 
#statistical calculations. As we will need some of the code from the previous part,
#I am just going to keep the code that we have already written for Part 1 and I will
#add to it to create Part 2 of the assignment.
df = pd.read_csv('Book1.csv')

#Set up some display features for when it prints to the screen or to a file
pd.set_option('display.max_columns',None) 
pd.set_option('display.max_colwidth',-1) 

# display basic file structure information
# print(df)
print(f'\n ------ Print Header Information')
print(df.head(0)) 
print(df.head()) 
print(df.head(2))

print(f'\n ------ Basic dataframe properties')
print(df.count()) 
print('Number of lines is ', len(df)) 
print('Matrix shape = ',df.shape)

# Now we obtain some information about the contents of the dataframe.
print(f'\n ------ Basic dataframe counts')
print(df.columns) 
print('number of unique group ids in list=',df["Group"].nunique())
print('number of unique sex ids in list=',df["Sex"].nunique())
print(f'{"Group":<12}Number')
print(df["Group"].value_counts())
print(f'\n') 

print(f'{"Sex":<5}Number')
print(df["Sex"].value_counts().sort_index())

gk = df.groupby('Group')
print(gk["Sex"].value_counts().sort_index())


gk.get_group('Ballet')
gk.get_group('Controls')
gkk = df.groupby(['Group', 'Sex'])
print(gkk.describe())

ballet_female_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="F")]
ballet_male_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="M")]
ballet_female_data=df[(df["Group"]=="Controls") & (df["Sex"]=="F")]
ballet_male_data=df[(df["Group"]=="Controls") & (df["Sex"]=="M")]
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="M")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="M")])

controls_female_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="F")]
controls_male_data=df[(df["Group"]=="Ballet") & (df["Sex"]=="M")]
controls_female_data=df[(df["Group"]=="Controls") & (df["Sex"]=="F")]
controls_male_data=df[(df["Group"]=="Controls") & (df["Sex"]=="M")]
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Ballet") & (df["Sex"]=="M")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="F")])
print(df[(df["Group"]=="Controls") & (df["Sex"]=="M")])

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


print(ballet_female_data_ages)
print(ballet_male_data_ages)

#Adding statistical analyses to the Ballet code.
print('\n Statistics for female ballet age')
print (ballet_female_data_ages.describe(),'\n')
print('\n Statistics for male ballet age')
print(ballet_male_data_ages.describe())

#I can also use the specific statistical variable I want to see. For example,
#if I wanted to list the means of the ballet male and female ages data,
#would print the following:
print('\n mean value of ballet female ages = ',ballet_female_data_ages.mean())
print('mean value of ballet male ages = ',ballet_male_data_ages.mean())

#QUESTION: Insert code to output the following information:
#(1) The basic statistics for the controls male and female variable=ages
#(2) Print the results
#(3) Read about Pandas and calculating statistics in Python with Pandas
#(4) Insert code to print out the mean values for the control male and female ages
#(5) Print the results
#(6) Repeat items (4) and (5) only print out the standard deviation for the control
#    male and female ages

#MAKE SURE TO INSERT YOUR CODE AFTER THIS LINE
#basic statistics for male and female ballet ages
print('\nStatistics for control female ballet age')
print(controls_female_data_ages.describe())
print('\nStatistics for control male ballet age')
print(controls_male_data_ages.describe())
#mean for controls
control_mean_female_ages = controls_female_data_ages.describe()[1]
control_mean_male_ages = controls_male_data_ages.describe()[1]
print('Mean control female ballet age is: ',control_mean_female_ages)
print('Mean control male ballet age is: ', control_mean_male_ages)

#std for control male and female
control_std_female_ages = controls_female_data_ages.describe()[2]
control_std_male_ages = controls_male_data_ages.describe()[2]
print('\nStandard deviation for female ballet age is ', control_std_female_ages)
print('Standard deviation for male ballet age is ', control_std_male_ages)

#We have looked at some basic statistics; mean, mode, variance, standard deviation, etc.
#Now we want to perform some statistical analyses. For example, we might want to know 
#if the mean ages of the ballet men is statistically the same as the mean age of the 
#controls men.There are different ways to do this. The first way is to perform a 
#correlation between the two variables. We do this as follows:

#Here we calculate the Pearson correlation between the ballet and the control female ages
print('\n ---------- Begin Statistical Correlation Calculation Example')
pearson_female_age_corr, _=pearsonr(ballet_female_data_ages,controls_female_data_ages)
print('Pearsons correlation: %.3f' % pearson_female_age_corr)
#Here we calculate the Spearman correlation between the ballet and the control female ages
spearman_female_age_corr, _=spearmanr(ballet_female_data_ages,controls_female_data_ages)
print('Spearmans correlation: %.3f' % spearman_female_age_corr)

print('\n ---------- Begin Statistical Covariance Calculation Example')
#Here we calculate the covariance between the ballet female age groups; control vs. ballet
covariance_female_ages=cov(ballet_female_data_ages,controls_female_data_ages)
print("Female age covariance = ",covariance_female_ages)
covariance_male_ages=cov(ballet_male_data_ages,controls_male_data_ages)
print("Male age covariance = ",covariance_male_ages)

#Here we calculate the Pearson correlation between the ballet female ages and
#their weight
print('\n ---------- Begin Statistical Correlation Calculations Between Female Ballet Age and BodyMass')  
pearson_female_age_mass_corr, _=pearsonr(ballet_female_data_ages,ballet_female_data_bodymass)
print('Pearsons correlation: %.3f' % pearson_female_age_mass_corr)
#Here we calculate the Spearman correlation Between the Ballet and the Control Female Ages
spearman_female_age_mass_corr, _=pearsonr(ballet_female_data_ages,ballet_female_data_bodymass)
print('Spearmans correlation: %.3f' % spearman_female_age_mass_corr)

# HOMEWORK: REPEAT THIS FOR MALE AGES VS BODY MASS. INSERT CODE AFTER THIS LINE
print('\n ---------- Begin Statistical Correlation Calculations Between Male Ballet Age and BodyMass')
pearson_male_age_mass_corr, _=pearsonr(ballet_male_data_ages,ballet_male_data_bodymass)
print('Pearsons correlation: %.3f' % pearson_male_age_mass_corr)
spearman_male_age_mass_corr, _=pearsonr(ballet_male_data_ages,ballet_male_data_bodymass)
print('Spearmans correlatio: %.3f' % spearman_male_age_mass_corr)



print('\n ---------- Begin Statistical Covariance Calculations between the two groups ages')  
#Here we calculate the covariance between the ballet female ages
covariance_female_ages=cov(ballet_female_data_ages,controls_female_data_ages)
print("Female age covariance = ",covariance_female_ages)
covariance_male_ages=cov(ballet_male_data_ages,controls_male_data_ages)
print("Male age covariance = ",covariance_male_ages)

#Many of the Panda modules require a simple dataset containing just the two 
#columns that you want to analyze. There are all sorts of fancy ways of
#extracting data from the original dataframe  df. What I am going to do is to
#show you how to create a new data frame from two data vectors (or series as
#they are called in Python).
data_dict={'x':ballet_female_data_ages,'y':ballet_female_data_bodymass}
dframe=pd.DataFrame(data_dict)
print(dframe)
dframe1=pd.concat([ballet_female_data_ages,ballet_female_data_bodymass],axis=1)
dframe1.columns=['ballet_female_data_ages','ballet_female_data_bodymass']
print(dframe1)

#Now that we are done making the new dataframe, let's do a simple scatter
#plot just to see what the data looks like for our two variables that are
#being plotted against each other. NOTE: This will plot a pop-up image. You
#have to kill the plot window in order to go to the next part of the program.
dframe1.plot(x='ballet_female_data_ages',y='ballet_female_data_bodymass',style='o')
plt.title('ballet_female_data_ages vs. ballet_female_data_bodymass')
plt.xlabel('ballet_female_ages')
plt.ylabel('ballet_female_bodymass')
plt.show()
plt.close()
#Obviously, there are many plot options and you are encouraged to explore what
#is possible.

#HOMEWORK: (1) Repeat the above dataframe construction for the male age and body mass
#and plot the result. (2) Create a plot with both male and female data plotted on it.
#Make sure to use a different symbol for each dataset and print a legend so that I 
#know which symbol is for which group.

#df construction and plot for male age and body mass
male_age_mass_dict = {'x':ballet_male_data_ages,'y':ballet_male_data_bodymass}
male_df = pd.DataFrame(male_age_mass_dict)
print(male_df)
male_df1 = pd.concat([ballet_male_data_ages,ballet_male_data_bodymass], axis = 1)
male_df1.columns = ['ballet_male_data_ages','ballet_male_data_bodymass']
print(male_df1)
print(f'Ballet Male Ages vs Ballet Male BodyMass')
male_df1.plot(x = 'ballet_male_data_ages', y = 'ballet_male_data_bodymass', style = 'o')
plt.title('ballet_male_data_ages vs. ballet_male_data_bodymass')
plt.xlabel('ballet_male_ages')
plt.ylabel('ballet_male_bodymass')
plt.show()

#plot for both male (male_df1) and female (dframe1)
#use different labels for male and female, maybe colors too?
#print legend too
print('\nBallet Ages vs Ballet Body Mass')
ax = male_df1.plot(marker = 'o', color = '#3389ff', linestyle = 'None')
dframe1.plot(ax = ax, marker = 'o',color = '#ff33fb', linestyle = 'None')
plt.title('Ballet Ages vs. Ballet Body Mass')
plt.xlabel('Ballet Age')
plt.ylabel('Ballet BodyMass')
plt.ylim(0,100)
plt.xlim(20,50)
ax.legend(loc = 'upper center', bbox_to_anchor = (1.35, 0.8))
plt.show()



#In your Zybook, you read about linear regression as a beginning way to understand
#potential relationships between variables. Using out the previous data, we can
#use a simple canned routine called lingress which is stored in the stats module of
#scipy. It prints out the basic regression values. I have illustrated it below.
slope, intercept, r_value, p_value, std_err = stats.linregress(ballet_female_data_ages,ballet_female_data_bodymass)
print(f'\n')
print(f'Female Regression Stats')
print(f'regression slope = ',slope)
print(f'regression intercept = ',intercept)
print(f'regression rvalue = ',r_value)
r_squared=r_value*r_value
print(f'regression r_squared = ',r_squared)
print(f'regression p_value = ',p_value)
print(f'regression std_error = ',std_err)
print(f'\n')

#You can see from the previous output that the regression claims that there is
#a negative relationship between the two variables. However, we note that the
#r_squared variable is so small that the regression does not account for much
#of the overall data variation. Further, the p_value is >0.05. Consequently, we
#would reject the fitting as meaningful.

#It would be nice to see how the data scatters around the regression line. Often,
#visualizing the data (which we will talk about in the upcoming assignment) tells
#us quite a bit. So here is a very simple way to plot the data scatter and the
#fitted regression line.
print(f'\nFemale Regression Plot')
plt.plot(ballet_female_data_ages, ballet_female_data_bodymass, 'o', label='original data')
plt.plot(ballet_female_data_ages, intercept + slope*ballet_female_data_ages, 'r', label='fitted line')
plt.legend()
plt.show()

#HOMEWORK: (1) Repeat the above dataframe construction for the male age and body mass
#and plot the result. (2) Create a plot with both male and female data plotted on it.
#Make sure to use a different symbol for each dataset and print a legend so that I 
#know which symbol is for which group.
mslope, mintercept, mr_value, mp_value, mstd_err = stats.linregress(ballet_male_data_ages,ballet_male_data_bodymass)
print(f'\n')
print(f'Male Regression Stats')
print(f'regression slope = ',mslope)
print(f'regression intercept = ',mintercept)
print(f'regression rvalue = ',mr_value)
mr_squared=mr_value*mr_value
print(f'regression r_squared = ',mr_squared)
print(f'regression p_value = ',mp_value)
print(f'regression std_error = ',mstd_err)
print(f'\n')

#HOMEWORK: (1) Create a plot for the regression line and data scatter associated
#with the regression fit to the data. the male age and male body mass
#and plot the result. (2) Create a plot with both male and female data plotted on it.
#Make sure to use a different symbol for each dataset and print a legend so that I 
#know which symbol is for which group. I should be able to see both regression lines 
#the data scatter for each female/male dataset.
print(f'\nMale Regression Plot')
plt.plot(ballet_male_data_ages, ballet_male_data_bodymass, 'o', label='original data')
plt.plot(ballet_male_data_ages, mintercept + mslope*ballet_male_data_ages, 'r', label='fitted line')
plt.legend()
plt.show()

#plot with both male and female data plotted in it
print(f'\nMale and Female Regression Plot')
plt.plot(ballet_male_data_ages, ballet_male_data_bodymass, 'o', label='male original data', color = '#3389ff')
plt.plot(ballet_male_data_ages, mintercept + mslope*ballet_male_data_ages, 'b', label='male fitted line')
plt.plot(ballet_female_data_ages, ballet_female_data_bodymass, 'o', label='female original data', color = '#ff33fb')
plt.plot(ballet_female_data_ages, intercept + slope*ballet_female_data_ages, 'r', label='female fitted line')
plt.legend()
plt.show()
#In the next and last part of this statistical analysis series, we will examine
#some more simple yet sophisticated ways of understanding relationships between
#variables. For the purposes of this class, we will just compare between two
#different data series.

print('\n --------------------------- END OF PROGRAM ---------------') 




