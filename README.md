# Assignment 4

Author: Kristal Zhou

Date: 11/16/2021

## Exercise 1 
<br/>

### Code Instructions and answers
<br/>

Packages requirement:

```
import pandas as pd
import numpy as np
import requests
```

Step 1: Test the API to make sure it is working. I passed a=0.4 and b=0.2 to test the API and got 1.294915 as my result. 

Step 2: Before quering the API, I created a 2 variables function to find the local and global minimum. The purpose of doing so was to identify the optimal learning rate gamma, stopping criteria and initial a and b without tested the API multiple times. 

1. Create an error function `f(a,b) = a**2 + b**2`. 
2. Create a derivative function that takes a, b and precision h as parameters. Since I could directly compute the derivative, I would use the definition of derivative `f(x+h) - f(x))/h` to estimate the gradient. In our case of having two values, I used this formula to compute the gradient twice: `(f(a+h,b) - f(a,b))/h` and `(f(a, b+h) - f(a,b))/h)`. 
3. Create a function to find the minima that passes the following parameters: 

`num_iter`: Total numbers of iteration. I set it to 10 just to get a sense of how good the function would find the minima. 

`stopping_threshold`: Decide when to stop finding if the absolute difference in error values between two successive iterations falls below this numeric threshold. I set it to `-1` because this would be an impossible case since absolute value could not be negative. Thus, when the absolute difference reached to 0, the function would stop calculating. 

`f`: The error function

`init_a` and `init_b`: The initial a and b values I guessed. I set them to both 1, a value small enough for running not too many iterations but not too small that would return the result too fast. 

`h`: The precision (the small increment step) in the derivative function. I set it to `1e-4` to ensure a better precision in estimation. 

`gamma_list`: A list of different learning rates. I used `0.05,0.25,0.3,and 0.5` for my learning rates to test the function in different scenarios. I would justify which learning rate I picked later.

4. Assign `a` and `b` variables that store the initial a and b values; and `all_a` and `all_b` variables that store all estimated a and b using gradient descent formula. Also assigne `all_errors` variables that calculate the errors by the error function. Set an initial large difference (1.0e10) between two sucessive iterations. 
5. During the iterations, while the difference is larger than the stopping_threshold, continue computing the gradient descend for a and b, the errors and the absolute difference between two consecutive iterations. 

Step 3: After passing all the parameters, I got the results from four different learning rates. 
1. When gamma = 0.05, I found the minimum a and b were both 0.34864587 and the error was 0.24310789. This would not be the global minimum because by using first derivative, we know that the (0,0) would return the smallest value 0 for `y = a**2 + b**2`. However, it could be a local minimum. 
2. When gamma = 0.25, I found the minimum a and b were both 4.48360754e-05 and error was 4.02054732e-09. These three values were close enough to 0. I noticed that the function generated more than 10 iterations because the difference between two successitive did not reach to stopping threshold yet. 
3. When gamma = 0.3 or 0.5, the minimum a and b were converged to -4.99642935e-05 and -5.000000e-05, respecitive. The errors were converged to 4.99286126e-09 and 5.00000000e-09, respectively. However, using those two gammas in fact overshooted the estimation because the learning rates were too fast. Thus, if I want to use these two gammas, I would want to consider raising my initial guess valules for a and b. 

Step 4: Based on the scenario above, if I want to run a small number of trials using the API, I would pick `0.25` as my learning rate gamma to avoid over-shooting or over-dampening. I decided to double my number of iterations since I have no clue for the query function and not knowing how many minima there would be, I wanted slightly more trials to find the minima. 

I choosed a = 0.3 and b = 0.7 as my initial guesses. From my results, I saw that the minimum in this query was 1.100000. The errors converged to 1.100000 after 7 trials, even though a and b were still changing slightly afterwards. However, I was not sure if I found my global minimum or not. I might be stucked at my local minimum atfter 7 iteration. Thus, this should be my true local minimum 1.100000 where a = 0.216607 and b = 0.689036. 

![error_result_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/Error_result_1.jpg)

