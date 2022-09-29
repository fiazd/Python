"""
Daanish Fiaz
CMSC 391
Final Project
COVID - 19
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Module 1: Wrangling and describing dataframe properties

#import datasets
confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered = pd.read_csv('time_series_covid19_recovered_global.csv')

#header of each dataset
print('Confirmed Column Names: ')
print(confirmed.columns.values)
print('\n Deaths Column Names: ')
print(deaths.columns.values)
print('\n Recovered Column Names: ')
print(recovered.columns.values)


#Top 3 lines and bottom 3 lines of each dataset
print('\n First 3 and last 3 of Confirmed')
print(confirmed.head(3))
print(confirmed.tail(3))

print('\n first 3 and last 3 of deaths')
print(deaths.head(3))
print(deaths.tail(3))

print('\n first 3 and last 3 of recovered')
print(recovered.head(3))
print(recovered.tail(3))

#dimensions of each dataset
print('\nDimensions of confirmed is: ' + str(confirmed.shape))
print('Dimensions of deaths is: ' + str(deaths.shape))
print('Dimensions of recovered is: ' + str(recovered.shape))

#number of missing values in each dataset
print('\nNumber of missing values confirmed: ' + str(confirmed.isnull().sum().sum()))
print('Number of missing values deaths: ' + str(deaths.isnull().sum().sum()))
print('Number of missing values recovered: ' + str(recovered.isnull().sum().sum()))

#How would you handle where data is missing?
#if we don't want the values we could remove them, missing data
#may or may not be useful so we would examine the data and determine what analysis
#we are doing then decide whether or not the missing data affects that analaysis

#report how many countries have multiple regions reported
mC = confirmed.pivot_table(index = ['Country/Region'], aggfunc = 'size')
mC = pd.DataFrame(mC)
mC = mC[mC[0] != 1]
print('\nCountries with multiple regions: ')
print(len(mC.index.values))
#Australia, Canada, China, Denmark, France, Netherlands, United Kingdom

#new data frames that contain data not broken down by regions
newconfirmed = confirmed.groupby(['Country/Region']).agg('sum').reset_index()
newdeaths = deaths.groupby(['Country/Region']).agg('sum').reset_index()
newrecovered = recovered.groupby(['Country/Region']).agg('sum').reset_index()

#They are in alphabetical order

#types for each variable
print('\nTypes of Variables for confirmed, deaths, and recovered: ')
typesconfirmed = newconfirmed.dtypes
typecarr = []
for i in typesconfirmed:
    typecarr.append(i)
    
typesdeaths = newdeaths.dtypes
typedarr = []
for i in typesdeaths:
    typedarr.append(i)

typesrecovered = newrecovered.dtypes
typerarr = []
for i in typesrecovered:
    typerarr.append(i) 
    
for i in range(0, len(typecarr)):
    print(str(typecarr[i]) + "\t" + str(typedarr[i]) + "\t" + str(typerarr[i]))
    
#dataframes for US, France, and Italy
usdfconfirmed = newconfirmed[newconfirmed['Country/Region'] == 'US']
usdfdeaths = newdeaths[newdeaths['Country/Region'] == 'US']
usdfrecovered = newrecovered[newrecovered['Country/Region'] == 'US']

francedfconfirmed = newconfirmed[newconfirmed['Country/Region'] == 'France']
francedfdeaths = newdeaths[newdeaths['Country/Region'] == 'France']
francedfrecovered = newrecovered[newrecovered['Country/Region'] == 'France']

italydfconfirmed = newconfirmed[newconfirmed['Country/Region'] == 'Italy']
italydfdeaths = newdeaths[newdeaths['Country/Region'] == 'Italy']
italydfrecovered = newrecovered[newrecovered['Country/Region'] == 'Italy']

#cumulative sum for all three countries
#us
cum_us_confirmed = usdfconfirmed.iloc[:,3:].cumsum(axis = 1)
cum_us_confirmed.insert(loc = 0, column = 'Country/Region', value = ['US'])
cum_us_deaths = usdfdeaths.iloc[:,3:].cumsum(axis = 1)
cum_us_deaths.insert(loc = 0, column = 'Country/Region', value = ['US'])
cum_us_recovered = usdfrecovered.iloc[:,3:].cumsum(axis = 1)
cum_us_recovered.insert(loc = 0, column = 'Country/Region', value = ['US'])

#france
cum_france_confirmed = francedfconfirmed.iloc[:,3:].cumsum(axis = 1)
cum_france_confirmed.insert(loc = 0, column = 'Country/Region', value = ['France'])
cum_france_deaths = francedfdeaths.iloc[:,3:].cumsum(axis = 1)
cum_france_deaths.insert(loc = 0, column = 'Country/Region', value = ['France'])
cum_france_recovered = francedfrecovered.iloc[:,3:].cumsum(axis = 1)
cum_france_recovered.insert(loc = 0, column = 'Country/Region', value = ['France'])

#italy
cum_italy_confirmed = italydfconfirmed.iloc[:,3:].cumsum(axis = 1)
cum_italy_confirmed.insert(loc = 0, column = 'Country/Region', value = ['Italy'])
cum_italy_deaths = italydfdeaths.iloc[:,3:].cumsum(axis = 1)
cum_italy_deaths.insert(loc = 0, column = 'Country/Region', value = ['Italy'])
cum_italy_recovered = italydfrecovered.iloc[:,3:].cumsum(axis = 1)
cum_italy_recovered.insert(loc = 0, column = 'Country/Region', value = ['Italy'])


#Module 2: Statistical Analysis
#for Thailand, Singapore, and Malaysia
#report he mean number/day of confirmed, deaths, recovered
#mean confirmed 
print('\nMean number/day of confirmed cases')
thailandc = newconfirmed[newconfirmed['Country/Region'] == 'Thailand']
singaporec = newconfirmed[newconfirmed['Country/Region'] == 'Singapore']
malaysiac = newconfirmed[newconfirmed['Country/Region'] == 'Malaysia']
print('Thailand: ' + str(thailandc.iloc[:,3:].mean(axis = 1)))
print('Singapore: ' + str(singaporec.iloc[:,3:].mean(axis = 1)))
print('Malaysia: ' + str(malaysiac.iloc[:,3:].mean(axis = 1)))

#mean deaths 
print('\nMean number of day deaths')
thailand_deaths = newdeaths[newdeaths['Country/Region'] == 'Thailand']
singapore_deaths = newdeaths[newdeaths['Country/Region'] == 'Singapore']
malaysia_deaths = newdeaths[newdeaths['Country/Region'] == 'Malaysia']
print('Thailand: ' + str(thailand_deaths.iloc[:,3:].mean(axis = 1)))
print('Singapore: ' + str(singapore_deaths.iloc[:,3:].mean(axis = 1)))
print('Malaysia: ' + str(malaysia_deaths.iloc[:,3:].mean(axis = 1)))

#mean recovered
print('\nMean number of day recovered')
thailand_recovered = newrecovered[newrecovered['Country/Region'] == 'Thailand']
singapore_recovered = newrecovered[newrecovered['Country/Region'] == 'Singapore']
malaysia_recovered =  newrecovered[newrecovered['Country/Region'] == 'Malaysia']
print('Thailand: ' + str(thailand_recovered.iloc[:,3:].mean(axis = 1)))
print('Singapore: ' + str(singapore_recovered.iloc[:,3:].mean(axis = 1)))
print('Malaysia: ' + str(malaysia_recovered.iloc[:,3:].mean(axis = 1)))

#is there a significant differentce between confirmed recovered and deaths for
#singapore and malaysia
#For confirmed, they're about 700 apart so there is a significant difference
#for deaths, they're 26 apart and this is over the course of several moths so this is not significant
#for recovered, theyre about 600 recovered apart so there is a significant difference

"""
14A. They are 500 apart so somewhat of a linear relation ship but not really.
14B. They are 700 apart so not a linear releationship at all for deaths
14C. They are 26 apart so this is a lot closer to a linear relationship than the others
"""

#is there a linear relationship between:

#confirmed in singapore and confirmed in thailand
thailandcgraph = thailandc.T.iloc[3:,:].plot.line()
singapoecgraph = singaporec.T.iloc[3:,:].plot.line()
"""
15A.) there seems to be someowhat of a relationship but it's inconclusive.
    this is because the cases go up in singapore first then the cases go up in thailand
    however, there may be a lot of travel between the two places so there definitely is a correlation
    a better explanation for these would be more exponential though, due to the shape of the cuves spikes
