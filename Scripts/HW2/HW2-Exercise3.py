with open('weights.txt') as f:
    weights = []
    for line in f:
        weights.append(float(line))
print("average =", sum(weights) / len(weights))

# Explain what went wrong (6 points). 


# There are probably three reasons that can lead to overstraining the user's memory usage by loading this text file. 
# First, it is probably that "my friend" has a 32-bit operating system. All 32-bit operating systems have a 4GB RAM limit. Therefore, it is very likely that "my friend's" operating system used all the memories when loading the file.  
# Second, other than the memory usage in storing data, loading data in Python also consumes overhead memory about information of loading the data into the list and related procedural information.
# When loading the data into list, Python also creates pointers that record the location of where each element locates in the computer. These pointers consumer extra memory as reference memory.
# Third, since the original "weights" information are string in the data. They are convereted to float objects, which consume more memories than float numbers. 

# I made a test file to demonstrate how loading the text file into list consume much more memories than we think. 
# The "weights.txt" I created include a total of 30 random numbers. I used the code provided by "my firend" to load the file. 
import sys
print(sys.getsizeof(weights))

# 312

# I then imported sys and used the function "getsizeof" to get the memory size of my list. It returned 312 bytes.

# Then I wanted to see the size of individual element in my list. 

print(sys.getsizeof(weights[0]))

# 24

len(weights)
# 30

# Since there are a total of 30 elements inside my list. The total size could be 24*30 = 720 bytes, which is almost 2.3 times the original size of the list. 
# This means that Python almost doubled the size of my original data. Therefore, it is likely that "my friend"'s computer consumed more than 8 GB memories as loading the file and thus exceeded the RAM limit.

# Suggest a way of storing all the data in memory that would work (7 points), 


# I suggest storing the list of data inside an array instead of a list, which can substantially reduce the overhead memory. 
# I get this idea from a blog https://pythonspeed.com/articles/python-integers-memory/. 

import numpy as np
import random

# Storing random float numbers in an array
arr = ny.array([float(random.randint(1,1000)) for _ in range(10000)])
print(sum(arr))
# 5042391.0
print(sys.getsizeof(arr))
# 80104

# Storing random float numbers in a list
l = [float(random.randint(1,1000)) for _ in range(10000)]
print(sum(l))
# 5008535.0
print(sys.getsizeof(l))
# 85176


# Compared to the size of list, an array has a much smaller sizes. Using an array can be useful when dealing with a large amount of data. 


# Suggest a strategy for calculating the average that would not require storing all the data in memory (7 points).

# I suggest calculating the average by looping through the total weight and number of weights one by one without storing them in a list. 

# Using my test file to illustrate the result:

with open('weights.txt') as f:
    total_weight = 0
    count_weight = 0
    for line in f:
        total_weight += float(line)
        count_weight += 1     
print("average =", total_weight / count_weight)
# average = 37.38430000000001

print(sys.getsizeof(count_weight))
# 28
print(sys.getsizeof(total_weight))
# 24

# Using the code "my friend" provided:

with open('weights.txt') as f:
    weights = []
    for line in f:
        weights.append(float(line))
print("average =", sum(weights) / len(weights))
# average = 37.38430000000001

# We could see that the sizes of total_weight and count_weight are just the single size of each elements. 
# We got the same result of average weight by not storing the data. Thus, this strategy will work. 

