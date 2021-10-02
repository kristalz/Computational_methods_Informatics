# Examine the contents of hw2-patients.xml  Download hw2-patients.xml in a text-editor to see its structure, 
# but in brief, there are a handful of fields you can ignore for this exercise and then several <patient> entries, 
# all contained inside <patients>. Each <patient> has several attributes that we will want, namely name, age, and gender. 
# Some patients have other associated data (e.g. diagnoses), but we won't need that here.


# Load the data. 
# Do any of the patients share the same exact age? (2 points) How do you know? (2 points).

# Installation 
# py -m pip install lxml

from xml.dom import minidom # reference: https://www.studytonight.com/python-howtos/how-to-read-xml-file-in-python

# parse the xml file by name
file = minidom.parse('hw2-patients.xml')

# use getElementsByTagName() to get tag
patients = file.getElementsByTagName('patient')

# find all patient ages
age = []
for elem in patients:
    age.append(float(elem.attributes['age'].value))
age

# Plot a histogram showing the distribution of ages (2 points). 
from matplotlib import pyplot as plt

plt.hist(age, bins=50, edgecolor='black')  
plt.ylabel('Frequency')
plt.xlabel('Age')
plt.show()

# Do any of the patients share the same exact age? (2 points) How do you know? (2 points).

print(len(age) == len(set(age))) # Reference: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list

# True

# Because "set" does not allow duplication. “True" means that no patients sharing the same exact age. 



# Plot the distribution of genders. (2 points). 
# In particular, how did this provider encode gender? What categories did they use? (2 points)


# find all patient genders 
gender = []
for elem in patients:
    gender.append(elem.attributes['gender'].value)
gender

plt.hist(gender, bins=5, edgecolor='black')
plt.ylabel('Frequency')
plt.xlabel('Gender')
plt.show()

# This provider encoded gender in "string". They classified gender in categories "male", "female", and "unknown". 

# Sort the patients by age and store the result in a list (use the "sorted" function with the appropriate key, 
# or implement sort yourself by modifying one of the algorithms from the slides or in some other way). (2 points) 
# Who is the oldest patient? (2 points).

name = []
for elem in patients:
    name.append(elem.attributes['name'].value)
name

patient = list(zip(name, age))
patient

sorted_patient = sorted(patient, key=lambda patient: patient[1], reverse=True) # reference: https://www.w3schools.com/python/python_lambda.asp
sorted_patient

oldest_patient_name = sorted_patient[0][0]
oldest_patient_age = sorted_patient[0][1]
print(f'The oldest patient is {oldest_patient_name}.')

# The oldest patient is Monica Caponera.

# Identifying the oldest person from a list sorted by age should be an O(1) task... 
# but sorting is an O(n log n) process (assuming we're using an efficient algorithm), 
# so the total time for the above is O(n log n). Describe how (you don't need to implement this, 
# unless that's easier than writing it out) you could find the second oldest person's name in O(n) time. (2 points).


# First I can use find max function to find the oldest patient's age. 
# Then I could loop through the entire list to find which patient's age is the largest after removing the oldest one. Thus it is O(n) time.

# Discuss when it might be advantageous to sort and when it is better to just use the O(n) solution. (2 points).


# It might be advantageous to sort the list when I want to quickly return the value and when the number of items in the list is relatively large (n is large).
# It is better to just use the O(n) solution when I do not want to change the orginal list and when n is small. 

# Recall from our discussion of the motivating problem for September 9th that we can search within a sorted list in O(log n) time via bisection. 
# Use bisection on your sorted list (implement this yourself; don't trivialize the problem by using Python's bisect module) to identify the patient who is 41.5 years old. (2 points)


def binary_search(arr, val): # reference: https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7
    n = len(arr)
    left = 0
    right = n

    while left < right:
        middle = (left + right)//2
        if val < arr[middle]:
            right = middle
        else:
            left = middle + 1
    return middle
    raise ValueError('Value is not in the list')

sorted_age = sorted(age)
sorted_age
print(binary_search(sorted_age, 41.5))
# 173886

# Find the patient's name 
sorted_patient_asc = sorted(patient, key=lambda patient: patient[1])
patient_name = sorted_patient_asc[173886][0]
print(patient_name)
# Output: John Braswell

# Once you have identified the above, use arithmetic to find the number of patients who are at least 41.5 years old. (2 points)
print(len(sorted_patient_asc) - 1 - 173886 + 1)

# Output: 150471


