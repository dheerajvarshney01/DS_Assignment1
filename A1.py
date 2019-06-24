import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
originalDf = pd.read_csv(r'D:\Studies\DalhousieUniversity\Summer2019\DataScience\A1\zomato.csv')

############### Plot frequency for the 'rate' column: ##########################

## '7.0/5' value is used to replace 'nan' values,
## '6.0/5' value is used to replace 'NEW' values:
rating_values = [ '0.1/5', '0.2/5', '0.3/5', '0.4/5', '0.5/5', '0.6/5', '0.7/5', '0.8/5', '0.9/5', '1.0/5',
                  '1.1/5', '1.2/5', '1.3/5', '1.4/5', '1.5/5', '1.6/5', '1.7/5', '1.8/5', '1.9/5', '2.0/5',
                  '2.1/5', '2.2/5', '2.3/5', '2.4/5', '2.5/5', '2.6/5', '2.7/5', '2.8/5', '2.9/5', '3.0/5',
                  '3.1/5', '3.2/5', '3.3/5', '3.4/5', '3.5/5', '3.6/5', '3.7/5', '3.8/5', '3.9/5', '4.0/5',
                  '4.1/5', '4.2/5', '4.3/5', '4.4/5', '4.5/5', '4.6/5', '4.7/5', '4.8/5', '4.9/5', '5.0/5',
                  '6.0/5', '7.0/5'
                  ]

import re
pattern = re.compile(r'[^0123456789./-]')

df = originalDf.copy(deep = True)
values = {}

from math import isnan

def removeBadCharactersAndNaN(val):
    if type(val) is not str and isnan(val) == True:
        val = '7.0/5'
    if type(val) is str:
        if val.lower() == 'new':
            val = '6.0/5'
        if val not in values.keys():
            values[val] = 1
        else:
            values[val] += 1
        return pattern.sub("", val)
    return val

df['rate'] = df['rate'].apply(removeBadCharactersAndNaN)

## idea for removing rows is taken from here:
## https://thispointer.com/python-pandas-how-to-drop-rows-in-dataframe-by-conditions-on-column-values/
df.drop(df[~df['rate'].isin(rating_values)].index, inplace = True)

rate = df['rate']
## idea for plot formating is taken from here
## https://stackoverflow.com/questions/23246125/how-to-center-labels-in-histogram-plot
labels, counts = np.unique(rate, return_counts=True)
plt.bar(labels, counts, align='center')
plt.gca().set_xticks(labels)
plt.show()

