# Assignment 1 

Author: Kristal Zhou

Date: 9/16/2021

## Exercise 1 
<br/>

### Code Instructions and answers
<br/>

Step 1: Define a function `temp_tester` that takes parameter for tested temperature as `temp`.

Step 2: Within funciton `temp_tester`, define a `judge` function that determines the normal temperature range and takes parameter for normal temperature as `normal_temp`.

Step 3: Within function `judge`, creates a condition for normal temperature range: if the absolute value of `normal_temp` minus the tested temperature `temp` is within 1 celsius, return `True`; otherwise, return `False`. 

Step 4: Return function `judge` that prints out the result of the tested temperature `temp`.

```
def temp_tester(temp):
    def judge(normal_temp):
        if abs(normal_temp - temp) <= 1:
            return True
        else:
            return False

    return judge

```

### Test the Function
</br>

```
human_tester = temp_tester(37) 
chicken_tester = temp_tester(41.1)

print(chicken_tester(42)) # True
print(human_tester(42))   # False
print(chicken_tester(43)) # False
print(human_tester(35))   # False
print(human_tester(98.6)) # False 
```

## Exercise 2
</br>

### Data 

Population database `"hw1-population.db"`(<https://yale.instructure.com/courses/70314/files/5320045?wrap=1>) from Canvas

### Installation Instructions
</br>
Install packages `pandas` and `sqlite3` in the terminal using the following codes:

```
py -m pip install pandas

py -m pip install sqlite3

py -m pip install plotnine
```


### Code Instructions and Answers
<br/>

Step 1: Import `pandas` and `sqlite3`, then load `"hw1-population.db"`(<https://yale.instructure.com/courses/70314/files/5320045?wrap=1>) as pandas DataFrame.

Step 2: After examining the `head` of the data, return column names of the dataframe using `list(data.columns)`.

['name', 'age', 'weight', 'eyecolor']

Step 3: Find the number of rows in the data by using `len(data["name"]).`

152361

Step 4: Examine the distribution of ages

1. Find the mean, standard deviation, minimum, and maximum by using the built-in function `mean()`,`std()`, `min()`, `max()` 
```
print(mean_age) # 39.51052792739697
print(sd_age) # 24.152760068601573
print(min_age) # 0.0007476719217636152
print(max_age) # 99.99154733076972
```
2. Plot a histogram distribution by using plotnine: `import plotnine as p9`. Then return the histogram using `geom_histogram`. Here, I used `bin = 100` because the `age` roughly ranged from birth to 100. The number of bins affect the ability of a histogram to identify the underlying trends of data.

![age_distribution](https://github.com/kristalz/BIS634/blob/main/Images/age_distribution.png)

3. The majority of ages spaned from 1 to 70 with about 2,000 people, while there were equal to or less than 500 people age from 70 to 99. The outlier groups was about 100 years old with less than 250 people. 

```
print(mean_weight) # 60.884134159929715
print(sd_weight) # 60.884134159929715
print(min_weight) # 3.3820836824389326
print(max_weight) # 100.43579300336947
```

Step 5: Examine the distribution of weights
1. Repeat items 1&2 in Step 4 but change `age` to `weight`. I originally used the same number of bins as above. But that would overly squeeze the bin_width. I adjusted the `bin` to 50 instead for better visualization. 

![weight_distribution](https://github.com/kristalz/BIS634/blob/main/Images/weight_distribution.png)

2. It turned out that the outlier group was population that weighed around 60, while the majority population weighed between 60 to 65. 

Step 6: Make a scatterplot of the weights vs the ages and determine the relationship between them. 

1. Use `geom_point` to plot weights over ages. 

![weight_vs_age](https://github.com/kristalz/BIS634/blob/main/Images/weight_vs_age.png)

2. Weights increased almost linearly with ages from birth to about 20, then become steady afterwards. People who weighed more at birth also weighed more in their adulthood. 

Step 7: Find the outlier in the scatterplot and return the person name. (Edit 9/12: I realized I did a long way to find the outlier originally. In fact, I could have done it faster and got the same answer. I include both ways display as following.)

The short way: 

1. From the scatterplot I knew that the outlier aged between 25 and 50. Thus I locate a group of population in this age group using the following code:
```
data_outlier = data[data["age"] >= 25]
data_outlier = data_outlier[data_outlier["age"] <= 50]
```

2. Again from the scatter plot I knew that the outlier weighed roughly below 25. Therefore, I can simply found the data_outlier whose weight was under 25. 
```
data_outlier[data_outlier["weight"] < 25]["name"]
```

I got the answer "Anthony Freeman".

The long way: (Use the interquantile range(IQR) in the following steps)

1. Use `data.describe()` to visualize the statistics of the data, which summarize the distribution of ages and weights in 25, 50 , 75% groups respectively. 

![weight_age_stats](https://github.com/kristalz/BIS634/blob/main/Images/weight_age_stats.png)

2. Find the 1st and 3rd quantile of weights by using the `data.weight.quantile([0.25, 0.75])`. 1st quantile `q1` = 58.300134985835484 and 3rd quantile `q3` = 71.529859953. 68817. 
3. Compute the `iqr` using `q3` minus `q1` and get 13.22972496785269. 
4. Find the upper and lower bound by subtracting `q1` from the multiple of 1.5*`iqr` and adding `q3` to the multiple of 1.5*`iqr`, respectively. The output is 38.45554753405645 and 91.37444740546721. Basically, I only need the lower bound to find the outlier because from the scatterplot I found that the outlier's weight fell below 25. 
5. From the scatterplot I knew that the outlier aged between 25 and 50. Thus I locate a group of population in this age group using the following code:
```
data_outlier = data[data["age"] >= 25]
data_outlier = data_outlier[data_outlier["age"] <= 50]
```
Finally, locate the person who weighed beneath the lower bound in this group of population given the condition `data_outlier["weight"] < lower_bound` 

I got the result "Anthony Freeman".


## Exercise 3
<br/>

### Data 

Historical data for COVID-19 cases by state from The New York Times's GitHub (<'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'>). 

I import the data and stored it as `covid_data`. I downloaded the data on 9/8/2021. 

### Code Instructions and Answers

Step 1: Import pacakges
```
import pandas as pd
import plotnine as p9
```

Step 2: Standardize the datetime by using `pd.to_datetime(covid_data["date"])` and examined the data:

![covid_data(head)](https://github.com/kristalz/BIS634/blob/main/Images/covid_data(head).png)

Step 3: Make a function `plot_state_by_cases` that takes state names `state_list` as the parameter and plots their cases vs date using overlaid line graphs, one for each selected state.
1. Create a sublist that includes the data of my test state_list inside the function: 

`test_covid_data = covid_data[covid_data["state"].isin(state_list[:])]`

2. Graph the test_covid_data

```

    graph = (
            p9.ggplot(test_covid_data, p9.aes("date", "cases", color="state")) +
            p9.geom_line() +
            p9.scale_y_continuous(trans='log10') +
            p9.theme(axis_text_x=p9.element_text(angle=20))
    )
    graph.draw()

```

Step 4： Test the function `plot_state_by_cases` using the following examples:

1. "New Jersey", "Connecticut", "New York" -- three states in the East Coast

![plot_cases_by_state_test1](https://github.com/kristalz/BIS634/blob/main/Images/plot_cases_by_state_test1.png)

2. "Washington", "Nevada", "California" -- three states in the West Coast

![plot_cases_by_state_test2](https://github.com/kristalz/BIS634/blob/main/Images/plot_cases_by_state_test2.png)

3. "Ohio", "Minnesota", "Illinois" -- three states in the Middle West

![plot_cases_by_state_test3](https://github.com/kristalz/BIS634/blob/main/Images/plot_cases_by_state_test3.png)

Step 5：Make a function `find_date_highest_new_cases` that takes a name of state `test_state` as parameter and returns the date of its highest number of new cases.

1. Import package `numpy` for making arrays in the function, because arrays are easier to access.
2. Make two arrays `test_cases` and `test_dates`. 
3. Store the difference in cases (i.e., new cases) up to current date between one date `[1]` and the date before `[0]` as `previous_cases_difference`. 
4. Compare `previous_cases_difference` with the up-to-date new cases by using a for loop. If the up-to-date new cases are larger than the new cases occurred previously, override the `current_cases_difference` over  `previous_cases_difference`. 
5. Return the date when up-to-date new cases (i.e., `current_cases_difference`) occur. 

Step 6: Test the function `find_date_highest_new_cases`
```
print(find_date_highest_new_cases("New York")) 
# 2021-03-24 00:00:00

print(find_date_highest_new_cases("Connecticut")) 
# 2020-12-28 00:00:00

print(find_date_highest_new_cases("New Jersey")) 
# 2021-01-04 00:00:00
```

Step 7: Make a function `find_difference_in_days` that takes a list of two states `states` as parameter and reports which one had its highest number of cases first and how many days separate that one's peak from the other one's peak.

1. Store the name of the two states separately: `state1` and `state2`. 
2. Find the date when each state has their highest number of cases by using the previous function `find_date_highest_new_cases` and store in `date1` and `date2`, respectively. 
3. Subtract the difference between the two dates. 
4. Find out which state has the highest cases first: If the days_differences are positive, the second state has the highest cases first; othewise the first state has the highest cases first. For each scenario, print out the days differences between them. The last scenario is that two states have the highest cases on the same date. 

Step 8: Test the above funciton using the following examples:

```
states_1 = ["Washington", "Connecticut"]
print(find_difference_in_days(states_1))

# Washington has its highest number of cases on 2021-09-07 00:00:00

# Connecticut has its highest number of cases on 2020-12-28 00:00:00

# Connecticut has its highest number of cases first. 
# Washington and Connecticut have 253 between them.


states_2 = ["New York", "Connecticut"]
print(find_difference_in_days(states_2))

# New York has its highest number of cases on 2021-03-24 00:00:00

# Connecticut has its highest number of cases on 2020-12-28 00:00:00

# New York has its highest number of cases first. 
# New York and Connecticut have 86 between them.

states_3 = ["New Jersey", "Connecticut"]
print(find_difference_in_days(states_3))

# New Jersey has its highest number of cases on 2021-01-04 00:00:00

# Connecticut has its highest number of cases on 2020-12-28 00:00:00

# New Jersey has its highest number of cases first. 
# New Jersey and Connecticut have 7 between them.
```

## Exercise 4

### 4a. 
Make a function `simulate_drug_use` that takes a population size n and a number of drug users d and returns a list of size n with d True values and n - d False values. The Trues represent drug users, the Falses represent non-drug users. 

Step 1: Import `random` package 

Step 2: Make a list of `drug_users` that include all the true drug users in range of `d`.

Step 3: Make a list of `non_drug_users` that include all the non-drug users in range of `n-d`. 

Step 4: Combine the two lists above together and store as `drug_users`. 

Step 5: Use the function `shuffle` in `random` to return a random list of `True` and `False`. 

```
def simulate_drug_use(n, d):

    # n = population size
    # d = number of true drug users in the population 

    drug_users = [True for n in range(d)] 
    non_drug_users = [False for n in range(n - d)]
    drug_users = drug_users + non_drug_users
    random.shuffle(drug_users)
    return drug_users
```

Step 6: Test the function 

```
print(simulate_drug_use(100, 50))
[True, True, False, False, True, True, True, False, True, False, False, False, False, False, False, True, False, False, True, True, False, True, False, True, False, False, False, False, False, False, True, True, True, False, True, True, False, False, True, False, True, False, False, False, False, True, True, True, False, False, True, False, True, False, False, True, False, True, True, False, True, True, True, False, True, False, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, True, True, True, True, True, True, True, False, True, False, True, True, False, True, True, False, False, False]
```

### 4b. 
Make a function `simulate_sample_response` that takes population size n, number of true drug users in the population d, and sample size n as parameters, and returns that sample's responses to the protocol of `True` and `False`. 

Step 1:  Make a list of drug use in population using the function created in 4a and store as `drug_use_response`.

Step 2: Make a list of random sample from the list `drug_use_response` and store as `sample`. 

Step 3: For the sample in the sample list: If they flip "heads", return a random list of `True` or `False` with 50% probability of each. If they flip "tails", return the original sample that represents the true answers for drug ues. 

```
def simulate_sample_response(n, d, s):
    
    # n = population size
    # d = number of true drug users in the population 
    # s = sample size
    
    drug_use_response = simulate_drug_use(n, d) # List of drug use in populaiton 
    sample = random.sample(drug_use_response, s) # Randomly select a list of drug use in sample of 50 


    for s in range(0, len(sample)): 
        s = random.randint(0, 1)  
        heads = 0
        tails = 0
        if (s == 0):
            return random.choices([True,False], weights=(50, 50), k=len(sample))
        else:
            return sample
```

Step 4: Test the funcion
```
print(simulate_sample_response(1000, 100, 50))
[True, True, False, True, True, True, False, True, False, True, True, True, False, False, False, True, False, True, True, True, True, True, False, False, False, False, True, False, False, True, False, False, False, True, True, False, False, False, False, False, True, True, True, True, False, False, False, True, False, False]
```

### 4c. 

Make a function that takes parameters for the total population, the true number of drug users in the population, the sample size, and returns the estimated number of drug users in the population that would be predicted using such a sample and the randomized response protocol.

Step 1: Simulate the sample using the function made in 4b and store as sample.

Step 2: Count the number of `True` that represent the `espected_drug_users`. Then return the rate of the drug users over the total sample size as `espected_drug_users_rate`. 

Step 3: Use the rate calculated in Step 2 to estimate the proportion `p` of drug users in the total population. 

```
def predict_drug_user_fraction(n, d, s):

    # n = population size
    # d = number of true drug users in the population 
    # s = sample size

    sample = simulate_sample_response(n, d, s)
    espected_drug_users = sample.count(True)
    espected_drug_users_rate = espected_drug_users/s

    fraction_estimated_drug_users = (espected_drug_users_rate - 0.25)/0.5
    return fraction_estimated_drug_users
```

### 4d. 

Display an example for above function using n = 1000, d = 100, and s = 50:

```
fraction_estimated_drug_users = predict_drug_user_fraction(1000, 100, 50)
print(fraction_estimated_drug_users)
# 0.54

estimated_drug_users = fraction_estimated_drug_users*1000
print(estimated_drug_users)
# 540
```

### 4e. 

I used 1000 trials to test the function in 4c when my population is 1000, because the trials I want to test should be at least cover the total population.

I imported matplotlib tho plot the histogram of the test results: 

![4e_plot](https://github.com/kristalz/BIS634/blob/main/Images/4e_plot.png)

### 4f. 
Repeat the steps in 4d and 4e for n = 100000, d = 10000, and s = 5000:

```
fraction_estimated_drug_users = predict_drug_user_fraction(100000, 10000, 5000)
print(fraction_estimated_drug_users)
# -0.4908

estimated_drug_users = fraction_estimated_drug_users*100000
print(estimated_drug_users)
# -49080.0
```

I used 100 trials to test the function due to limited memory storage to test the large number of population. 

![4f_plot](https://github.com/kristalz/BIS634/blob/main/Images/4f_plot.png)

My result fell in the two extreme cases by in this example comparing to result using n = 1000, d = 100, and s = 50 in 4f, in which the trails of drug users are spread out in a wider range of number. The plot returned 50 trials with negative drug-users (i.e., no drug users) and 50 trials with more than 4,000 drug users. I think this extreme case might be due to the trial numbers I chose: There might be not enough trials to test all the population (n = 100000). 

### 4g. 
Repeat the steps in 4d and 4e for n = 1000, d = 500, and s = 50:

```
fraction_estimated_drug_users = predict_drug_user_fraction(1000, 500, 50)
print(fraction_estimated_drug_users)
# Output: 0.38

estimated_drug_users = fraction_estimated_drug_users*1000
print(estimated_drug_users)
# Output: 380
```
I used 1000 trials for the same reason described in 4e. 

![4g_plot](https://github.com/kristalz/BIS634/blob/main/Images/4g_plot.png)

My result this time was more distributed comparing to the results in 4e and 4f. Most trials returned around 500 drug users and no trials returned negative drug users. This could mean that the number of trials I selected was enough to cover all the tested population. 
