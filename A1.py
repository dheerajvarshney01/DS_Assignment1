import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from math import isnan
originalDf = pd.read_csv(r'D:\Studies\DalhousieUniversity\Summer2019\DataScience\A1\zomato.csv')

def replaceNaNAndNewAndRemoveWhiteSpaces(val):
    if type(val) is not str and isnan(val) == True:
        val = '7.0/5'
    if type(val) is str:
        if val.lower() == 'new':
            val = '6.0/5'
        return pattern.sub("", val)
    return val

def replaceNaNByString(val):
    if type(val) is not str and isnan(val) == True:
        val = 'NaN'
    return val

def removeCommas(val):
    if type(val) is str:
        # make values like 8,200 be 8200
        val = val.replace(',', '')
    elif isnan(float(val)):
        val = '-100'
    return float(val)

def replaceNaNsByNegativeValue(val):
    if isnan(float(val)):
        val = '-100'
    return float(val)

def splitToList(stringValue):
    splittedTypes = []
    for value in stringValue.split(","):
        value = value.replace(" ", "")
        splittedTypes.append(value)
    return splittedTypes

def convertRatingsToFloat(val):
    return float(val[:-2])

def removeWhiteSpaces(val):
    return pattern.sub("", val)

## '7.0/5' value is used to replace 'nan' values,
## '6.0/5' value is used to replace 'NEW' values:
rating_values = [ '0.0/5','0.0/5','0.1/5', '0.2/5', '0.3/5', '0.4/5', '0.5/5', '0.6/5', '0.7/5', '0.8/5', '0.9/5', '1.0/5',
                  '1.1/5', '1.2/5', '1.3/5', '1.4/5', '1.5/5', '1.6/5', '1.7/5', '1.8/5', '1.9/5', '2.0/5',
                  '2.1/5', '2.2/5', '2.3/5', '2.4/5', '2.5/5', '2.6/5', '2.7/5', '2.8/5', '2.9/5', '3.0/5',
                  '3.1/5', '3.2/5', '3.3/5', '3.4/5', '3.5/5', '3.6/5', '3.7/5', '3.8/5', '3.9/5', '4.0/5',
                  '4.1/5', '4.2/5', '4.3/5', '4.4/5', '4.5/5', '4.6/5', '4.7/5', '4.8/5', '4.9/5', '5.0/5',
                  '6.0/5', '7.0/5'
                  ]

pattern = re.compile(r'[^0123456789./-]')