"""

#recovered
thailandrraph = thailand_recovered.T.iloc[3:,:].plot.line()
singaporergraph = singapore_recovered.T.iloc[3:,:].plot.line()

"""
15B.) linear relationship between deaths in singapore and thailand
    Yes there does appear to be a linear relationship that is most prevalent between deaths in both countries
    This may be because of the average time a person has left once infected with covid 19

"""

#deaths in singapore and deaths in thailand
thailanddgraph = thailand_deaths.T.iloc[3:,:].plot.line()
singaporedgraph = singapore_deaths.T.iloc[3:,:].plot.line()
"""
15C.)Linear relationship between singpore and thailand deaths?
    There is more of a direct relationship between the two because 
    deaths start rising in late march for both countries
    this is more linear than that of confirmed 
15d.) Overall, I would say confirmed is exponential, deaths are linear
    and recovered can be based upon different factors like the population density,
    transmission rate, hospital care, hospital limitations, etc. based by country.
"""

#MODULE 3: Graphics and Visualization


#use US France and Italy
#create an axes labeled and titled plot 
#cum_us_confirmed cum_us_deaths cum_us_recovered
#US
cum_us_confirmed = cum_us_confirmed.T
cum_us_deaths = cum_us_deaths.T
cum_us_recovered = cum_us_recovered.T
temp = pd.concat([cum_us_confirmed, cum_us_deaths, cum_us_recovered], axis = 1)
temp.columns = ['confirmed', 'deaths', 'recovered']
finalus = temp.iloc[1:,:]
ax1 = finalus.plot(title = 'Cumulative US COVID 19')
ax1.set_xlabel('Date')
ax1.set_ylabel('Cases (10s of millions)')
#10s of millions for example cumulative us covid is about 25 million

#France
cum_france_confirmed = cum_france_confirmed.T
cum_france_deaths = cum_france_deaths.T
cum_france_recovered = cum_france_recovered.T
temp = pd.concat([cum_france_confirmed, cum_france_deaths, cum_france_recovered], axis = 1)
temp.columns = ['confirmed', 'deaths', 'recovered']
finalfrance = temp.iloc[1:,:]
ax1 = finalfrance.plot(title = 'Cumulative France COVID 19')
ax1.set_xlabel('Date')
ax1.set_ylabel('Cases')

#Italy
cum_italy_confirmed = cum_italy_confirmed.T
cum_italy_deaths = cum_italy_deaths.T
cum_italy_recovered = cum_italy_recovered.T
temp = pd.concat([cum_italy_confirmed, cum_italy_deaths, cum_italy_recovered], axis = 1)
temp.columns = ['confirmed', 'deaths', 'recovered']
finalitaly = temp.iloc[1:,:]
ax1 = finalitaly.plot(title = 'Cumulative Italy COVID 19')
ax1.set_xlabel('Date')
ax1.set_ylabel('Cases')

#plot for confirmed us, italy, and france
temp = pd.concat([cum_us_confirmed, cum_france_confirmed, cum_italy_confirmed], axis = 1)
temp.columns = ['US', 'France', 'Italy']
finalconfirmed = temp.iloc[1:,:]
ax1 = finalconfirmed.plot(title = 'Cumulative Confirmed US, France, and Italy')
ax1.set_xlabel('Date')
ax1.set_ylabel('Cases')

#plot for death us, italy, and france
temp = pd.concat([cum_us_deaths, cum_france_deaths, cum_italy_deaths], axis = 1)
temp.columns = ['US', 'France', 'Italy']
finaldeaths = temp.iloc[1:,:]
ax1 = finaldeaths.plot(title = 'Cumulative deaths US, France, and Italy')
ax1.set_xlabel('Date')
ax1.set_ylabel('Cases')

#plot for recovered us, italy, and france
temp = pd.concat([cum_us_recovered, cum_france_recovered, cum_italy_recovered], axis = 1)
temp.columns = ['US', 'France', 'Italy']
finalrecovered = temp.iloc[1:,:]
ax1 = finalrecovered.plot(title = 'Cumulative recovered US, France, and Italy')
ax1.set_xlabel('Date')
ax1.set_ylabel('Cases')


"""
What does this say about COVID 19?
There is a clear exponential growth of confirmed cases in us, france, and italy
deaths and recovered are exponential at first but then level off to be linear.
This also can say that COVID-19 is a pandemic.
The graph for cumulative deaths is interesting because italy starts spiking first, but then
the US spikes past italy, showing it has a higher rate of exponential growth.
Also interesting to see how in the recovered graph, us starts behind italy, but then passes it,
this may demonstrate the exponential increase that the US has as well as it might be linked
to the higher capacity healthcare system we have than italy.
"""
#16D. Create bar chart for each country and put all in one
#bar chart with each country next to each other
#get maxes first
#us maxes
cum_usconfirmedmax = finalus['confirmed'].max()
cum_usdeathsmax = finalus['deaths'].max()
cum_usrecoveredmax = finalus['recovered'].max()

#france maxes
cum_franceconfirmedmax = finalfrance['confirmed'].max()
cum_francedeathsmax = finalfrance['deaths'].max()
cum_francerecoveredmax = finalfrance['recovered'].max()

#italy maxes
cum_italyconfirmedmax = finalitaly['confirmed'].max()
cum_italydeathsmax = finalitaly['deaths'].max()
cum_italyrecoveredmax = finalitaly['recovered'].max()
#reorganize to make alphabetical
cum_data = {'Confirmed' : [cum_franceconfirmedmax, cum_italyconfirmedmax, cum_usconfirmedmax],
            'Deaths' : [cum_francedeathsmax, cum_italydeathsmax, cum_usdeathsmax],
            'Recovered' : [cum_francerecoveredmax, cum_italyrecoveredmax, cum_usdeathsmax]}
index = ['France', 'Italy', 'US']
cumbar = pd.DataFrame(data = cum_data, index = index);
cumbar.plot.bar(rot = 15, title = 'Barplot for France, Italy, and US');

#only bar chart that has confirmed for us france and italy
cum_data = {'Confirmed' : [cum_franceconfirmedmax, cum_italyconfirmedmax, cum_usconfirmedmax]}
cumconfirm = pd.DataFrame(data = cum_data, index = index)
cumconfirm.plot.bar(rot = 15, title = 'Barplot for France, Italy, and US (confirmed only)');
plt.close()
plt.clf()
"""
What might we tell our epidiemologist friend?
That the US is the epicenter of the world!
The rate of growth in the US is obscene when compared to these other countries.
Look into why this may have happened in the us... and what we can do to prevent such things.

