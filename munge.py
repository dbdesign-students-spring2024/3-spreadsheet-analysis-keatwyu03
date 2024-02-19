# place your code to clean up the data file below.

import csv
import os

#Importing the CSV file
platform_agnostic_file_path_munge = os.path.join('data', '2012_SAT_Results_20240215.csv')

f = open(platform_agnostic_file_path_munge, 'r')
readData = csv.DictReader(f)

keys = ['DBN', 'SCHOOL NAME', 'Num of SAT Test Takers', 'SAT Critical Reading Avg. Score', 'SAT Math Avg. Score', 'SAT Writing Avg. Score']

cleanedList = [keys]

#Removing all the data rows with empty elements in their data
for line in readData: 
    invalid = False
    for key in keys:
        if line[key] == 's':
            invalid = True
            break
    
    if invalid:
        pass
    else:
        temp = []
        for place in keys:
            temp += [line[place]]
        cleanedList += [temp]


#Creating a new CSV file that stores the munged data
newFile = os.path.join('data', 'cleaed_data.csv')

newF = open(newFile, 'w')

#Storing the data (post munging) into the new csv file
#There is one step of munging here that checks whether or not the row follows proper syntax
#If the data row does not follow the syntax, then we can omit it as well
for j in range(0, len(cleanedList)):
    line = ''

    for val in cleanedList[j]:
        line += val + ','
    
    numItems = line.count(',')

    if numItems != 6:
        continue

    newF.write(line)
    if j != len(cleanedList) - 1:
        newF.write('\n')