def plotDataForExploration(_df):
    ############### Plot frequency for the 'rate' column: ##########################
    df = _df.copy(deep = True)

    df['rate'] = df['rate'].apply(replaceNaNAndNewAndRemoveWhiteSpaces)

    ## idea for removing rows is taken from here:
    ## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
    ## the line below drops records that contain the value of '-' in the rate column:
    df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

    rates = df['rate']

    ## idea for plot formating is taken from here
    ## https://stackoverflow.com/questions/23246125/how-to-center-labels-in-histogram-plot
    labels, counts = np.unique(rates, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.title('rate frequences', fontsize = 18)
    plt.xlabel('rate', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### Plot frequency for the 'online_order' column: ##########################
    df = _df.copy(deep = True)
    online_order = df['online_order']

    labels, counts = np.unique(online_order, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [4, 7]
    plt.gca().set_xticks(labels)
    plt.title('online_order frequences', fontsize = 18)
    plt.xlabel('online_order', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### Plot frequency for the 'book_table' column: ##########################
    df = _df.copy(deep = True)
    book_table = df['book_table']

    labels, counts = np.unique(book_table, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [4, 7]
    plt.gca().set_xticks(labels)
    plt.title('book_table frequences', fontsize = 18)
    plt.xlabel('book_table', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### Plot frequency for the 'location' column: ##########################
    df = _df.copy(deep = True)
    location = df['location']

    df['location'] = df['location'].apply(replaceNaNByString)

    labels, counts = np.unique(location, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    ## idea how to rotate x-axes labels:
    ## https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.title('location frequences', fontsize = 18)
    plt.xlabel('location', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()

    ## CLEAN ANA FROM THE PLOT !!!

    ############### Plot frequency for the 'votes' column: ##########################
    df = _df.copy(deep = True)
    votes = df['votes']

    ## idea how to plot histogram:
    ## https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data
    plt.hist(list(votes), bins=5000)
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.axis([-10, 250, 0, 12000])
    plt.title('votes frequences', fontsize = 18)
    plt.xlabel('number of votes', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)

    plt.show()



    ############### Plot frequency for the 'approx_cost(for two people)' column: ##########################
    df = _df.copy(deep = True)
    ##df.drop_duplicates(subset =['name','address'], keep = 'first', inplace = True)

    df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(removeCommas)
    df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(replaceNaNsByNegativeValue)

    ## idea how to plot histogram:
    ## https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data
    plt.hist(list(df['approx_cost(for two people)']), bins='auto')
    plt.axis([-120, 4500, 0, 2000])
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.xticks(rotation=90)
    plt.title('approx_cost(for two people) frequency - histogram', fontsize = 18)
    plt.xlabel('approx_cost', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()

    labels = []
    counts = []
    for i in range(0, 100, 1):
        labels.append(i*10)
        counts.append(0)

    for price in list(df['approx_cost(for two people)']):
        index = int(price/10 - price%10)
        if index < 100:
            counts[index] += 1


    plt.bar(labels, counts, align='center', width = 5)
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(fontsize=6, rotation=90)
    plt.yscale('log')
    plt.title('approx_cost(for two people) frequency - bar chart with logarithmic Y scale', fontsize = 18)
    plt.xlabel('approx_cost', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()

    ##labels, counts = np.unique(list(df['approx_cost(for two people)']), return_counts=True)
    plt.bar(labels, counts, align='center', width = 5)
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(fontsize=6, rotation=90)
    plt.title('approx_cost(for two people) frequency - bar chart with linear scale', fontsize = 18)
    plt.xlabel('approx_cost', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()




    ############### Plot frequency for the 'listed_in(type)' column: ##########################
    df = _df.copy(deep = True)

    listed_in = df['listed_in(type)']
    labels, counts = np.unique(listed_in, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.title('listed_in(type) frequencies', fontsize = 18)
    plt.xlabel('listed_in(type)', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### Plot frequency for the 'reviews_list' column: ##########################
    df = _df.copy(deep = True)

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
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.title('reviews_list frequencies', fontsize = 18)
    plt.xlabel('number of reviews', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### Plot frequency for the 'menu_item' column: ##########################
    ## we don't plot number of restaurants that have zero items in menu because those are
    ## about 35000 and this number makes others invisible on the plot.
    df = _df.copy(deep = True)

    menuItemCounts = []

    menu_items = list(df['menu_item'])
    for menu_item in menu_items:
        num_of_items = len(menu_item.split("',"))
        if num_of_items > 1 and num_of_items < 450:
            menuItemCounts.append(num_of_items)

    plt.hist(menuItemCounts, bins=450)
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.show()



    ############### Plot frequency for the 'cuisines' column: ##########################
    df = _df.copy(deep = True)

    cuisinesList = []

    df['cuisines'] = df['cuisines'].apply(replaceNaNByString)
    df['cuisines'] = df['cuisines'].apply(splitToList)

    for cuisines in list(df['cuisines']):
        cuisinesList += cuisines

    ## frewquency diagram for number of cuisines in the range [0:50]
    labels, counts = np.unique(cuisinesList, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.title('cuisines frequencies', fontsize = 18)
    plt.xlabel('cuisine', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### Plot frequency for the 'rest_type' column: ##########################
    df = _df.copy(deep = True)
    rest_type = df['rest_type']

    df['rest_type'] = df['rest_type'].apply(replaceNaNByString)

    fixedrestaurants = []

    rest_type = list(df['rest_type'])

    for typeValue in rest_type:
        for value in typeValue.split(","):
            value = value.replace(" ", "")
            fixedrestaurants.append(value)

    df['rest_type'] = df['rest_type'].apply(splitToList)

    ## if not splitting the string by comma:
    labels, counts = np.unique(rest_type, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.title('rest_type frequencies', fontsize = 18)
    plt.xlabel('rest_type', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()

    ## if splitting the string by comma:
    labels, counts = np.unique(fixedrestaurants, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.title('rest_type frequencies (rest_typy split by comma and evaluated separately)', fontsize = 18)
    plt.xlabel('rest_type', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()



    ############### 2.d - What is the neighborhood with the highest average rating? ##########################
    ############### Drop duplicates: ##########################
    df = originalDf.copy(deep = True)
    ##df.drop_duplicates(subset =['name','address'], keep = 'first', inplace = True)


    ############### Drop 'NEW' and NaN from the 'rate': ##########################
    ## We are dropping 'NEW' because it means that there is no rating assigned to the restaurant.
    ## We are dropping NaN because:
    ## 1. Replacing with the value of the neighbourhood's average won't change the neighbourhood's average
    ## 2. Replacing with the value of the dataset's average will unreasonably change the average of neighbourhood

    df.dropna(subset = ['rate'], inplace = True)

    df['rate'] = df['rate'].apply(removeWhiteSpaces)

    ## idea for removing rows is taken from here:
    ## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
    ## the line below drops records that contain the value of '-' or '' in the rate column:
    df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

    df['rate'] = df['rate'].apply(convertRatingsToFloat)

    ## idea of grupping by column name and calculation of the mean value of other column per group is taken from here:
    ## https://stackoverflow.com/questions/30482071/how-to-calculate-mean-values-grouped-on-another-column-in-pandas
    rateAverageByLocation = df.groupby('location', as_index=False)['rate'].mean()
    rateAverageByLocation.iloc[rateAverageByLocation['rate'].idxmax()]

    labels = list(rateAverageByLocation['location'])
    counts = list(rateAverageByLocation['rate'])
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.gca().set_xticks(labels)
    plt.title('Rating by Neighbourhood', fontsize = 18)
    plt.xlabel('Neighbourhood', fontsize = 12)
    plt.ylabel('Rating', fontsize = 12)
    plt.show()

    ## What are the major characteristics of this neighborhood (e.g., type of restaurant, type of food they offer, etc).

    mostRatedRestaurants = df[df.location=='Lavelle Road']


    online_order = mostRatedRestaurants['online_order']
    labels, counts = np.unique(online_order, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [4, 7]
    plt.gca().set_xticks(labels)
    plt.title('online_order frequencies for the neighbourhood with highest rate)', fontsize = 18)
    plt.xlabel('online_order', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()


    book_table = mostRatedRestaurants['book_table']
    labels, counts = np.unique(book_table, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [4, 7]
    plt.gca().set_xticks(labels)
    plt.title('book_table frequencies for the neighbourhood with highest rate)', fontsize = 18)
    plt.xlabel('online_order', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
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
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.title('rest_type (splitted by comma) frequencies for the neighbourhood with highest rate)', fontsize = 18)
    plt.xlabel('rest_type', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()


    fixedCuisines = []

    cuisines = list(mostRatedRestaurants['cuisines'])

    for cuisine in cuisines:
        if type(cuisine) is not str and isnan(cuisine) == True:
            cuisine = 'NaN'
        for value in cuisine.split(","):
            value = value.replace(" ", "")
            fixedCuisines.append(value)

    ## frewquency diagram for number of cuisines in the range [0:50]

    labels, counts = np.unique(fixedCuisines, return_counts=True)
    plt.bar(labels, counts, align='center')
    plt.rcParams['figure.figsize'] = [17, 7]
    plt.gca().set_xticks(labels)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(bottom=0.27)
    plt.title('cuisines (splitted by comma) frequencies for the neighbourhood with highest rate)', fontsize = 18)
    plt.xlabel('cuisine', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()


plotDataForExploration(originalDf)
print(500*'*')
df_copy_no_duplicates = originalDf.drop_duplicates(subset =['name','address'], keep = 'first')
plotDataForExploration(df_copy_no_duplicates)



############### 3 - preparing the dataset ##########################
# load data:
df = originalDf.copy(deep = True)
# remove duplicates:
df.drop_duplicates(subset =['name','address'], keep = 'first', inplace = True)
# select columns to be used in model training:
df = df[['location', 'rate', 'rest_type', 'cuisines', 'approx_cost(for two people)']]
df['location'] = df['location'].apply(replaceNaNByString)

# 'rate' column contains the following bad data: empty cells '', NaN, and
# whitespaces inside the rate value (for example, '3.2 /2').

df['rate'] = df['rate'].apply(replaceNaNByString)
df['rate'] = df['rate'].apply(removeWhiteSpaces)

## the line below drops records that contain the value of '-' or '' in the rate column:
extended_rating_values = rating_values + ['NEW', 'NaN', '']
df.drop(df[~df['rate'].isin(extended_rating_values)].index, inplace = True)

df['rest_type'] = df['rest_type'].apply(replaceNaNByString)

def splitToList(stringValue):
    splittedTypes = []
    for value in stringValue.split(","):
        value = value.replace(" ", "")
        splittedTypes.append(value)
    return splittedTypes

df['rest_type'] = df['rest_type'].apply(splitToList)

df['cuisines'] = df['cuisines'].apply(replaceNaNByString)
df['cuisines'] = df['cuisines'].apply(splitToList)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(removeCommas)
# TARGET value of -100.0 appears in cells where NaN appeared in original data. We remove
# those records from the dataframe because we cannot use it not for training, nor for testing
df.drop(df[df['approx_cost(for two people)'] == -100.0].index, inplace = True)


## Apply "one hot encoding":
## https://stackoverflow.com/questions/42711861/scikit-learn-one-hot-encoding-of-column-with-list-values
from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()

rest_type_mlb = mlb.fit_transform(df['rest_type'])
## List comprehension
## https://stackoverflow.com/questions/2050637/appending-the-same-string-to-a-list-of-strings-in-python
rest_type_mlb_column_names = [rest_type + '_rest_type' for rest_type in mlb.classes_]

cuisines_mlb = mlb.fit_transform(df['cuisines'])
cuisines_mlb_column_names = [cuisine + '_cuisine' for cuisine in mlb.classes_]

location_mlb = mlb.fit_transform(df['location'])
location_mlb_column_names = [location + '_location' for location in mlb.classes_]

rate_mlb = mlb.fit_transform(df['rate'])
rate_mlb_column_names = [rate + '_rate' for rate in mlb.classes_]

encoded_df = pd.DataFrame(df['approx_cost(for two people)'].reset_index()['approx_cost(for two people)'])\
            .join(pd.DataFrame(rate_mlb, columns = rate_mlb_column_names)) \
            .join(pd.DataFrame(location_mlb, columns = location_mlb_column_names)) \
            .join(pd.DataFrame(rest_type_mlb, columns = rest_type_mlb_column_names)) \
            .join(pd.DataFrame(cuisines_mlb, columns = cuisines_mlb_column_names))


for val in list(train['approx_cost(for two people)']):
    if type(val) is not float and isnan(val) == True:
        prubt("asd")
# Split data into training and testing sets:
from sklearn.model_selection import train_test_split
train, test = train_test_split(encoded_df, test_size=0.2)
train_x = train.drop('approx_cost(for two people)', axis=1)
train_y = train['approx_cost(for two people)']

test_x = test.drop('approx_cost(for two people)', axis=1)
test_y = test['approx_cost(for two people)']

# from here - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
randomForestRegression = RandomForestRegressor(max_depth=10, random_state=0, n_estimators=100)

randomForestRegression.fit(train_x, train_y)