Naively, I wanted to guess other values to find if there were value smaller than 1.100000. This time, I chosed a = 0.9 and b = 0.1 as my initial guesses. From my results, I saw that the minimum in this query was 1.000000, where a = 0.711950 and b = 0.168950. The function converged when after 11 iterations. This would be my global minimum.  

![error_result_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/Error_results_2.jpg)

## Exercise 2
<br/>

### Code Instructions and answers
<br/>

Packages requirement:

```
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import random
import numpy as np
from math import radians, cos, sin, asin, sqrt
```

Data:

World city data set "worldcities.csv"(https://simplemaps.com/data/world-cities) licensed CC BY 4.0.

Step 1: Examine the data set using `head()`function. 

![HW4_Exercise2_data](https://github.com/kristalz/BIS634/blob/main/Images/HW4/HW4_Exercise2_data.jpg)

Step 2: Define Python Haversine function that calculates the distance between 2 global position system points (reference: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points). 

Step 3: Create a list that stores the lonitude and latitude for each city in the data set. 

Step 4: Implement the Lloyd's algorithm for k-means to examine the distribution of cities. 
1. Generate a pseudo-random sample of k points from the data set, which are considered the seeds for forming k clusters. 
2. Initiate two empty lists that store the old and new assigned cluster for each cities. 
3. Generate an iteration that assigns each data point to a cluster based on the nearest seeds (the centers) and use the centers of each cluster as the seeds to assign next clusters of points. 
4. Determine the distance between each cities and the nearest centers using the Haversine function in step 3.
5. Repeat 3-4 until convergence. 

Step 5: Map the k clusters of cities on a Robinson map. 
1. Defind the map by passing arguments of `projection = 'robin`; `lat_0 = 0` and `lon_0 = -100` for central latitude and longitude of projection; and use `resolution = 'c'`for crude resolution coastlines.
2. Use `drawmapboundary.()` to fill the basemap with aqua color. 
3. Extract the`longitudes`, `latitudes` and `cluster` from the data set into three separate lists.
4. Convert the longitudes and latitudes to the map projection coordinates `xpts` and `ypts`.
5. Use a scatter plot to map `xpts` and `ypts` based on the cluster into different colors. 

I selected the first, two intermediate and the final plots for k = 5 clusters. 

![k5_first](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k5_first.jpg)

From the first plot, we could see that cities in Eurasia had had the most numbers of divisions. Specifically, the right portion of Eurasia and Australia &Oceania was color coded in light blue. We could also notice that the majority of cities in Africa was in light blue as well.

![k5_interm1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k5_interm1.jpg)

In this plot, however, Eurasia was divided into two clusters, probably one for Europe and the other for Asia. However, Asian cities in the left side was in different cluster. We could also see that the right half of Eurasia and Africa were in the same cluster.

![k5_interm2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k5_interm2.jpg)

Here was another example intermediate plot. This time, Eurasia was basically color-coded in one cluster except some disperse cities in the right bottom corner. We could see that left top corner of Africa were in the same color as Europe.

![k5_final](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k5_final.jpg)

Finally, we could clearly distinguish cities in Europe and Africa in this last plot, inwhich we had the convergence. Notice that there were few outliers in Africa color coded as the same as North American. Two important things we learnt from using k = 5: 1) Asia cities that are not next to Europe and Australia & Oceania had the same colors in the entire iteration; 2) Cities in Eurasia were eventually convered in one cluster likely due to proximity. 

I selected the first, four intermediate and the final plots for k = 7 clusters. 

![k7_first](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k7_first.jpg)

From the first plot, we noticed that the Eurasia again had the most divisions. Some cities in the Eurasia, Africa and South America were assigned in the same cluster. We could also see that a small portion of Europe in the left botton corner were assigned in a cluster as its own. 

![k7_interm1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k7_interm1.jpg)

In these two example intermediate plots, we noticed that the size of that small cluster of cities in Europe expanded to the left top corner of Africa. This time we could see a sharp division between cities in Europe and Asia in Eurasia. More cities in Asia were assigned to a different cluster from the neighbor European cities. 

