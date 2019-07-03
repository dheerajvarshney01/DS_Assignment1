import csv

## solves the issue "Error: field larger than field limit (131072)"
## solution from here:
## https://stackoverflow.com/questions/15063936/csv-error-field-larger-than-field-limit-131072
import sys
csv.field_size_limit(1000000000)

columnsToDrop = ['url', 'address', 'phone', 'listed_in(city)']
columnsToKeep = []
columnsToProcess = {}

with open('zomato.csv', mode='r') as inData:
    reader = csv.reader(inData)
    columnNames = reader.__next__()

    for columnIndex, columnName in zip(range(0, len(columnNames)), columnNames):
        if columnName not in columnsToDrop:
            columnsToKeep.append(True)
            columnsToProcess[columnName] = []
        else:
            columnsToKeep.append(False)

    for row in reader:
        for index in range(len(row)):
            if columnsToKeep[index] == True:
                columnsToProcess[columnNames[index]].append(row[index])

    inData.close()


import matplotlib.pyplot as plt

def plotFrequency(columnName, listOfValues):
    plt.hist(listOfValues)
    plt.xlabel(columnName)
    plt.ylabel('count')
    plt.show()

plotFrequency('rest_type', columnsToProcess['rest_type'])