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
4. I tested the function using four groups of number and confirmed my results using `len` function to filter the tested age range. I got the same results from four tests: There are 169212 between 20 and 60; 92087 between 20 and 41.5; 165565 between 1 and 40.5; 134761 between 32 and 64.

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
Install packgae 'BioPython'. 

``` 
py -m pip install BioPython
```

### Code Instructions and answers
<br/>

Step 1: Use `SeqIO` to parse the file `GCA_000001405.28_GRCh38.p13_genomic.fna` and stored the chromosome "CM000664.2" into a string `sequence`. 

Step 2: Find the total number of subsequences of 15 bases within chromosome 2. I subtracted 14 from the length of sequence because the last 14 subsequences were not in 15 bases. There were a total of 242193515 (potentially duplicated) subsequences.

Step 3: Find the number of total subsequences (counting duplicates) that do not contain more than 2 Ns. I made a for loop in the range of the entire seequence and used the `if` restriction to count numbers sequences with less than 2 'n's. (Reference: https://www.biostars.org/p/14834/). There were a total of 240548031 subsequences that do not contain more than 2 Ns. 

Step 4: Using 100 hash functions from the family provided by the question and a single pass through the sequences, estimate the number of distinct 15-mers in the reference genome's chromosome 2. 

1. Before testing the entire chromosome 2, I used the 1-hash function to find the minimal hash number for the first 15000000 of the sequence. I pass 1 into the function `get_ath_hash` as `first_hash` and paseed the first 15000000 of the sequence ([0:15000000]) into the function `frist_hash`. I got a hash value `23262025092` for this portion of sequence. 
2. Then I estimated the minimal hash number on the entire list of 15-mer subsequence using the 1-hash function. Using a for loop that went through the entire list, I compared each newly found minimal hash value to the hash number for the first 15-mer subsequence to see which one was smaller, untill I got the smallest result. At the end, I got 520 as my new minimal hash number. Converted this number on a range from 0 to 1, I divided the result by 34359738367 (I printed out this hexadecimal scale number to a decimal number) and got `1.5133991837941983e-08`. After that, I calculated my minimal distinguished number by subtracting 1 from the division of 1 over my minimal hash number. Thus, I got my minimal distinguished number `66076419`(I rounded to the whole number). 
4. Next I used a = 100 to estimate the  minmal hash number by looping through the entire list of 15-mer subsequence. My result were `80` for minimal hash value, `2.328306436606459e-09` on a scale from 0 to 1, and `429496729` as minimal distinguished number. 

Step 5: Compare my estimate change for different-sized subsets of these hash functions

1. I firsted decided to test the hash families on the first 100000 of the sequence, which I stored in a `test` list. I created a function `find_min_hash_median` that takes `a` and a `sequence` list to loop through the entire list to find out the minimal hash value. Again, I used the hash number for the first 15-mer subsequence as my initial minimal hash value. Inside the function, the outer for loop would go through a number of hash families from 1 to a, and the inner for loop would continue until finding the smallest hash value. I tested my function using 10 and 100 total hash functions and got `29120.0` and `23099.0` as my minimal median hash value, `8.47503542924751e-07` and `6.722693797396574e-07` minimal hash values divided by scale, and `1179935`and `1487498`as my minimal distinguished values. The actual distinct value for this test data set was 931157, and thus closer to the median distinct values using the median values of 10 hash functions. 
2. I also generated fake genome sequence using `random` function that consisted of different nucleic acids `['a','c','t','g','n']`. I made a for loop to join each individual numbers into the entire sequence. I encoded the sequence in `'utf8'` to ensure the sequence can be tested in the function. Then, I subsetted `fake_subseq` for the fake sequence subsetting every 15-mer as a subsequence. I used the median of 10 and 100 hash functions to estimate the distinct values. I compared my results above with the actual distinct value 16554, which were closer to the median hash value of 100 hash functions `26092`. 
4. After the testing above, I used the function I created in the previous step and repeated the same process as in the testing. But this time, I called the function to loop through the actural chronmosome 2 using different-sized subsets in 5,10, and 100.  
5. Using 5 hash functions, I got `177` as my median minimal hash value, `5.15137799099179e-09` minimal hash value divided by scale, and `194122815` for my minimal distinguished value. 
6. Using 10 hash functions, I got `247.5` as my minimal hash value, `7.203198038251232e-09` minimal hash value divided by scale, and `138827225` for my minimal distinguished value. 
7. Using 100 hash functions, I got `170.5` as my minimal hash value, `4.9622030930175156e-09` on a scale from 0 to 1, and `201523391` for my minimal distinguished number.
8. Using different hash functions to find the median hash value, I got quiet different results compared to using only one hash function. Generally, the hash value from only one hash function (a=100) was much larger than the medians from different subsets of hash functions. 
9. I found the length of a `set` of all subsequences as 145003145, which was closer to the results using the median of 10 hash functions. 

### Alternative method

I found the original method too slow to find the minimal hash value. Plus, it was not friendly to my computer's memories. Alternatively, I used `multiprocessing` function to speed up the process, by leveraging the 16 threds in my computer. I also use this method to confirm the results in my previous method.

Step 1: I created a `quick_min_hash` function that passed queue, the progress of my task, a, and the range of my task (range_l and range_r) as parameters. This function stored the minimal hash values for later comparison. It was also the `target` for my multi processors to find out the minimal hash values for the sequence.
1. Inside the function, I set a min_list that has the largest hash values. Therefore, any hash value found later will be smaller than this list of values. 
2. For each range of task (individual task distributed for each worker/processor, I stored the integer hash value of the entire sequence using sha256 function and take the reminder of bits_48 into a variable `s256`. 
3. Then, I enumerated the min hash value list from index 1, and stored the last couple digits of scale after multipling `s256` with any index inside my min_list in a variable `t`. 
4. If t was smaller than the hash value in min_list, I stored the new hash value as `t`. 
5. I calculated the percentages of the progress after completing every 100,000 subsequences.
6. I used `put` function to return the list of min hash value into the queue.

Step 2: I created a work load distribution `loaddist` function that passed the `size` of the task and `worker` as parameters. Since the size of the entire task (going through the 100 hash families) divided by my total workers would not be an interger (my computer has 8 cores 16 threads), the reminders would be evenly distributed to each worker.

Step 3: I created a `find_min_hash` function would find the minimal hash values by comparing the hash values in the min_list made above. 
1. Inside the function, I made two empty lists for the process of completing the task, and queque list for each worker's result. I again set a min_list that has the largest hash values. 
2. I called `loaddist` function to evenly distribute the task of loading all 15-mer subsequences to 16 workers.
3. I made a for loop that took the range size (range_l and range_r) as parameters. This for loop stored queuing results in a variable `q`, and used the function `Process` to target `quick_min_hash` then stored the process results in a variable `p`. After starting the multiprocessing by calling `start` function, each results from `q` and `p` would be stored in the process and queuing lists, respectively. 
4. I made another for loop that enumerated the process list which would return the processing results. Inside this for loop, I made an inner for loop that would `get` the queueing results from each worker, who compared the new hash values with the original hash values in the min_list. 
5. Finally, I ended process by joining results from all workers. 
6. I first tested the funciton on the first 1000000 of the chromosome2 sequence. 
7. I found all the min hash values for the 100 hash families. My function returned the same values as those in my previous method: for 5-hash, 10-hash, 100-hash functions, the median minimal hash values were `177, 247.5 and 170.5`, respectively. After dividing by scale, I had `5.15137799099179e-09, 7.203198038251232e-09 and 4.9622030930175156e-09`,`194122815, 138827225` and `201523391` minimal distinguished numbers for each of the five hash function above. My comparison was the same as that of my previous method. 
8. To compare the distinct values results with the actual distinct values of the subsequences, I again found that using the median of 10-hash functions would return a closer value. 
9. Because I got the same hash values results using both methods, I could convince myself they both worked. 


## Exercise 3
<br/>

Step 1: Explain what went wrong in "my friend's" code.

1.  First, it is probably that "my friend" has a 32-bit operating system. All 32-bit operating systems have a 4GB RAM limit. Therefore, it is very likely that "my friend's" operating system used all the memories when loading the file.  
2. Second, other than the memory usage in storing data, loading data in Python also consumes overhead memory about the data structure, and related procedural information of loading the data into the list . When loading the data into list, Python also creates pointers that record the location of where each element locates in the computer. These pointers consumer extra memory as reference memory.
3. Third, since the original "weights" information are string in the data. They are convereted to float objects, which consume more memories than float numbers. In addition, the file consists of high-precision weights of exactly 500 milion people, if one weight consumes 8 byte, 500 million x 8 byte is equal to 4 GB. 
4. Counting all the memories discussed above (the memories of loop through the 500 million high precision weights, the overhead memory and the reference memory) the total memories consumed would be likely over 8 GB.

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
