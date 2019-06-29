import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
originalDf = pd.read_csv(r'D:\Studies\DalhousieUniversity\Summer2019\DataScience\A1\zomato.csv')

############### Plot frequency for the 'rate' column: ##########################

## '7.0/5' value is used to replace 'nan' values,
## '6.0/5' value is used to replace 'NEW' values:
rating_values = [ '0/5','0.0/5','0.1/5', '0.2/5', '0.3/5', '0.4/5', '0.5/5', '0.6/5', '0.7/5', '0.8/5', '0.9/5', '1.0/5',
                  '1.1/5', '1.2/5', '1.3/5', '1.4/5', '1.5/5', '1.6/5', '1.7/5', '1.8/5', '1.9/5', '2.0/5',
                  '2.1/5', '2.2/5', '2.3/5', '2.4/5', '2.5/5', '2.6/5', '2.7/5', '2.8/5', '2.9/5', '3.0/5',
                  '3.1/5', '3.2/5', '3.3/5', '3.4/5', '3.5/5', '3.6/5', '3.7/5', '3.8/5', '3.9/5', '4.0/5',
                  '4.1/5', '4.2/5', '4.3/5', '4.4/5', '4.5/5', '4.6/5', '4.7/5', '4.8/5', '4.9/5', '5.0/5',
                  '6.0/5', '7.0/5'
                  ]

import re
pattern = re.compile(r'[^0123456789./-]')

df = originalDf.copy(deep = True)

from math import isnan

def replaceNaNAndNewAndRemoveWhiteSpaces(val):
    if type(val) is not str and isnan(val) == True:
        val = '7.0/5'
    if type(val) is str:
        if val.lower() == 'new':
            val = '6.0/5'
        return pattern.sub("", val)
    return val

df['rate'] = df['rate'].apply(replaceNaNAndNewAndRemoveWhiteSpaces)

## idea for removing rows is taken from here:
## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
## the line below drops records that contain the value of '-' in the rate column:
df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

rates = df['rate']
floatRates = []
for rate in rates:
    floatRates.append(float(rate[:-2]))
