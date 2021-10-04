# Assignment 1 

Author: Kristal Zhou

Date: 10/7/2021

## Exercise 1 
<br/>

### Data 

Download patients xml file `"hw2-patients.xml"`(<https://yale.instructure.com/courses/70314/files/5401025?wrap=1>) from Canvas<br/>

### Installation Instruction 
<br/> 
Install packgae 'lxml' to load the xml file. 

``` 
py -m pip install lxml
```

### Code Instructions and answers
<br/>
Step 1: Use minidom to parse the xml file (reference: https://www.studytonight.com/python-howtos/how-to-read-xml-file-in-python)

Step 2: Parse the xml file by name

Step 3: Use getElementsByTagName() to get tag and rename the xml file as `Patients`

Step 3: Find all patient ages and store them in the list `age`

Step 4: Import matplotlib to plot a histogram of `age`

![hw2_exercise1_plot1](https://github.com/kristalz/BIS634/blob/main/Images/hw2_exercise1_plot1.jpg)

Step 5: Find if there are any patients share the same age. I changed the `age` from a list to a set, and compare it with the original list. Because "set" does not allow duplication. (Reference: https://stackoverflow.com/questions/1541797/how-do-i-check-if-there-are-duplicates-in-a-flat-list) 

I got a result `True`, which meant that no patients sharing the same exact age. 

### For an extra 2 points: explain how the answer to the question about multiple patients having the same age affects the solution to the rest of the problem.

If multiple patients having the same age, there would be multiple locations in when we want to find the index of a specific age. Therefore, there would be different number of patients in certain age range depending on the indexes of the age bound I set. For example, if I want to find the index of age 25 and suppose from index [1000] and [1005] represent age 25 after sorting the list. Then I need to find the first index that represent age 25 also to count all the numbers of patients with the same age. 

Step 6: Find all patient genders and store them in the list `gender`. Plot a histogram of `gender`.
![hw2_exercise1_plot2](https://github.com/kristalz/BIS634/blob/main/Images/hw2_exercise1_plot2.jpg)

This provider encoded gender in "string". They classified gender in categories "male", "female", and "unknown". 

Step 7: Sort the patients by age and store the result in a list and find the oldest patient.

1. I created another list `name` to store all the patients' names.
2. I use `zip` function to store patients' names and ages into a tuple then store in a list `patients`. 
3. I use the function `sort` to sort the list `patients` by age in descending order. (Reference: https://www.w3schools.com/python/python_lambda.asp)
4. I printed out the oldeset patient's name by using index [0] in the list: Monica Caponera. 

Step 8: Describe how you could find the second oldest person's name in O(n) time. Discuss when it might be advantageous to sort and when it is better to just use the O(n) solution.

1. First I can use find `max` function to find the oldest patient's age. Then I could loop through the entire list to find which patient's age is the largest (the new oldest age) after removing the oldest one. Thus it is O(n) time. 

2. It might be advantageous to sort the list when I want to quickly return the value and when the number of items in the list is relatively large (n is large). It is better to just use the O(n) solution when I do not want to change the orginal list and when n is small. 

Step 9: Use bisection on your sorted list to identify the patient who is 41.5 years old. 

1. I created a function `binary_search` that took the sorted age list and a specific age as parameter, then returned the index of the age I wanted to find. For every comparison between the age I wanted to find and the middle age in the list, if the middle age was larger, I decreased the searching size to the left side of the middle age, and to the right side if the middle age was smaller. If the age I wanted to find was equal to the value in the middle age, the function would return the middle. The function would repeat the steps above until the specific age was found or the left bounder was equal or higher than the right age bound.(Reference: https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7). 

2. Because my function took the left side as the lower age bound and right side as the upper age bound, I made an ascending age list using `sorted` function and returned a list `sorted_age`. 
3. I found the location of age 41.5 as [173886]. I then sorted the `patients` list I made earlier in an ascending order and returned the patient name by using the index I found. The patient name was `John Braswell`. 

Step 10: To find the number of patients who are at least 41.5 years old, I used the total number of the ascending sorted patient list (by using `len` function minus 1 to get the index of the last patient) minus the index I found above and added 1 for take into the count of patient at 41.5 years old. The total number I got was 150571. 

Step 11: Generalizing the above, write a function that in O(log n) time returns the number of patients who are at least low_age years old but are strictly less than high_age years old. 

1. I created a function `find_num_age_range` that took the ascending sorted age list, the low_age, and the high_age as parameters. 
2. In the function, I made two while loops using the one I made in my original `binary_search` funciton with some modifications to find the positions of `low_age` and `high_age`, respectively. I exited the while loops when the low or high ages were neither smaller nor larger than the middle age in their searching area. The middle age in the searching area for the `low_age` (`middle_low`) would become left(low) bound, while the middle age for the `high_age` searching area (`middle_high`) would become the right(high) bound. Then I returned the difference between `middle_low` and `middle_high` as differences in low and high age's indexes.
3. This function would work because finding the indexes of the both low and high age using the modified `binary_search` function I described above took O(log n) time. Therefore, the entire function was 2 x O(log n) time and still in O(log n) time. 
4. I tested the function using four groups of number and confirmed my results using `len` function to filter the tested age range. I got the same results from four tests: There are 169212 between 20 and 60; 94319 between 20 and 42; 165565 between 1 and 40.5; 134761 between 32 and 64.

Step 12: Modify the above, to provide a function that returns both the total number of patients in an age range AND the number of males in the age range, all in O(log n) time as measured after any initial data setup.

1. I made another list `patient_new_list` that store patient's genders with ages and names in tuples. 
2. I sorted `patient_new_list` in an ascending order. 
3. I extracted a list that only included male patients and named it as `res`. (Reference: https://www.geeksforgeeks.org/python-filter-tuples-according-to-list-element-presence/). Then I sorted `res` in an ascending order as `sorted_age_male`. 
4. I created a function `find_num_age_range_new` that took the ascending sorted age list, the ascending sorted male age list, the low_age, and the high_age as parameters. Inside the function, I simply used the function `find_num_age_range` I created earlier to count the number between of low_age and high_age in both sorted age and sorted male age list. 
5. Again, this function took O(log n) time because the each search used O(log n) going through thet total and male age lists. The entire function was 4 x O(log n) and still in O(log n). 
6. I tested my function using 4 different groups and used the `len` function to confirm my results. Using both methods returned the same results: Test 1: There are 169212 in total and and 83542 in males between 20. Test 2: There are 160608 in total and 78247 in males between 30 and 70. Test 3: There are 105076 in total and 52797 in males between 10 and 35. Test 4: There are 147090 in total and 74149 in males between 5 and 40.

## Exercise 2
<br/>

### Data 

Download Genome(GRCh38.p13) from <https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.28_GRCh38.p13/GCA_000001405.28_GRCh38.p13_genomic.fna.gz>. 
<br/>

### Installation Instruction 
<br/> 
Install package 'BioPython'. 

``` 
py -m pip install BioPython
```

### Code Instructions and answers
<br/>

Step 1: Create a fake data set to estimate the distinct values. 

1. I first generated a fake genome sequence using `random` function that consisted of 10000 different nucleic acids `['a','c','t','g','n']`. I set a `random.seed(1)` for reproducible randomness. I made a for loop to join each individual numbers into the entire sequence. I encoded the sequence in `'utf8'` to ensure the sequence can be tested in the function. Then, I subsetted `fake_subseq` for the fake sequence into each 15-mer as a subsequence. I found out there were 9986 true distinct sequences by using `len` function over the `set` of the fake subsequences(`set` does not contain duplicated elements). 
2. I made a `estimate_distinct_values` function that passed `a` and a sequence `seq` as parameters. Inside the function, I created an empty list that would later store the minimal hash values. I made a for loop that went through the entire sequence in a range of `a`, compared each newly found minimal hash value to the hash number for the first 15-mer subsequence to see which one was smaller, and stored the smallest results after divided by the scale. I converted the list of hash numbers to an array because arrays would save lots of memories. 
3. After that, I used four different strategies to estimate the distinct values: 1) Calculate the average min hash values first then estimate the distinct value; 2) calculate the median min hash values first then estimate the distinct value; 3) calculate the distinct values for each hash first then take the average of them; 4) calculate the distinct values for each hash first then take the median of them. I returned the result for each approach at the end of my function. 
4. I pass `a=100` for my function created above because it would printed out all hash values at once. Then I plot my estimate results for the fake sequence.

![estimate_test_results](https://github.com/kristalz/BIS634/blob/main/Images/estimate_test_results.jpg)

5. According to the results above, using the average of all minimal hash numbers to estimate the distinct values wass closest to the actual distinct value `9986` (blue line in the plot), whereas calculating the distinct values first then take the average was furthest away from the true value(green line). While all four lines were quite vasillating using small sized hash functions, only the green line (calculate the distinct values for each hash first then take the average of them) did not converage over about 25 hash functions. Note that the yellow line and red line almost overlapped, inferring that the estimate results were about the same either calculate the median first or after to estimate the distinct values. Therefore, according to this result, I decided to use the first stratege(calculate the average min hash values first then estimate the distinct value) to estimate the distinct 15-mer in chromosome2. 

Step 2: Find all 15-mer subsequences and estimate the distinct values of subsequences in chromosome2. 

1. I used a for loop to find all 15-mers subsequences of 15 bases within chromosome2 in the range of the entire length of `sequence` after subtracting the last 14 indexes. (Reference: https://www.biostars.org/p/14834/). I subtracted 14 from the length of sequence because the last 14 subsequences did not contrain 15 bases. There were a total of 242193515 (potentially duplicated) subsequences.
2. To find the number of total subsequences (counting duplicates) that do not contain more than 2 Ns, I made a for loop in the range of the subsequence and used the `if` condition to count numbers sequences with less than 2 'n's (I used `count`b'n because the sequence was encoded). There were a total of 240548031 subsequences that do not contain more than 2 Ns. 
3. I found the length of a `set` of all subsequences as `145003145`, the true distinct value.
4. After the testing above, I used the function I created in step 1 to estimate the distinct values of subsequences in the actual chronmosom 2 sequence. Again, I passed a=100 in the function to get all hash values. I also printed out all estimated values for single `a` hash functions . 
5.  Then I printed out the estimated distinct values for different-sized subsets (a=1, a=1 to 10, and a=1 to 100): `66076419, 138827225, and 201523391`. From the results, I found that the estimated value by using the median of 10 hash functions was closer to the true distinct value `145003145`. This was different from my testing result above.
6. In both cases, I got quiet different results compared to using only one hash function using different hash functions to find the median hash value. Generally, there were more variations in the estimated values by using only one hash function than those of the medians from different subsets of hash functions. I realized that the estimation would be more accurate (or smoother) using different subsets of hash functions compared to only using one. As the size of dataset increased (earlier I used the a fake sequence that only had 10000 elements and then here the entire sequence), there were also more variations between the estimated values and the actual value. Greater accuracies were observed in the smaller/median sized dataset when using larger size of hash functions.

### Alternative method

Alternatively, I used `multiprocessing` function to speed up the process finding all minimal hash value. I also use this method to confirm the results in my previous method.

Step 1: I created a `quick_min_hash` function that passed queue, the progress of my task, a, and the range of my task (range_l and range_r) as parameters. This function stored the minimal hash values for later comparison. It was also the `target` for my multi processors to find out the minimal hash values for the sequence.
1. Inside the function, I set a min_list that has the largest hash values. Therefore, any hash value found later will be smaller than this list of values. 
2. For each range of task (individual task distributed for each worker/processor, I stored the integer hash value of the entire sequence using sha256 function and take the reminder of bits_48 into a variable `s256`. 
3. Then, I enumerated the min hash value list from index 1, and stored the last couple digits of scale after multipling `s256` with any index inside my min_list in a variable `t`. 
4. If t was smaller than the hash value in min_list, I stored the new hash value as `t`. 
5. I calculated the percentages of the progress after completing every 1000000 subsequences.
6. I used `put` function to return the list of min hash value into the queue.

Step 2: I created a work load distribution `loaddist` function that passed the `size` of the task and `worker` as parameters. Since the size of the entire task (going through the 100 hash families) divided by my total workers would not be an interger (my computer has 8 cores 16 threads), the reminders would be evenly distributed to each worker.

Step 3: I created a `find_min_hash` function would find the minimal hash values by comparing the hash values in the min_list made above. 
1. Inside the function, I made two empty lists for the process of completing the task, and queque list for each worker's result. I again set a min_list that has the largest hash values. 
2. I called `loaddist` function to evenly distribute the task of loading all 15-mer subsequences to 16 workers.
3. I made a for loop that took the range size (range_l and range_r) as parameters. This for loop stored queuing results in a variable `q`, and used the function `Process` to target `quick_min_hash` then stored the process results in a variable `p`. After starting the multiprocessing by calling `start` function, each results from `q` and `p` would be stored in the process and queuing lists, respectively. 
4. I made another for loop that enumerated the process list which would return the processing results. Inside this for loop, I made an inner for loop that would `get` the queueing results from each worker, who compared the new hash values with the original hash values in the min_list. 
5. Finally, I ended process by joining results from all workers. 
6. I first tested the funciton on the first 1000000 of the chromosome2 sequence. My function returned a list of all hash values. I then took the median of all 100 hash functions, 1 hash function, and 10 hash functions: `23099.0, 37244 and 29120.0`, respectively. After dividing by scale, I had `6.722693797396574e-07, 1.083943061562137e-06 and 8.47503542924751e-07`,`1487497.9552361574, 922556.683573193` and `1179935.0702953297` as minimal distinguished numbers, respectively. I found that using the median of 10 hash functions would be closer to the actual distinct value `931157`. 
7. Then, I used the function to find all the min hash values for the 100 hash families. My function returned the same values as those in my previous method: For first 5 hash, first 10 hash, and all 100 hash functions, the median minimal hash values were `177, 247.5 and 170.5`, respectively. After dividing by scale, I had `5.15137799099179e-09, 7.203198038251232e-09 and 4.9622030930175156e-09`,`194122815, 138827225` and `201523391` minimal distinguished numbers for each of the five hash function above. My comparison was the same as that of my previous method. 
8. To compare the results of distinct values with the actual distinct values of the subsequences, I again found that using the median of 10 hash functions would return a closer value. Thus, both the test case (first 1000000 of the chromosome2 sequence) and the actual case (he entire chromosome2 sequence) confirmed my conclusion using the previous method. 


## Exercise 3
<br/>

Step 1: Explain what went wrong in "my friend's" code.

1.  First, it is probably that "my friend" has a 32-bit operating system. All 32-bit operating systems have a 4 GB RAM limit. Therefore, it is very likely that "my friend's" operating system used all the memories when loading the file.  
2. Second, the file consists of high-precision weights of exactly 500 milion people, if one weight consumes 8 bytes, 500 million x 8 byte is equal to 4 GB. Since the original "weights" information are string in the data. They are convereted to float objects, which consume more memories than float numbers. 
3. In addition, other than the memory usage in storing data, loading data in Python also consumes overhead memory about the data structure, and related procedural information of loading the data into the list . There would be 16 bytes to describe the the metadata for each float. Moreover, list would also consume extra 56 bytes to describe the metadata for itself. Therefore, 4 GB (to store the 500 million float numbers above)+56 bytes+16 bytes*500 miliion ≈ 12 GB! No wonder "my friend"'s operating system would run out of memories. 
5. Finally, when loading the data into list, Python also creates pointers that record the location of where each element locates in the computer. These pointers consume extra memories as reference memory. 
6. Thus, counting all these memory usages discussed above, the total memories consumed would be likely two times over 8 GB, "my friend" RAM limit.

Plese see my script for an illustration of an example that showing the affects of extra memories that Python created when loading a file. 

Step 2: Suggest a way of storing all the data in memory that would work

I suggest storing the list of data inside an array instead of a list, which can substantially reduce the overhead memory. I get this idea from a blog https://pythonspeed.com/articles/python-integers-memory/. The entire size of an array is much smaller than a list when we have lots of data. However, this difference in sizes is not significant if we only have a small amount of data. (I showed an example in my script for this suggestion.)

I also suggest switching to lower precision floating points to save more memories. 

Step 3: Suggest a strategy for calculating the average that would not require storing all the data in memory. 


I suggest calculating the average by looping through the total weight and number of weights one by one without storing them in a list. The code was displayed below: 

```
with open('weights.txt') as f:
    total_weight = 0
    count_weight = 0
    for line in f:
        total_weight += float(line)
        count_weight += 1     
print("average =", total_weight / count_weight)
```
In this way, we do not need to store any data but still got the total_weight and count_weight everytime we looped through the file. I would get the average weight at the end. Please see an example illustrated in my script that returned the same average weight using the code I modified and the code provided by "my friend." 

## Exercise 4
<br/>

I identified a dataset about access and use of telemedicine during COVID 19 from HealthData.gov <https://healthdata.gov/dataset/Access-and-Use-of-Telemedicine-During-COVID-19/c835-etjt>. This dataset came from the Research and Development Survey (RANDS), a platform that conducts commercial survey panels for research at the National Center for Health Statistics (NCHS). 

During COVID-19 quarantine time, telemedicine offers an opportunity for patients to access healthcare without potential risk for pandemic exposure. RANDS conducted three rounds of surveys (between June 9, 2020 and July 6, 2020, August 3, 2020 and August 20, 2020, and May 17, 2021 and June 30, 2021) for people at least 18 years old to show the percentages of U.S. adults 1) who have a usual place of care and a provider that offered telemedicine in the past 2 months, 2) who used telemedicine in the past 2 months, or 3) who have a usual place of care and a provider that offered telemedicine prior to the pandemic. 

I downloaded the csv data and stored it as a panda dataframe in `access_and_use_telemedicine`. I examined the head of the dataframe. 
![hw2_exercise4_dataset](https://github.com/kristalz/BIS634/blob/main/Images/hw2_exercise4_dataset.jpg)

There are 11 variables in the data: 'Round','Indicator','Group', 'Subgroup', 'Sample Size', 'Response', 'Percent', 'Standard Error', 'Suppression', 'Significant 1', 'Significant 2'. 

The variables inside the dataset are straight-forward and explicily specified. "Groups" represent age, race, sex, education level, urbanization, and selected chronic conditions in the study. 
"Subgroups" represent the subctegories within each group. For example, "18-44 years" is a subrgoup for age group. For different purposes or the questions I will be interested in my final project, I might divide or group the age group into different age ranges. For instance, if I am interested in knowing how compare middle-age people (before 65) and the elderly using telemedicine during COVID, I will group people from "18-44" and "44-64" together for analysis. 

The binary responses 0 and 1 under "Significance 1" and "Significance 2" indicates the estimated significance testing of difference  at the 5% significance level from Round 1 and Round 2, respetively. I need to look up the description for the dataset (https://data.cdc.gov/NCHS/Access-and-Use-of-Telemedicine-During-COVID-19/8xy9-ubqz) to interpret thses responses. 

There might be overlapped numbers of people into different subgroups. For example, there might be intersection of people who are Hispanic and aged between "18-44 years". 

All groups (i.e., age, race, sex, education level, urbanization, and selected chronic conditions) can serve as predictors for the variables "Response" of using telemedicine during COVID. There are totla of 126 row in age and education level groups, 168 rows in race and chronic condition groups, as well as 84 rows in sex and urbanization groups. 

The data is in a standard format because each element is in their atomic form in a separate cell. For instance, the number of people responding using telemedicine in "18-44 years" are separated from those who age in "65 years and over". 

This dataset published by Centers for Disease Control and Prevention is owned by HHS Office of the Chief Data Officer. It is opened to public use so I do not have to officially apply to get permission to download the data. The section "Limitation and data use" from their "Technical Note" document (https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm#limitations) did not sepcify any restrictions on the data use. But they did mention some limitations about their data collection and statistical methods. Theystressed that the p-value used in their 3 rounds investigation should not be the only consideration for making decisions.
