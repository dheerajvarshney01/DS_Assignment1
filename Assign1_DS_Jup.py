
# coding: utf-8

# ## 1. Introduction
# For assignment1 we have been given a dataset which contains the information of all the restaurants in Bangalore which is
# IT capital of India. It has more than 12000 restaurants. The reason for such a huge number of restaurants and rapid 
# increase in the number of these restaurants is because people do not have time to cook food and mostly they 
# refer to eat outside.
# The data is taken from zomato and have different attributes. Below are the attributes in the dataset:-
# 1) url - It is the url of the restaurant which when user provides will be navigated 
# 2) address - This attribute basically provides the address of the restaurant where they are located in Bengaluru.
# 3) name - This attribute specifies the name of the restaurant.
# 4) online_order - This attribute provides information that whether online order can be placed or not.
# 5) book_table - This attribute provides information that whether the restaurant has booking table facility or not.
# 6) rate - This attribute tells the overall rating of the restaurant. The rating is given on a scale of 5.
# 7) votes - It provides the votes or number of people who have voted for the restaurant till March 15, 2019.
# 8) phone - This attribute provides the contact number of the restaurant.
# 9) location - This attribute provides the locality where the restaurant is located.
# 10) rest_type - This attribute provides the information that which type of restaurant is it. Different categories could be Buffet, Cafes, Delivery, Desserts, Dineout, Drinks and Nightlife, Pubs and Bars.
# 11) dish_liked - This attribute provides the dish people liked most in the restaurant.
# 12) cuisines - This attribute provides information about which kind of cuisine or food style it is and values for this attribute are separated by comma
# 13) approx_cost(for two people)- This attribute provides the approximate cost of two people in the restaurant.
# 14) reviews_list - This attribute provides information on rating and review by the customer.
# 15) menu_item - It provides list of the menus for a specific restaurant.
# 16) listed_in(type) - It provides what kind of meal it is for that restaurant for eg. Delivery, Cafe etc.
# 17) listed_in(city) - This attribute provides the neighbourhood in which the restaurant is listed. 
# 

# ## 2.Data pre-processing and understanding
# ### a. Load the data.
# We uploaded the csv file and saved it in Data folder in Jupyter notebook and then loaded the data by calling the file with read_csv() 

# In[1]:


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


# ## b. Explore the data. Plot the distribution of the attributes (frequency). What trends can you find in your data? Are there attributes that are useless at this point?
# 
# We plotted frequency plots for 'rate', 'online_order', 'Book_table','location','votes', 'approx_cost for two people', 'listed_in(type)', 'menu_item','cuisines','reviews_list' and 'rest_type'. We found that the dataset contain duplicates values for all the columns. Hence, we decided to remove those duplicates.
# 
# We also observed that there are some attributes which are not informative and are useless like url, address, phone, and dish_liked.
# 
# ## c. Are there restaurant duplicates in the data? Detect and if there is, clean it.

# In[2]:


df = originalDf.copy(deep = True)
df1 = df.duplicated(subset=['address','name'], keep='first')
df1


# ### FrequencyPlot  for the 'rate' column:
# With frequency plot of rate column we observed that 3.9 rating is most predominant given rating for most of the restaurants.

# In[4]:


#def plotDataForExploration(_df):

df = originalDf.copy(deep = True)

df['rate'] = df['rate'].apply(replaceNaNAndNewAndRemoveWhiteSpaces)

## idea for removing rows is taken from here:
## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
## the line below drops records that contain the value of '-' in the rate column:
df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

rates = df['rate']

