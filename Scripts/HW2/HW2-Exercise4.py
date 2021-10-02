# Identify a data set online (10 points) that you find interesting that could potentially be used for the final project; the main requirements is that there needs to be many (hundreds or more) data items with several identifiable variables, 
# at least one of which could be viewed as an output variable that you could predict from the others.

import pandas as pd 

access_and_use_telemedicine = pd.read_csv('Access_and_Use_of_Telemedicine_During_COVID-19.csv') 
# Downloaded from https://healthdata.gov/dataset/Access-and-Use-of-Telemedicine-During-COVID-19/c835-etjt. 
access_and_use_telemedicine.head()
print(len(access_and_use_telemedicine)) # 798

# Describe the dataset (10 points) Your answer should address (but not be limited to): 
# how many variables? 

prin(list(access_and_use_telemedicine.columns))
# ['Round','Indicator','Group', 'Subgroup', 'Sample Size', 'Response', 'Percent', 'Standard Error', 'Suppression', 'Significant 1', 'Significant 2']
print(len(list(access_and_use_telemedicine.columns)))
# There are 11 variables. 

# Are the key variables explicitly specified or are they things you would have to derive (e.g. by inferring from text)? 

# The variables inside the dataset are straight-forward and explicily specified. "Groups" represent age, race, sex, education level, urbanization, and selected chronic conditions in the study. 
# "Subgroups" represent the subctegories within each group. For example, "18-44 years" is a subrgoup for age group. 
# For different purposes or the questions I will be interested in my final project, I might divide or group the age group into different age ranges. 
# For instance, if I am interested in knowing how compare middle-age people (before 65) and the elderly using telemedicine during COVID, I will group people from "18-44" and "44-64" together for analysis. 

# The binary responses 0 and 1 under "Significance 1" and "Significance 2" indicates the estimated significance testing of difference  at the 5% significance level from Round 1 and Round 2, respetively. 
# I need to look up the description for the dataset (https://data.cdc.gov/NCHS/Access-and-Use-of-Telemedicine-During-COVID-19/8xy9-ubqz) to interpret thses responses. 

# Are any of the variables exactly derivable from other variables? (i.e. are any of them redundant?) 

# There might be overlapped numbers of people into different subgroups. For example, there might be intersection of people who are Hispanic and aged between "18-44 years". 

# Are there any variables that could in principle be statistically predicted from other variables? How many rows/data points are there? 

# All groups (i.e., age, race, sex, education level, urbanization, and selected chronic conditions) can serve as predictors for the variables "Response" of using telemedicine during COVID. 

# Age: 
age = len(access_and_use_telemedicine[access_and_use_telemedicine['Group'] == 'Age group'])
print(f"There are {age} rows in age group")
# There are 126 rows in age group

# Race:
race = len(access_and_use_telemedicine[access_and_use_telemedicine['Group'] == 'Race/Hispanic origin'])
print(f"There are {race} rows in race group")
# There are 168 rows in race group

# Sex:
sex = len(access_and_use_telemedicine[access_and_use_telemedicine['Group'] == 'Sex'])
print(f"There are {sex} rows in sex group")
# There are 84 rows in sex group

# Education level:
education = len(access_and_use_telemedicine[access_and_use_telemedicine['Group'] == 'Education'])
print(f"There are {education} rows in education level group")
# There are 126 rows in education level group

# Urbanization:
urbanization = len(access_and_use_telemedicine[access_and_use_telemedicine['Group'] == 'Urbanization'])
print(f"There are {urbanization} rows in urbanization level group")
# There are 84 rows in urbanization level group

# Selected chronic conditions:
chronic_con = len(access_and_use_telemedicine[access_and_use_telemedicine['Group'] == 'Chronic conditions'])
print(f"There are {chronic_con} rows in selected chronic conditions group")
# There are 168 rows in selected chronic conditions group

# Is the data in a standard format? If not, how could you convert it to a standard format?

# The data is in a standard format because each element is in their atomic form in a separate cell. For instance, the number of people responding using telemedicine in "18-44 years" are separated from those who age in "65 years and over". 

# Describe the terms of use and identify any key restrictions (e.g. do you have to officially apply to get access to the data? Are there certain types of analyses you can't do?)

# This dataset is opened to public use so I do not haave to officially apply to get permission to download the data. 