"""

#three plots, one for confirmed , deaths, and recovered each
#regression lines
#colors, appropriately labeled
#thailandc singaporec
indexes = list(range(0, 104))
thailandc = thailandc.T
singaporec = singaporec.T
temp = pd.concat([thailandc, singaporec], axis = 1)
temp = temp.iloc[3:,:]
temp.columns = ['Thailand', 'Singapore']
temp = temp.reset_index()
temp = temp.reset_index()
temp.drop(columns = ['index'])
thailandarr = []
for i in temp['Thailand']:
    thailandarr.append(i)
singaporearr = []
for i in temp['Singapore']:
    singaporearr.append(i)
coef = np.polyfit(indexes, thailandarr, 1)
poly1d_fn = np.poly1d(coef)
#sns.regplot(x = 'level_0', y = 'Singapore', data = temp, fit_reg = True, ax = ax2)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(indexes, thailandarr, indexes, poly1d_fn(indexes), '--k', label = 'Thailand')
coef = np.polyfit(indexes, singaporearr, 1)
poly1d_fn = np.poly1d(coef)
ax1.plot(indexes, singaporearr, indexes, poly1d_fn(indexes), '-k', label = 'Singapore')
plt.title('Confirmed Cases Thailand Singapore')
plt.ylabel('Cases')
plt.xlabel('Day Number')
plt.legend(loc = 'upper left')
plt.show()
plt.close()
plt.clf()

#thailand recovered
thailandr = thailand_recovered.T
singaporer = singapore_recovered.T
temp = pd.concat([thailandr, singaporer], axis = 1)
temp = temp.iloc[3:,:]
temp.columns = ['Thailand', 'Singapore']
temp = temp.reset_index()
temp = temp.reset_index()
temp.drop(columns = ['index'])
thailandarr = []
for i in temp['Thailand']:
    thailandarr.append(i)
singaporearr = []
for i in temp['Singapore']:
    singaporearr.append(i)
coef = np.polyfit(indexes, thailandarr, 1)
poly1d_fn = np.poly1d(coef)
#sns.regplot(x = 'level_0', y = 'Singapore', data = temp, fit_reg = True, ax = ax2)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(indexes, thailandarr, indexes, poly1d_fn(indexes), '--k', label = 'Thailand')
coef = np.polyfit(indexes, singaporearr, 1)
poly1d_fn = np.poly1d(coef)
ax1.plot(indexes, singaporearr, indexes, poly1d_fn(indexes), '-k', label = 'Singapore')
plt.title('Recovered Thailand Singapore')
plt.ylabel('Cases')
plt.xlabel('Day Number')
plt.legend(loc = 'upper left')
plt.show()
plt.close()
plt.clf()

#thailand recovered
thailandd= thailand_deaths.T
singapored = singapore_deaths.T
temp = pd.concat([thailandd, singapored], axis = 1)
temp = temp.iloc[3:,:]
temp.columns = ['Thailand', 'Singapore']
temp = temp.reset_index()
temp = temp.reset_index()
temp.drop(columns = ['index'])
thailandarr = []
for i in temp['Thailand']:
    thailandarr.append(i)
singaporearr = []
for i in temp['Singapore']:
    singaporearr.append(i)
coef = np.polyfit(indexes, thailandarr, 1)
poly1d_fn = np.poly1d(coef)
#sns.regplot(x = 'level_0', y = 'Singapore', data = temp, fit_reg = True, ax = ax2)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(indexes, thailandarr, indexes, poly1d_fn(indexes), '--k', label = 'Thailand')
coef = np.polyfit(indexes, singaporearr, 1)
poly1d_fn = np.poly1d(coef)
ax1.plot(indexes, singaporearr, indexes, poly1d_fn(indexes), '-k', label = 'Singapore')
plt.title('Deaths Thailand Singapore')
plt.ylabel('Cases')
plt.xlabel('Day Number')
handles, labels = ax1.get_legend_handles_labels()
plt.legend(loc = 'upper left')
plt.show()
plt.close()
plt.clf()

#REMEMBER TO TURN IN OUTPUT AS WELL