## idea for plot formating is taken from here
## https://stackoverflow.com/questions/23246125/how-to-center-labels-in-histogram-plot
labels, counts = np.unique(rates, return_counts=True)
import matplotlib.pyplot as plt
plt.bar(labels, counts, align='center')
plt.rcParams['figure.figsize'] = [17, 7]
plt.gca().set_xticks(labels)
plt.title('rate frequencies', fontsize = 18)
plt.xlabel('rate', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### Frequency plot for the 'online_order' column: 
# With online_order frequency plot we observed that ~21000 people do not order line while ~30000 people order food online. We believe reason for it that since most of the people work in IT industry and do not have even time to go to some restaurant and hence they order food online. 

# In[6]:


df = originalDf.copy(deep = True)
online_order = df['online_order']
labels, counts = np.unique(online_order, return_counts=True)
plt.bar(labels, counts, align='center')
plt.rcParams['figure.figsize'] = [4, 7]
plt.gca().set_xticks(labels)
plt.title('online_order frequencies', fontsize = 18)
plt.xlabel('online_order', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### Frequency plot for the 'book_table' column: ##########################
# With frequency plot for book_table we observed that only ~8000 people book table before going to the restaurant while almost ~45000 people do not book table before going to teh restaurant. 

# In[ ]:


df = originalDf.copy(deep = True)
book_table = df['book_table']
import matplotlib.pyplot as plt
labels, counts = np.unique(book_table, return_counts=True)
plt.bar(labels, counts, align='center')
plt.rcParams['figure.figsize'] = [4, 7]
plt.gca().set_xticks(labels)
plt.title('book_table frequencies', fontsize = 18)
plt.xlabel('book_table', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### Frequency plot for the 'location' column: 
# With frequency plot for location we found that in 'BTM' there are majority of the restaurants which is one of the famous places of Bangalore.

# In[ ]:


df = originalDf.copy(deep = True)
location = df['location']
df['location'] = df['location'].apply(replaceNaNByString)
labels, counts = np.unique(location, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
#plt.rcParams['figure.figsize'] = [18, 7]
## idea how to rotate x-axes labels:
## https://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib
plt.xticks(rotation=90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.title('location frequencies', fontsize = 18)
plt.xlabel('location', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ###  Frequency plot  for the 'votes' column:
# Frequency plot for votes tells that there were around ~10000 people who did not vote for any restaurant and not many people  like to vote for a particular restaurant

# In[ ]:


## CLEAN ANA FROM THE PLOT !!!
df = originalDf.copy(deep = True)
votes = df['votes']
## idea how to plot histogram:
## https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data
plt.hist(list(votes), bins=5000)
plt.rcParams['figure.figsize'] = [17, 7]
plt.axis([-10, 250, 0, 12000])
plt.title('votes frequencies', fontsize = 18)
plt.xlabel('number of votes', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### Frequency plot for the 'listed_in(type)' column:
# Frequency plot for listed_in(type) provides information that Delivery type of meal is most common among all other types of meal. 

# In[ ]:


############### Plot frequency for the ')' column: ##########################
df = originalDf.copy(deep = True)
listed_in = df['listed_in(type)']
labels, counts = np.unique(listed_in, return_counts=True)
plt.bar(labels, counts, align='center')
plt.rcParams['figure.figsize'] = [17, 7]
plt.gca().set_xticks(labels)
plt.title('listed_in(type) frequencies', fontsize = 18)
plt.xlabel('listed_in(type)', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### Frequency plot for the 'approx_cost(for two people)' column:
# Frequency plot for 'approx_cost(for two people)' tells that the range of cost for a meal lies between range of Rs.100 to Rs.1000 for two people with ~Rs.300 with the highest frequency.

# In[ ]:


df = originalDf.copy(deep = True)
##df.drop_duplicates(subset =['name','address'], keep = 'first', inplace = True)

df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(removeCommas)
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(replaceNaNsByNegativeValue)

## idea how to plot histogram:
## https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data

# plt.hist(list(df['approx_cost(for two people)']), bins='auto')
# plt.axis([-120, 4500, 0, 2000])
# plt.rcParams['figure.figsize'] = [17, 7]
# plt.xticks(rotation=90)
# plt.title('approx_cost(for two people) frequency - histogram', fontsize = 18)
# plt.xlabel('approx_cost', fontsize = 12)
# plt.ylabel('frequency', fontsize = 12)
# plt.show()

labels = []
counts = []
for i in range(0, 100, 1):
    labels.append(i*10)
    counts.append(0)

for price in list(df['approx_cost(for two people)']):
    index = int(price/10 - price%10)
    if index < 100:
        counts[index] += 1

    
# plt.bar(labels, counts, align='center', width = 5)
# plt.rcParams['figure.figsize'] = [17, 7]
# plt.gca().set_xticks(labels)
# plt.xticks(fontsize=6, rotation=90)
# plt.yscale('log')
# plt.title('approx_cost(for two people) frequency - bar chart with logarithmic Y scale', fontsize = 18)
# plt.xlabel('approx_cost', fontsize = 12)
# plt.ylabel('frequency', fontsize = 12)
# plt.show()

##labels, counts = np.unique(list(df['approx_cost(for two people)']), return_counts=True)
    
plt.bar(labels, counts, align='center', width = 5)
plt.rcParams['figure.figsize'] = [17, 7]
plt.gca().set_xticks(labels)
plt.xticks(fontsize=8, rotation=90)
plt.title('approx_cost(for two people) frequency - bar chart with linear scale', fontsize = 18)
plt.xlabel('approx_cost', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### Frequency plot for the 'reviews_list' column: 
# Frequency plot for 'reviews_list' provides information on the reviews and the rating given by the customer. According to the plot ~8000 people give 2 reviews and with the kind of trend we observe that not many people are interested to give reviews about any restaurant. We believe the reason for it is that the time crunch. As people do not have enough time, they do not provide reviews.

# In[ ]:


df = originalDf.copy(deep = True)
reviewsCounts = []
reviews = list(df['reviews_list'])
for review in reviews:
    reviewsCounts.append(len(review.split(")")))

## frequency diagram for number of reviews in the range [0:50]
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


# ### Frequency plot for the 'menu_item' column: 
# NOTE:we don't plot number of restaurants that have zero items in menu because those are about 35000 and this number makes others invisible on the plot.
# 
# 

# In[ ]:


df = originalDf.copy(deep = True)
menuItemCounts = []
menu_items = list(df['menu_item'])
for menu_item in menu_items:
    num_of_items = len(menu_item.split("',"))
    if num_of_items > 1 and num_of_items < 450:
            menuItemCounts.append(num_of_items)
plt.hist(menuItemCounts, bins=450)
plt.rcParams['figure.figsize'] = [17, 7]
plt.show()


# ### Frequency plot for the 'cuisines' column: 
# Frequency plot for 'cuisines' tells that the NorthIndian cuisines are most liked by people of about ~22000. Chinese is the other type pf cuisine which people liked most after NorthIndian.

# In[ ]:


df = originalDf.copy(deep = True)
cuisinesList = []
df['cuisines'] = df['cuisines'].apply(replaceNaNByString)
df['cuisines'] = df['cuisines'].apply(splitToList)

for cuisines in list(df['cuisines']):
        cuisinesList += cuisines

## frequency diagram for number of cuisines in the range [0:50]
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


# ###   Frequency plot for the 'rest_type' column:
# Frequency plot for 'rest_type' provides information about the type pf restaurant people like most. Quick Bites is
#  the predominant among all other types of restaurants.

# In[ ]:


df = originalDf.copy(deep = True)
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
plt.title('rest_type frequencies (rest_type split by comma and evaluated separately)', fontsize = 18)
plt.xlabel('rest_type', fontsize = 12)
plt.ylabel('frequency', fontsize = 12)
plt.show()


# ### 2.d - 
# The neighborhood with the highest average rating is **Lavelle Road** . We found it by grouping all the location and then finding the mean of the rate 
# 
# Dropping 'NEW' and NaN from the 'rate' column: 
# We are dropping 'NEW' because it means that there is no rating assigned to the restaurant.
# We are dropping NaN because:
# 1. Replacing with the value of the neighbourhood's average won't change the neighbourhood's average
# 2. Replacing with the value of the dataset's average will unreasonably change the average of neighbourhood

# In[ ]:


############### Drop duplicates: ##########################
df = originalDf.copy(deep = True)
##df.drop_duplicates(subset =['name','address'], keep = 'first', inplace = True)

df.dropna(subset = ['rate'], inplace = True)

df['rate'] = df['rate'].apply(removeWhiteSpaces)

## idea for removing rows is taken from here:
## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
## the line below drops records that contain the value of '-' or '' in the rate column:
df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

df['rate'] = df['rate'].apply(convertRatingsToFloat)

## idea of grouping by column name and calculation of the mean value of other column per group is taken from here:
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


# ### The major characteristics of this neighborhood (e.g., type of restaurant, type of food they offer, etc).
# 1. Online Order
# ~200 people residing in this area order their food online while ~300 people do not order online.
# 
# 2. Book Table
# ~230 people who live in Lavelle Road book table before going to the restaurant while ~260 people do not book table before their visit.
# 
# 3. Rest Type
# The restaurant type which is more poular in this neighborhood is Casual Dining. The second most famous kind of restaurant is Bar. 
# 
# 4. Cuisines
# People residing in this area like Italian, Continental and NorthIndian. Italian cuisine is liked by ~150 people who stay here.

# In[ ]:


mostRatedRestaurants = df[df.location=='Lavelle Road']
online_order = mostRatedRestaurants['online_order']
labels, counts = np.unique(online_order, return_counts=True)
    
plt.bar(labels, counts, align='center')
plt.rcParams['figure.figsize'] = [4, 7]
plt.gca().set_xticks(labels)
plt.title('online_order frequencies for the neighbourhood with highest rate', fontsize = 18)
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

## frequency diagram for number of cuisines in the range [0:50]

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


# plotDataForExploration(originalDf)
# print(500*'*')
# df_copy_no_duplicates = originalDf.drop_duplicates(subset =['name','address'], keep = 'first')
# plotDataForExploration(df_copy_no_duplicates)


# #### 3a.
# The task that we are solving is a supervised regression. It is supervised because our training set contains both input and output (target) values, and it is regression because target value is numeric.
# 
# #### 3b. 
# We will use the sklearn.ensemble. RandomForestRegressor. We choose this classifier for several reasons:                      i.	It solves regression tasks.                                                                                             ii. It uses the advantages of ensembles.                                                                                   iii. It does not use the “distance” measure between the data points, which is good for our case where input features are categorical (even though we have concerted the ‘rate’ to be numerical, ‘3.7/5’ -> 3.7, still other )
# 
# #### 3c.
# As the algorithm that we are using is a regression, the metric we will use for the model evaluation will be the root mean square error.
# 
# #### 3d. 
# To make sure we are not overfitting, we will plot the root mean square error of the model on training and testing sets versus the depth of the trees in ensemble.
# 
# #### 3e. 
# We have noticed that most of the costs of meal for two people are below Rs. 2250. Hence we decided to drop records where the cost of the meal is higher than Rs. 2250. Our observation showed that dropping those records improves the accuracy (RMSE is lower). We are using the Cross-Validation approach to evaluate the algorithm we choose. Cross-Validation allows us to use all of the data for the evaluation purpose, and collect some statistical data (in our case it is a root mean square errors) on the performance of different models that are generated on each of the folds of the data set. We have calculated RMSE for each model in the Cross-Validation folds (we divide our data set into ten folds). Here is the plot of RMSEs:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# We can see that RMSE values are located within a narrow range of 120 – 140, and this means that these models behave consistently.Regarding the quality of the model: the RMSEs that we have calculated are  the errors that will happen when trying to predict the cost of the meal for two people. Given that we have limited our modeling to the cost range of Rs. 0 to Rs. 2250, most of the costs fall in the range of Rs. 100 to Rs. 1100, and the average RMSE is ~130, our model is good for predicting costs in upper range 
# 

# In[ ]:


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

encoded_df = pd.DataFrame(df['approx_cost(for two people)'].reset_index()['approx_cost(for two people)'])            .join(pd.DataFrame(rate_mlb, columns = rate_mlb_column_names))             .join(pd.DataFrame(location_mlb, columns = location_mlb_column_names))             .join(pd.DataFrame(rest_type_mlb, columns = rest_type_mlb_column_names))             .join(pd.DataFrame(cuisines_mlb, columns = cuisines_mlb_column_names))
encoded_df


# for val in list(train['approx_cost(for two people)']):
#     if type(val) is not float and isnan(val) == True:
#         prubt("asd")
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