## idea for plot formating is taken from here
## https://stackoverflow.com/questions/23246125/how-to-center-labels-in-histogram-plot
labels, counts = np.unique(rates, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()



############### Plot frequency for the 'online_order' column: ##########################
df = originalDf.copy(deep = True)
online_order = df['online_order']

labels, counts = np.unique(online_order, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()



############### Plot frequency for the 'book_table' column: ##########################
df = originalDf.copy(deep = True)
book_table = df['book_table']

labels, counts = np.unique(book_table, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()



############### Plot frequency for the 'location' column: ##########################
df = originalDf.copy(deep = True)
location = df['location']

def replaceNaNByString(val):
    if type(val) is not str and isnan(val) == True:
        val = 'NaN'
    return val

df['location'] = df['location'].apply(replaceNaNByString)

labels, counts = np.unique(location, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
## idea how to rotate x-axes labels:
## https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

## CLEAN ANA FROM THE PLOT !!!

############### Plot frequency for the 'votes' column: ##########################
df = originalDf.copy(deep = True)
votes = df['votes']

## idea how to plot histogram:
## https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data
plt.hist(list(votes), bins=5000)
plt.axis([-10, 250, 0, 12000])
plt.xlabel('Number of Restaurants')
plt.ylabel('Number of Votes')
plt.show()



############### Plot frequency for the 'approx_cost(for two people)' column: ##########################
df = originalDf.copy(deep = True)

def removeNaN(val):
    if type(val) is str:
        val = val.replace(',', '')
    elif isnan(float(val)):
        val = '-100'
    return int(val)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(removeNaN)

## idea how to plot histogram:
## https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data
plt.hist(list(df['approx_cost(for two people)']), bins='auto')
plt.axis([-120, 4500, 0, 8000])
plt.xticks(rotation=90)
plt.show()



############### Plot frequency for the 'listed_in(type)' column: ##########################
df = originalDf.copy(deep = True)

listed_in = df['listed_in(type)']
labels, counts = np.unique(listed_in, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()



############### Plot frequency for the 'reviews_list' column: ##########################
df = originalDf.copy(deep = True)

reviewsCounts = []

reviews = list(df['reviews_list'])
for review in reviews:
     reviewsCounts.append(len(review.split(")")))

## frewquency diagram for number of reviews in the range [0:50]

strings = []
for number in reviewsCounts:
    if number <= 50:
        strings.append(number)

labels, counts = np.unique(strings, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()



############### Plot frequency for the 'menu_item' column: ##########################
## we don't plot number of restaurants that have zero items in menu because those are
## about 35000 and this number makes others invisible on the plot.
df = originalDf.copy(deep = True)

menuItemCounts = []

menu_items = list(df['menu_item'])
for menu_item in menu_items:
    num_of_items = len(menu_item.split("',"))
    if num_of_items > 1 and num_of_items < 450:
        menuItemCounts.append(num_of_items)

plt.hist(menuItemCounts, bins=450)
##plt.axis([-10, 250, 0, 12000])
plt.show()



############### Plot frequency for the 'cuisines' column: ##########################

##    here we need to filter cousines manually because it contains bad data
df = originalDf.copy(deep = True)


fixedCuisines = []

cuisines = list(df['cuisines'])

for cuisine in cuisines:
    if type(cuisine) is not str and isnan(cuisine) == True:
        cuisine = 'NaN'
    for value in cuisine.split(","):
        value = value.replace(" ", "")
        fixedCuisines.append(value)

## frewquency diagram for number of cuisines in the range [0:50]

labels, counts = np.unique(fixedCuisines, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()



############### Plot frequency for the 'rest_type' column: ##########################
df = originalDf.copy(deep = True)
rest_type = df['rest_type']

def replaceNaNByString(val):
    if type(val) is not str and isnan(val) == True:
        val = 'NaN'
    return val

df['rest_type'] = df['rest_type'].apply(replaceNaNByString)

fixedrestaurants = []

rest_type = list(df['rest_type'])

for typeValue in rest_type:
    for value in typeValue.split(","):
        value = value.replace(" ", "")
        fixedrestaurants.append(value)

## if not splitting the string by comma:
labels, counts = np.unique(rest_type, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

## if splitting the string by comma:
labels, counts = np.unique(fixedrestaurants, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()



############### Drop duploicates: ##########################
df = originalDf.copy(deep = True)
df.drop_duplicates(subset =['name','address'], keep = 'first', inplace = True)


############### Drop 'NEW' and NaN from the 'rate': ##########################
## We are dropping 'NEW' because it means that there is no rating assigned to the restaurant.
## We are dropping NaN because:
## 1. Replacing with the value of the neighbourhood's average won't change the neighbourhood's average
## 2. Replacing with the value of the dataset's average will unreasonably change the average of neighbourhood

pattern = re.compile(r'[^0123456789./-]')

from math import isnan

def removeWhiteSpace(val):
    return pattern.sub("", val)

df.dropna(subset = ['rate'], inplace = True)

df['rate'] = df['rate'].apply(removeWhiteSpace)

## idea for removing rows is taken from here:
## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
## the line below drops records that contain the value of '-' or '' in the rate column:
df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

def convertRatingsToFloat(val):
    return float(val[:-2])

df['rate'] = df['rate'].apply(convertRatingsToFloat)

## idea of grupping by column name and calculation of the mean value of other column per group is taken from here:
## https://stackoverflow.com/questions/30482071/how-to-calculate-mean-values-grouped-on-another-column-in-pandas
rateAverageByLocation = df.groupby('location', as_index=False)['rate'].mean()
rateAverageByLocation.iloc[rateAverageByLocation['rate'].idxmax()]

labels = list(rateAverageByLocation['location'])
counts = list(rateAverageByLocation['rate'])
plt.bar(labels, counts, align='center')
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.gca().set_xticks(labels)
plt.show()

## What are the major characteristics of this neighborhood (e.g., type of restaurant, type of food they offer, etc).

mostRatedRestaurants = df[df.location=='Lavelle Road']


online_order = mostRatedRestaurants['online_order']
labels, counts = np.unique(online_order, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()


book_table = mostRatedRestaurants['book_table']
labels, counts = np.unique(book_table, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()


rest_type = mostRatedRestaurants['rest_type'].apply(replaceNaNByString)
fixedrestaurants = []
rest_type = list(rest_type)

for typeValue in rest_type:
    for value in typeValue.split(","):
        value = value.replace(" ", "")
        fixedrestaurants.append(value)

## if splitting the string by comma:
labels, counts = np.unique(fixedrestaurants, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()