# Generalizing the above, write a function that in O(log n) time returns the number of patients who are at least low_age years old but are strictly less than high_age years old. (2 points) 
# Test this function (show your tests) and convince me that this function works. (2 points). 
# (A suggestion: sometimes when you're writing high efficiency algorithms, it helps to make a slower, more obviously correct implementation to compare with for your tests. 
# Be sure your function works both for ages that are and are not in the dataset.)
  

def find_num_age_range(arr, low_age, high_age):
    n = len(arr)
    left = 0
    right = n

    while left < right:
        middle_low = (left + right)//2
        if low_age < arr[middle_low]:
            right = middle_low
        elif low_age > arr[middle_low]:
            left = middle_low + 1
        else:
            break
    middle_low = left   

    left = 0
    right = n

    while left < right:
        middle_high = (left + right)//2
        if high_age < arr[middle_high]:
            right = middle_high
        elif high_age > arr[middle_high]:
            left = middle_high + 1
        else:
            break
    middle_high = right
    
    print(f"There are {middle_high-middle_low} patients between {low_age} and {high_age}.")
 

# Test the function 

test1= find_num_age_range(sorted_age,20,60)
# There are 169212 patients between 20 and 60.
count1 = len([x for x in sorted_age if x>=20 and x<60])
print(count1) # 169212
# The results are the same.

test2 = find_num_age_range(sorted_age, 20, 42)
# There are 94319 patients between 20 and 42.
count2 = len([x for x in sorted_age if x>= 20 and x < 42])
print(count2) # 94319
# The results are the same.

test3 = find_num_age_range(sorted_age, 1, 40.5)
# There are 165565 patients between 1 and 40.5.
count3 = len([x for x in sorted_age if x>= 1 and x < 40.5])
print(count3) # 165565
# The results are the same.

test4 = find_num_age_range(sorted_age, 32, 64)
# There are 134761 patients between 32 and 64.
count4 = len([x for x in sorted_age if x>= 32 and x < 64])
print(count4) # 134761
# The results are the same.

# Modify the above, including possibly the data structure you're using, to provide a function that returns both the total 
# number of patients in an age range AND the number of males in the age range, all in O(log n) time as measured after any initial data setup. (2 points). 
# Test it (show your tests) and justify that your algorithm works. (2 points)

patient_new_list = list(zip(name, age, gender))
sorted_patient_new_list_asc = sorted(patient_new_list, key=lambda patient: patient[1])
sorted_patient_new_list_asc


# Create a list that only included male patients in the same age range. 

tar_list = ['male'] # target list is male patients
res = [tup for tup in sorted_patient_new_list_asc if any(i in tup for i in tar_list)] # reference: https://www.geeksforgeeks.org/python-filter-tuples-according-to-list-element-presence/
sorted_age_male = [x[1] for x in res]
sorted_age_male

def find_num_age_range_new(arr, arr_male, low_age, high_age):
    if low_age<high_age:
        find_num_age_range(arr, low_age, high_age)
        find_num_age_range(arr_male, low_age, high_age)
    else:
        False

# Test it (show your tests) and justify that your algorithm works. (2 points)

test1 = find_num_age_range_new(sorted_age, sorted_age_male, 20, 60)
# There are 169212 patients between 20 and 60.
# There are 83542 patients between 20 and 60.
count1 = len([x for x in sorted_age if x>= 20 and x < 60])
print(count1) # 169212
count1_male = len([x for x in sorted_age_male if x>= 20 and x < 60])
print(count1_male) # 83542
# The results are the same.

test2 = find_num_age_range_new(sorted_age, sorted_age_male, 30, 70)
# There are 160608 patients between 30 and 70.
# There are 78247 patients between 30 and 70.
count2 = len([x for x in sorted_age if x>= 30 and x < 70])
print(count2) # 160608
count2_male = len([x for x in sorted_age_male if x>= 30 and x < 70])
print(count2_male) # 78247
# The results are the same.

test3 = find_num_age_range_new(sorted_age, sorted_age_male, 10, 35)
# There are 105076 between 10 and 35.
# There are 52797 between 10 and 35.
count3 = len([x for x in sorted_age if x>= 10 and x < 35])
print(count3) # 105076
count3_male = len([x for x in sorted_age_male if x>= 10 and x < 35])
print(count3_male) # 52797
# The results are the same.

test4 = find_num_age_range_new(sorted_age, sorted_age_male, 5, 40)
# There are 147090 between 5 and 40.
# There are 74149 between 5 and 40.
count4 = len([x for x in sorted_age if x>= 5 and x < 40])
print(count4) # 147090
count4_male = len([x for x in sorted_age_male if x>= 5 and x < 40])
print(count4_male) # 74149
# The results are the same.