![k7_interm2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k7_interm2.jpg)

These two plots show better division of cities between Europe and Asia. Nevertheless, Aisan cities on the left and right sides of the plot were still color coded differently. 

![k7_final](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k7_final.jpg)

The final plot was not too different from the two intermediate plots above. Notice that cities in the left bottom corner of Europe and the top upper corner of Afica were still in same colors. The right protion of Asia (in the left side of the plot) and Austria&Oceania were still in the same cluster (both in yellow), although the size of which clearly shrinked compared to that when using k = 5. 

I selected the first, two intermediate and the final plots for k = 15 clusters.

![k15_first](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k15_first.jpg)

Cities in all continents were divided in different clusters. Interestingly, cities in North America were divided in most clusters that did not happen when using k = 5 or 7. Nevetheless cities in North America closet to those in South America were in the same. It was also interesting to see that cities in the right most corner of North America (in yellow) were in the same cluster as those in the middle of Eurasia. 

![k15_interm1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k15_interm1.jpg)

While more cities in the right most corner of North America  were assigned in the same cluster as those in the middle of Eurasia, fewer Asian cities that were close to Australi&Oceania were assigned in the same cluster. 

![k15_interm2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k15_interm2.jpg)

Again, we could see that more cities were colored coded in yellow in Eurasia. Almost all cities in the right poriton of Asia (in the left side of graph) were color coded differently from cities in Australi & Oceania.

![k15_final](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_with_interm/k15_final.jpg)

Notice that divisions of clusters in North and South America did not change significantly in the entire iteration. At the same time, divisions between Asia and Australi & Oceania became more distinct comparing to those hwen using k = 5 or 7. 

I also ran five times for each clusters. 

1. k = 5 plots

![k5_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k5_1.jpg)

![k5_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k5_2.jpg)

![k5_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k5_3.jpg)

![k5_4](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k5_4.jpg)

![k5_5](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k5_5.jpg)

From the five plots above, we could observe a fair variation each time when we assigned different initial centers (the seeds): For example, North and South America were assigned in the same clusters in the first and fourth plots, whereas Eurasia and Africa were assigned in the same clusters in the last plot. that the divisions in continents were quite different each time. We could also see The runtime for the five iterations span from 3.86 to 13.29 seconds, with a median of 6.46 seconds. 

2. k = 7 plots

![k7_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k7_1.jpg)

![k7_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k7_2.jpg)

![k7_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k7_3.jpg)

![k7_4](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k7_4.jpg)

![k7_5](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k7_5.jpg)

While there was a similar sense of variation, we could see a general increase of runtime when k = 7 clusters. The runtime for 7 clusters ranged from 5.10 to 19.33 seconds with a median of 8.72 seconds. 

3. k= 15 plots

![k15_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k15_1.jpg)

![k15_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k15_2.jpg)

![k15_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k15_3.jpg)

![k15_4](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k15_4.jpg)

![k15_5](https://github.com/kristalz/BIS634/blob/main/Images/HW4/k_plots_random_multiple_tests/k15_5.jpg)

Generally, cities in Eurasia were divided in most clusters comparing to those when using k = 5 or 7. Different from k = 5 or 7, we could see more similar clusters assignment in k = 15 (the second and the third plots), although they were in different colors. 

Again, we could observe an increase in runtime ranging form 24.60 to 38.46 seconds with a median of 36.24 seconds. We could see that the ranges of runtime were wider in both 7 and 15 clusters. 

## Exercise 3 
<br/>

### Code Instructions and answers
<br/>

Packages requirement: 
```
import time
import plotnine as p9
import pandas as pd
from tqdm import tqdm
from functools import lru_cache
```

Step 1: Create a function of the original computation fibonacci sequence `r(n)`that passes a parameter of n. The precondition for this function is that n is an interger >=1. If n is equal to 1 or 2, return the result as 1. Otherwise, call the function recursively by adding the results of `n-1` and `n-2`. 

Step 2: Create a timing function that passes the function and 3 timing times. Return the minutes of running range of n subtracting start time from end time. 

Step 3: Plot the runtime of function using plotnine on a log/log graph. I choose a range of n = 40 for this function because it would take a decent amount of time (about 2 mins) to run the function. I would not choose a larger size of n beyond that because the time complexity for fibonacci sequence is O(2^n). Thus, the runtime of the function will scale up rapidly with increasing sizes of n. 

![HW4_Exercise3_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/HW4_Exercise3_1.png)

Step 4: Modified the original function `r(n)` by using the decorator function `lru_cache` to cache the results for each n. Doing so can speed up the function significantly since `lru_cache` uses memoization technique reduces the execution time of the function. This decorator allows us to quickly cache what the function have calculated and continue executing the rest. 

I chose to run this function in a size of n = 1000. I did not use a log y axis to plot the run time because the computer would return all times as exactly 1e-7 in a straight line. Then we could not visualize the changes of runtime from smaller to larger sizes of n. 

![HW4_Exercise3_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/HW4_Exercise3_2.png)

From the plot above, we could see that the only outlier is the runtime for the first n. We could also see that the runtime speed up significantly as the size of n passes 10. The caching information for this function was summarized below. 

```
CacheInfo(hits=3992, misses=999, maxsize=128, currsize=128)
```

The runtime would be all in zero when I used `time.time()` instead of `time.perf_counter()`. 

![HW4_Exercise3_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/HW4_Exercise3_3.png)


## Exercise 4 
<br/>

### Questions: Implement a function that takes two strings and returns an optimal local alignment and score using the Smith-Waterman algorithm; insert "-" as needed to indicate a gap (this is part of the alignment points).
<br/>

####  Code Instructions and answers
<br/>

Packages requirement: 

```
import numpy as np
from enum import IntEnum
```

In this exercise, we will identify optimal local alignment between two different sequences consisted of nucleotides. We will use Smith-Waterman scoring matrix to assign scores for matches and mismatches between two sequences. We also use gap scores to an alignment when we have insertion or deletion from one sequence to another sequence. 

We will identify the maximum score assigned on the last base of the alignment, where we will trace back to identify the entire aligned sequence by checking the three possible previous points (i.e., to the diagonal, the above and the left direction). Finally, we will stop when we reach to the first base of the alignment, where the score will be 0.


Step 1: Assign the default scores match=1, gap_penalty=1, and mismatch_penalty=1. 

Step 2: Create a class object `Trace` using Assign constant numeric values to trace back the aligned sequence. By using `enum.IntEnum()` method, we can enumerate assigned strings based on integer values (reference: https://www.geeksforgeeks.org/enum-intenum-in-python/).
```
STOP = 0
LEFT = 1 
UP = 2
DIAG = 3
```
Since we will trace back the aligned sequence from right lower corner to left upper corner, we will use "LEFT" and "UP" for scores in horizontal and vertical directions. "STOP" means that we reaches the first base of the aligned sequence; "LEFT", "UP" and "DIAG" mean that the maximum score is in the left, the above and the diagonal direction of current location. 

Step 3: Create a Smith-Waterman local alignment algorithm function that pass parameters of two sequences. In this function, we will complete two parts 1) find the maximum score for the alignment and 2) trace back the optimal local alignment. (My function is based on the idea of existing Smith-Waterman algorithm: https://github.com/slavianap/Smith-Waterman-Algorithm/blob/master/Script.py.)

Part 1 Find the maximum score for the alignment:
1. The two sequences will be arranged in a matrix form with sequence1 + 1 rows and sequence2 + 1 columns. 
2. Create two empty matrixes: Matrix M for storing scores and tracing matrix s for to trace back the optimal local alignment. Assign zeros in both matrixes using `numpy.zeros` function. 
3. Initialize variables for the maximum score as `0` and the location in the alignment as `(0,0)`. 
4. Calculate the scores for all cells in matrix M using Smith-Waterman scoring system. Here, we store a variable `match_value` if the previous base in two sequences (the previous diagonal cell) match or mismatch. Then we add this `match_value` to the value of the previous cell and store the new value as a `diagonal_score`. We assign gap_penalty score if there is a gap "-" in sequence 1 or 2. The cell above and to the left will minus the `gap_penalty` score and stored as `up_score` and `left_score`, respectively. Then we will store the highest score for a cell from diagonal_score, up_score, left_score and 0.
5. Trace back where the cell's value is coming from. Here we have four situations: Assign `STOP` and store in the tracing matrix `s` if the score is 0; Assign `LEFT` if the score is the `left_score`, `UP` if the score is the `up_score` and `DIAG` if the score is the `diagonal_score`. 
6. Find the maximum score and the location after looping through all cells in the matrix.

Part 2 Trace back the optimal local alignment: 
1. Initialize variables for tracing the optimal local alignment. We assign `aligned_seq1` and `aligned_seq2` as two empty aligned strings, which are the final result of aligned sequences. We will also assign another two temporary empty aligned sequences 
`current_aligned_seq1` and `current_aligned_seq2` to store the aligned bases after each trace back. 
2. Initialize variables for the row and column index of the location of maximum score as `max_i` and `max_j`, respectively. 
3. Trace the pathway of the alignment: If the cell is assigned `DIAG`, move diagonally of the sequence; If the cell is assigned `UP`, move to the row above and assign a gap `-` in sequence 2; If the cell is assigned `LEFT`, move to left column and assign a gap `-` in sequence 1. 
4. Return a reversed version of aligned sequence 1 and 2 by using `[::-1]` after storing all aligned bases. We will return the maximum score at the end of function as well. 

Step 4: Run three tests for the function created above. I verified my tests results by using the "Freiburg RNA tools" that can return the maximum scores and aligned sequences by assigning match/mismatch/gap scores in two made-up sequences (http://rna.informatik.uni-freiburg.de/Teaching/index.jsp?toolName=Smith-Waterman#). 

1. Test 1: For sequences 'tgcatcgagaccctacgtgac' and 'actagacctagcatcgac', there is one of the possibility with a maximum score of 8:

```
agacccta-cgt-gac
agacc-tagcatcgac
```

Verification: 

![SW_test1_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test1_1.jpg)

![SW_test1_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test1_2.jpg)

![SW_test1_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test1_3.jpg)

Test 2: For sequences 'tggtcgagaactacgtgac' and 'actagacctaccatcggc', there is only one possibility with a maximum score of 6:
```
agaactac
agacctac
```
Verification: 

![SW_test2_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test2_1.jpg)

![SW_test2_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test2_2.jpg)

![SW_test2_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test2_3.jpg)

Test 3: For sequences 'gtctcgagaactacgtgac' and 'agtacacctaccatcggc', there is one of the possibility with a maximum score of 5:
```
agaactacgtgac
agtac-acct-ac
```
Verification: 

![SW_test3_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test3_1.jpg)

![SW_test3_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test3_2.jpg)

![SW_test3_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_test3_3.jpg)

Step 5: Modified the `aligned` function by adding a parameter that passes different gap_penalty score. The other parts of the function remains the same. 

When the gap_penalty is 2: 

Test 1: For sequences 'tgcatcgagaccctacgtgac' and 'actagacctagcatcgac', there is only one possibility with a maximum score of 7:
```
gcatcga
gcatcga
```
Verification: 

![SW_gap2_test1_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test1_1.jpg)

![SW_gap2_test1_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test1_2.jpg)

![SW_gap2_test1_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test1_3.jpg)

Test 2: For sequences 'tggtcgagaactacgtgac' and 'actagacctaccatcggc', there is only one possibility with a maximum score of 6:
```
agaactac
agacctac
```
Verification: 

![SW_gap2_test2_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test2_1.jpg)

![SW_gap2_test2_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test2_2.jpg)

![SW_gap2_test2_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test2_3.jpg)

Test 3: For sequences 'gtctcgagaactacgtgac' and 'agtacacctaccatcggc', there is one of the possibility with a maximum score of 4:
```
ctac
ctac
```
Verification: 

![SW_gap2_test3_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test3_1.jpg)

![SW_gap2_test3_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test3_2.jpg)

![SW_gap2_test3_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap2_test3_3.jpg)

Step 6: Assign the different scores match = 2, mismatch_penalty = 2, gap_penalty = 3

Test: For sequences 'tgcatcgagaccctacgtgac' and 'actagacctagcatcgac', there is only one possibility with a maximum score of 14:
```
gcatcga
gcatcga
```
Verification: 

![SW_gap3_test_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap3_test_1.jpg)

![SW_gap3_test_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap3_test_2.jpg)

![SW_gap3_test_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap3_test_3.jpg)

Step 7: Assign the different scores match = 2, mismatch_penalty = 1, gap_penalty = 4

Test: For sequences 'gtctcgagaactacgtgac' and 'agtacacctaccatcggc', there is only one possibility with a maximum score of 10:
```
agaactac
acacctac
```
Verification: 

![SW_gap4_test_1](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap4_test_1.jpg)

![SW_gap4_test_2](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap4_test_2.jpg)

![SW_gap4_test_3](https://github.com/kristalz/BIS634/blob/main/Images/HW4/SW_tests/SW_gap4_test_3.jpg)


## Appendix
Please also refer the scripts for five exercises in the Script/HW4 folder (https://github.com/kristalz/BIS634/tree/main/Scripts/HW4).

### Exercise 1: https://github.com/kristalz/BIS634/blob/main/Scripts/HW4/HW4-Exercise1.ipynb

![image](https://user-images.githubusercontent.com/90003165/141831067-93d5044a-9183-4226-9113-3c24c7940abe.png)

![image](https://user-images.githubusercontent.com/90003165/141831118-d95c6ce3-3f8e-4b5b-a4c9-d464dd85e2fd.png)

![image](https://user-images.githubusercontent.com/90003165/141831169-ba0c21c0-0756-42d2-9628-2391f1a37861.png)

![image](https://user-images.githubusercontent.com/90003165/141831224-0d1248bc-c9c6-4b97-a8e9-643bd95e52de.png)

![image](https://user-images.githubusercontent.com/90003165/141831311-f4fca221-40c5-4a92-8197-bc2a745bb243.png)

![image](https://user-images.githubusercontent.com/90003165/141831362-2d905051-34e3-4559-9df0-50332bfd25ba.png)

![image](https://user-images.githubusercontent.com/90003165/141831406-baa34af9-62f7-492f-a766-b8f947550339.png)

![image](https://user-images.githubusercontent.com/90003165/141831499-35ffa7a8-d6e0-4f9f-aa95-9d0461f71125.png)

![image](https://user-images.githubusercontent.com/90003165/141831514-dfd1b81e-ac84-44eb-8c90-0edaeb513e2c.png)

![image](https://user-images.githubusercontent.com/90003165/141831568-021477eb-cba4-4366-86c8-ee8eaa7c5fe2.png)

![image](https://user-images.githubusercontent.com/90003165/141831607-1e12e3f9-40bb-49ea-96ba-fac372a5600c.png)

![image](https://user-images.githubusercontent.com/90003165/141831716-46a2ce33-83ca-43e3-909c-4b785001e732.png)

![image](https://user-images.githubusercontent.com/90003165/141831746-78101380-c7e8-4d3c-97fb-2cc47f21a699.png)

![image](https://user-images.githubusercontent.com/90003165/141831779-18c17add-5c41-442f-aa99-fc74b6536e30.png)

### Exercise 2: https://github.com/kristalz/BIS634/blob/main/Scripts/HW4/HW4-Exercise2-final-plots.ipynb

![image](https://user-images.githubusercontent.com/90003165/141832396-9beb5a2c-7d0a-4fad-96fa-808c782ff733.png)

![image](https://user-images.githubusercontent.com/90003165/141832653-f5771f2a-aa47-496d-a7d9-272aa4d1a7e2.png)

![image](https://user-images.githubusercontent.com/90003165/141832710-42be88dc-0c19-4749-8ab0-d98a4936ad51.png)

![image](https://user-images.githubusercontent.com/90003165/141832754-48670177-3a50-4a59-9983-0d12c8936e8c.png)

![image](https://user-images.githubusercontent.com/90003165/141832794-b2440935-05b4-4b9a-ad86-2dee99aaa940.png)

![image](https://user-images.githubusercontent.com/90003165/141832836-cd205cdb-0a2d-4d60-a648-58ac9497259e.png)

![image](https://user-images.githubusercontent.com/90003165/141832874-1da12756-4641-48e4-82b3-657bff267708.png)

![image](https://user-images.githubusercontent.com/90003165/141832900-9e15a177-db9f-49ee-8989-765d0796808f.png)

![image](https://user-images.githubusercontent.com/90003165/141832930-37d68c27-1818-43af-9eb0-68c4e50c510d.png)

![image](https://user-images.githubusercontent.com/90003165/141832959-d713eb91-c673-448b-a432-89ae64fb3b35.png)

![image](https://user-images.githubusercontent.com/90003165/141832985-ca775508-8a33-4307-b464-b615669b478a.png)

![image](https://user-images.githubusercontent.com/90003165/141833018-706f234e-fa7b-4b4f-9900-23f981c4833e.png)

![image](https://user-images.githubusercontent.com/90003165/141833043-594572f7-b12d-4781-8011-3feb6a438318.png)

![image](https://user-images.githubusercontent.com/90003165/141833071-1e59328d-2c84-402b-8f2f-1c54b2292044.png)

![image](https://user-images.githubusercontent.com/90003165/141833106-6877c332-8c78-45d1-be8d-c519188716c0.png)

![image](https://user-images.githubusercontent.com/90003165/141833137-7fb5a927-9bd1-4898-8851-7ac79bd22ddf.png)

![image](https://user-images.githubusercontent.com/90003165/141833162-9bebed8e-8070-465d-b348-c409292c67dc.png)

Please also refer to https://github.com/kristalz/BIS634/blob/main/Scripts/HW4/HW4-Exercise2.ipynb if you would like see the intermediate plots for each cluster. 

### Exercise 3: https://github.com/kristalz/BIS634/blob/main/Scripts/HW4/HW4-Exercise3.ipynb

![image](https://user-images.githubusercontent.com/90003165/141833320-cea4ea20-e61c-496e-9eed-fabbe19b5763.png)

![image](https://user-images.githubusercontent.com/90003165/141833349-26fa02af-7b49-4735-9a4c-536b38be4be9.png)

![image](https://user-images.githubusercontent.com/90003165/141833387-2049b846-0505-497c-bbce-e3377ef4b8a2.png)

![image](https://user-images.githubusercontent.com/90003165/141833417-8b1844f7-3632-494f-8ee8-ae86eae82984.png)

![image](https://user-images.githubusercontent.com/90003165/141833454-d4aa8d16-058c-4562-a611-1db6b0d9c582.png)

![image](https://user-images.githubusercontent.com/90003165/141833502-64c7189c-0131-4c43-ba21-04e4eaf3cf24.png)

### Exercise 4: https://github.com/kristalz/BIS634/blob/main/Scripts/HW4/HW4-Exercise4.ipynb

![image](https://user-images.githubusercontent.com/90003165/141833548-d9ab33fd-7e2e-40cd-a9d2-a798fb242a9a.png)

![image](https://user-images.githubusercontent.com/90003165/141833591-aa329fcd-daab-4c8d-afda-f5e388df3936.png)

![image](https://user-images.githubusercontent.com/90003165/141833625-e0da1842-5099-4bd8-b18f-9b8057f0ec19.png)

![image](https://user-images.githubusercontent.com/90003165/141833678-769d2472-e3b7-4b24-8fa7-09e568579517.png)

![image](https://user-images.githubusercontent.com/90003165/141833717-3f25bb3c-e67e-465e-84a5-d287af0aaca2.png)

![image](https://user-images.githubusercontent.com/90003165/141833764-99f57226-b57b-4479-be8c-0ffd4e16975b.png)

![image](https://user-images.githubusercontent.com/90003165/141833808-380df105-4bc2-4254-883a-8ed72023ba65.png)




