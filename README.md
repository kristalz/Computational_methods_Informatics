# Assignment 5

Author: Kristal Zhou

Date: 12/3/2021

## Exercise 1 
<br/>

### Data
<br/>

Average incidence rates of cancer report by state from 2014 to 2018: https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=00&areatype=state&cancer=001&race=00&sex=0&age=001&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=default&output=0#results  from the National Cancer Institute. 

Original citations of data sources: 

1 Source: National Program of Cancer Registries and Surveillance, Epidemiology, and End Results SEER*Stat Database (2001-2018) - United States Department of Health and Human Services, Centers for Disease Control and Prevention and National Cancer Institute. Based on the 2020 submission.

5 Source: National Program of Cancer Registries and Surveillance, Epidemiology, and End Results SEER*Stat Database (2001-2018) - United States Department of Health and Human Services, Centers for Disease Control and Prevention and National Cancer Institute. Based on the 2020 submission.

6 Source: National Program of Cancer Registries SEER*Stat Database (2001-2018) - United States Department of Health and Human Services, Centers for Disease Control and Prevention (based on the 2020 submission).

7 Source: SEER November 2020 submission.

8 Source: Incidence data provided by the SEER Program. AAPCs are calculated by the Joinpoint Regression Program and are based on APCs. Data are age-adjusted to the 2000 US standard population (19 age groups: <1, 1-4, 5-9, ... , 80-84,85+). Rates are for invasive cancer only (except for bladder cancer which is invasive and in situ) or unless otherwise specified. Population counts for denominators are based on Census populations as modifed by NCI. The 1969-2018 US Population Data File is used with SEER November 2020 data.

### Code Instructions and answers
<br/>

Packages requirement:

```
import pandas as pd
import json
from flask import Flask, render_template, request, jsonify
import plotly
import plotly.express as px
```

#### Data Cleaning

Step 1: Download the use pandas to open the csv file. Skip the first 8 rows of the csv file that is not part of the table. 

Step 2: Examine the data and standardize missing values: There are a variety forms of missing values:`'***','N/A ',' N/A ',' N/A','*'`. Replace all of them into `NAN`. 

Step 3: Remove the lines that are not inside the table. From the table, I know the last state/territory is Puerto Rico. First, I found that the index of Puerto Rico is 52. Then, I dropped all the rows below that index row by subtracting 53 from 74 using `.tail(74-53).index`. (I knew there were total 74 rows after examining the data. I subtracted 53 because the index begins from 0.)

Step 4: Remove the reference numbers in the state column. Since the reference number in parentheses are in the last three indexes in the string of state + reference number (e.g.,"Connecticut(7)"), I applied a for loop in the data set to replace the old string with a new string that will not have the last three indexes: `data['State'][i] = data['State'][i][0:-3]`. 

Step 5: Export the cleaned data to a csv file using `.to_csv`. 
The file can be accessed through here: https://github.com/kristalz/BIS634/blob/main/Scripts/HW5/cancer_profiles.csv

### Use Flask to implement a server that provides three routes inside a server file (server.py)

#### File Structure

![flask_dir](https://github.com/kristalz/BIS634/blob/main/Images/HW5/flask_dir.jpg)

Step 1: Create the Flask application object using `app = Flask(__name__)`, which contains data about the application and also methods that tell the application to do certain actions. 

Step 2: Create the first route -- `"/"`the index page by returning the index html file using the function `render_template`. 

1. Inside the `index.html` file, I included a `body` part that has a heading `<h1>` and a paragraph `<p>` that prompts a user to enter a state. 

2. I created a `<form>` element that allows a user to input text and return to another route `/info` that contains the information about the state. Specifically, the information will be returned by a "GET" method. I turned off the `autocompletion` of the text using the `autocomplete="off"`; used the `autofocus name = "state"` attribute to let the route automatically get focus when the page loads; and added a `placeholder="State"` attribute to prompt the user to type a specific state. Then I used a button `<input type="submit">` to submit form data to a form-handler, which processes the input data. I named the button as "Find". 

![Flask1](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask1.jpg)


3. I added some stylistic elements in the index page. I created a `main.css` file that stored inside the `css` folder under the `static` folder. Inside the css file, I added a background colour, and set the margins, font, size and colour of the heading text `<h1>` and the paragraph text `<p>`. Then, I edited my index html file to include the CSS file using the line of code `<link rel="stylesheet" href='/static/css/main.css'/>`. 

4. I also added an map image that displays distribution of cancer in United States in the index page by using `<img src="{{url_for('static', filename='StateCancerProfilesMap.png')}}"width=1200>`. 

Step 3: Create the second route -- `"/state/<string:name>"` that returns JSON-encoded data containing the name of the state and the age-adjusted incidence rate (cases per 100k). I created a function that passed the name of a state as string and used pandas to find the incidence rate for that state: `df[df["State"] == name]["Age-Adjusted Incidence Rate([rate note]) - cases per 100,000"])`. The name of the state and the incidece rates were stored in a json dictionary named "result." The function will return the "result" as the user pass a state inside `/<string:name>`. 

Please see an example of Connecticut: 

![Flask_json](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask_json.jpg)

Step 4: Create the third route -- `"/info", methods=["GET"]` that takes the name of the state as a GET argument and return either same information as the API above if the state name is valid or an error page if the state name is invalid. 

1. I used a function `request.args.get` to get the information inside the csv file. If the user enter an invcalid state name, for example, if the state name is misspelled, it will return an error page stated that "Please enter a valid state." Please see example of error page below by not mispelling "Connecticut": 

![Flask_error](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask_error.jpg)

2. However, capitalization of input will not lead to errors. Inside the server file, I converted all the states in the csv file to lower case in stored in a list `states_lower`. I stated that "if state.lower() not in states_lower," the error statement will display in an error page. Thus, I also created an error page that incudes a heading "Error...", the error statement, and a button "back" that allows the user to return to the homepage /. 

3. When the user enter a valid state name regardless lower or upper cases, e.g., "New York", "new york", "New york", an info page will be returned and display the name of state and the incidece rate of that state. I created an info html file that includes the information for this page. There is also a button that promts the user to return to the homepage. 
Here are some examples of "New York", "new york", "New york":

![Flask2](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask2.jpg)

![Flask3](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask3.jpg)

![Flask4](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask4.jpg)

In both error and info html, I applied another css style sheet that set the font and color of the headings. 

4. Additionally, I created a new route -- `"/plot"` that returns an interactive bar chart using the `plotly` module. The bar chart takes the states as x-axis and cases per 100k for each state as y-axis. In order to display the interactive plotly graph in Flask, I first converted the graph into a JSON variable using this line of code: `graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)`. 

In order to show the graph, I needed to add the plotly and jQuery libraries: 

```
<script src='https://cdn.plot.ly/plotly-latest.min.js'></script>
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
```

I used below code was used for plotting a graph to parse the "graphJSON" variable using the following code: (Reference: https://python.plainenglish.io/create-a-simple-covid-19-dashboard-with-flask-plotly-altair-chart-js-and-adminlte-a92ef86a3ca8.)

```
<div id="chart" class="chart">
<script type='text/javascript'>
    var graphs = {{graphJSON | safe}};
    Plotly.plot('chart',graphs,{});
</script>
```

The div element is the Plotly chart container. Inside the `<script>` tag I have a "graph" variable that contains the JSON object from the plotting function inside the `"/plot"` route. The parameter "safe" allows the "graphJSON" rendered correctly. Otherwise, the chart won't be shown. After that, Plotly.plot is a Plotly function that executes the graph object and displays it into the div element which has "chart" id.

The user can hover over any column in the bar chart to visualize the incidence rates for each state. For example in the screenshot below, the bar chart displayed cases in Minnesota. 

![Flask_plot](https://github.com/kristalz/BIS634/blob/main/Images/HW5/Flask_plot.jpg)

The user can return to the home page using the "Back" button below the chart. 


## Exercise 2
<br/>

### Code Instructions and answers
<br/>

Packages requirement:

```
import random
import time
import matplotlib.pyplot as plt
import numpy as np
```
Step 1: Create root with a left and right branch. The parameter value is set to "None" because there is only one variable to be inserted later. 

Step 2: Provide an add method that inserts a single numeric value at a time. The add method compares the value of the node to the parent node and decides to add it as a left node or a right node. The value is added to the left side if it is smaller than the parent node, and to the right side if it is larger. Reference: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm. 

Step 3: Provide a __contains__ method that allows the tree to work like built-in data types. This method searches for an item in only one side of the tree. The method will only search for the left branch if a value that needed to be found is smaller than the parent node, and search for the right branch if the value is larger. Othervise, the method will return 'False" when the value is not in the tree. 

Step 4: Construct the tree that contains the sequence "[55, 62, 37, 49, 71, 14, 17]" using the add method in a for loop. 

Step 5: Test if 55 or 42 is in the my_tree. I confirmed that "my_tree.__contains__(55) = True" and "my_tree.__contains__(42) = False". 

Step 6: Create a `timeit` function that used various sizes n of trees ([1,10,100,1000,1e4,1e5,1e6]) populated with random integers in each call to in with 1000 attempts. For each size n of tree, the function will find 10 numbers in a sequence I generated and time the average execution time of finding those numbers. I returned the minimum execution time out of 1000 attempts and demonstrated the execution time of in on a log-log plot. From the graph below, we could see that the run time required for checking if a number is in the tree increased sharply from n = 10 to n = 1000, and slightly declined from n = 1000 to n = 1e4. After that, the curve of execution time was almost horizontal and in O(log n) times. 

![plot1](https://github.com/kristalz/BIS634/blob/main/Images/HW5/plot1.png)

Step 7: Create another `timeit` function that used various sizes n of trees ([1,10,100,1000,1e4,1e5]) populated with random integers in each call to in with 100 attempts. Again, the function will return the minimum execution time out of 100 attempts. I demonstrate the execution time of setting up the tree on a log-log plot and compared it with a linear and quadratic curve. I took the scale of the actual setup execution time at 0 and multiplied that in both linear and quadratic graph, thus allowing the three curves on the same scale in the plot. From the plot below, we could see that the curve of setup time (O(n log n)) lied between the linear (O(n)) and quadratic curves (O(n**2)). 

![plot2](https://github.com/kristalz/BIS634/blob/main/Images/HW5/plot2.png)


## Exercise 3
<br/>

### Code Instructions and answers
<br/>

Packages requirement:

```
import pandas as pd
from sklearn import decomposition
import plotnine as p9
import numpy as np
from sklearn.model_selection import KFold
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
```

Examine the rice dataset after normalization and decomposition

1. Use pandas's `read_excel` function to load the rice data set. 
2. Normalize the seven quantitative columns to a mean of 0 and standard deviation 1 using the function `(x-x.mean())/ x.std()`.
```
data.iloc[:,0:-1] = data.iloc[:,0:-1].apply(lambda x: (x-x.mean())/ x.std(), axis=0)
```
3. Separate out the seven quantitative features and classes of rice in the dataset.
4. Reduce the data to two dimensions using PCA with the sklearn's `decomposition` module. 
```
pca = decomposition.PCA(n_components=2)
data_reduced = pca.fit_transform(data[my_cols])
pc0 = data_reduced[:, 0]
pc1 = data_reduced[:, 1]
```
5. Plot a scatterplot of pc0 and pc1, color-coding by type of rice.

![pcs_plot](https://github.com/kristalz/BIS634/blob/main/Images/HW5/pcs_plot.png)

From the plot above we could see that there were a large overlapping area of "Cammeo"(red points) and "Osmancik"(blue points) from about -1.5 to 1.5 on the PC0 axis. This will be concerning when implementing k-nearest neighbors due to the following reason:
Ideally we will hope to separate the two clusters of points as much as possible to classify for those points. However, it is difficult to classify the points in the overlapping area corretly since they can possibly be assigned to either category given k nearest neighbors surrounding those points. 

Implement a two-dimensional k-nearest neighbors classifier given the rice data

Step 1: Create a quad tree node class `QTNode` and its attributes 

Attributes: 

`ntype`: The node type. Return 0 if the node of the quad tree is not a leaf node and 1 if it is a leaf node. 

`coord`: The (x,y) coordinate of a given point.

`cls`: The classification of a given point in the dataset.

`nodecount`: The numbers of nodes in the tree.

`xmin`, `xmax`, `ymin`, `ymax`: The bounds of a branch represented by the minimum and maximum values in x and y axes. 

`xmid`, `ymid`: The middle points in x and y axes. 

`BRll`, `BRlh`, `BRhl`, `BRhh`: The four branches of a node. The branch can be also interpreted as a quadrant in a two dimension space.

`BRpr`: The parent branch of the node that has the four branches.

Step 2: Create a quad tree class `QTree` and its attributes and methods

1. Attribute: 

`root`: Use class `QTNode` to store the minimum and maximum values in x and y axises as the root node.

2. Methods:

`addnode(self,node,data)`: Add the points from the data set to tree nodes. 

- If the data set has no values, return none. 

- If the data set has only one value, there is only one node and thus a leaf node. The node x,y coordinates `coord` is a list that combines "PC0" and "PC1" in the data set, and classfication `cls` is the cooresponding type of rice. And the number of nodes is the size of the data. 

- If the data set has more than one values, those values will be added to the nodes in the quad tree. Therefore, I will divided the tree by the median of points to avoid uneven distribution of space. The median values of "PC0" and "PC1" in the dataset are stored as `xmid` and `ymid`, respectively. 

Four branches `BRll`, `BRlh`, `BRhl`, `BRhh` will be add to each node until all the points are added: 
- The first branch `BRll` takes the minimum and median vectors in x and y axes as bounds. Vectors in "PC0" and "PC1" that are smaller than the middle vecotrs will be added in this branch. 
- The second branch `BRlh` takes the minimum and median vectors in x axis, median and maximum vectors in y axis as bounds. Vectors in "PC0" that are smaller than the middle vectors and in "PC1" that are larger than the middle vectors will be added in this branch. 
- The third branch `BRhl` takes the median and maximum vectors in x axis, minimum and median vectors in y axis as bounds. Vectors in "PC0" that are larger than and equal to the middle vectors and in "PC1" that are smaller than the middle vectors will be added in this branch. 
- The last branch `BRhh` takes the median and maximum vectors in x axis, median and maximum vectors in y axis as bounds. Vectors in "PC0" and "PC1" that are larger than and equal to the middle vectors will be added in this branch. 

![quad_subdivided](https://github.com/kristalz/BIS634/blob/main/Images/HW5/quad_subdivided.jpg)

`dist(self,p1,p2)`: Calcuate the distances between two points using the euclidean metric: `((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5`. ([0] and [1] represents x and y coordinate of a point1 and point2). 

`naive_getneighbors(self,coord,k)`: This is a naive implementation of k-nearest neighbors to search for all the points in the quad tree and return the closest points. This function takes the (x,y) coordinate `coord` and k neighbors as parameters. 

- Initialize a heap queue `neighbors` to store points with the closest distances. 
- Initialize a stack that stores the root node of the quad tree.
- While inside the stack, take the topmost value of the stack as a target node. If this target node is leaf node, calculate the distance between the target node and a new added node using their (x,y) coordinates. 
- Store the distance calculated above in a (distance, target node) tuples using `heappush` function of heap queue data structure. (Reference: https://codingdict.com/sources/py/heapq/7330.html). Since heap quque would sort on the first element that has the smallest value, I reversed the order of the distance to place the largest distance as the first element inside the `neighbors` heap queue.
- If the size of heap queue exceeds the k neighbors I can store, pop out the first element in the `neighbors` heap queue (the point with the largest distance) using `heappop`. This will completes searching closest points in all the leaf nodes. 
- If the target node is not a leaf node, continue searching in the four children branches of the target node and repeat the steps above. 

```
neighbors=[]
stack=[self.root]
while stack:
    t=stack.pop(0) 
    if t.leaf: 
        dist=self.dist(t.coord,coord) 
        heapq.heappush(neighbors,(-dist,t)) 
        if len(neighbors)>k: 
            heapq.heappop(neighbors) 
        else:
            for child in [t.BRll,t.BRlh,t.BRhl,t.BRhh]: 
                if child:
                    stack.append(child)                     
    return neighbors
```
In order to avoid searching for all the points in the quad tree, I needed two additional methods to help me implement (`searchnode` and `inrange`). 

`searchnode(self,coord,k=1)`: This method searches for the points of interest in subdivision of quad tree recursively. 
- Initialize the target node `target` from the root of the quad tree and a node `last` beging searched so far. 
- At most, one child branch will be a candidate. While the target node is not a leaf node, return the target node if its corresponding does not have enough points. 

```
while target and not target.leaf:
    if target.nodecount<=k:
        return target
```
- Otherwise, search for points in other four branches based on the comparison between the coordinate of points `coord` and the bounds of the target node. As mensioned earlier, the four branches (`BRll`, `BRlh`, `BRhl`, `BRhh`) are the four quadrants in a two dimension space that are divided based on median of the points (`xmid` and `ymid`). While searching inside the four branches, the current target node will become the last node being visited(`last`), and the new target node (`target`) will be continued subdivided. 

```
if coord[0]<target.xmid:
    if coord[1]<target.ymid:
        last=target
        target=target.BRll
    else:
        last=target
        target=target.BRlh
    else:
        if coord[1]<target.ymid:
        last=target
        target=target.BRhl
    else:
        last=target
        target=target.BRhh
```

- The function will return either the current or last node being visited. 

`inrange(self,coord,node,dist)`: This function returns true or false depending on if the point is within a distance `dist` of the branch. I used this function only when the there were not enough k nearest neighbors points (points of interest) in my current branch. Thus, I would need to search for other branches that might also have the points within the distance from the either to the point. I would show how I used this method in my next method. 

```
if coord[0]<node.xmin:
    if coord[1]<node.ymin:
            return self.dist(coord,(node.xmin,node.ymin))<=dist
        elif coord[1]>=node.ymax:
            return self.dist(coord,(node.xmin,node.ymax))<=dist
        else:
            return self.dist(coord,(node.xmin,coord[1]))<=dist
    elif coord[0]>=node.xmax:
        if coord[1]<node.ymin:
            return self.dist(coord,(node.xmax,node.ymin))<=dist
        elif coord[1]>=node.ymax:
            return self.dist(coord,(node.xmax,node.ymax))<=dist
        else:
            return self.dist(coord,(node.xmax,coord[1]))<=dist
    else:
        if coord[1]<node.ymin:
            return self.dist(coord,(coord[0],node.ymin))<=dist
        elif coord[1]>=node.ymax:
            return self.dist(coord,(coord[0],node.ymax))<=dist
        else:
            return True
```

`getneighbors(self,coord,k)`: This function is a modified version of the naive searching method `naive_getneighbors(self,coord,k)`. Inside the function I two while loops:
- The first one uses the `searchnode` method to find the nearest points in one branch that would contain the points of interest while avoiding other branches that are further away than the nearest points. The slight difference here is that I took the one branch as target node (`target=self.searchnode(coord,k=k)`) and store in a stack instead of starting from the root in previous naive method. 

```
target=self.searchnode(coord,k=k) 
stack=[target]
while stack:
    t=stack.pop(0) 
    if t.leaf:
        dist=self.dist(t.coord,coord)
        heapq.heappush(neighbors,(-dist,t))
    else:
        for child in [t.BRll,t.BRlh,t.BRhl,t.BRhh]:
        if child:
        stack.append(child)
```

- The second while loop tries seaching points in remaining nearby region by going up a level of branch. If the target node has children branches and when the neighbors heap queue still have empty space (not enough points of interest), I would continue searching points in other branches. To accomplish this, I used the `inrange` method to search any points of interest in the range of distance  between a child branch and a point. Here, the distance is the largest distance in the neighbors heap (`-neighbors[0][0]`). (I took the reverse order of the heap to make sure the first item was the largest distance.) This process will repeat until there are no remaining regions. 

```
stack=[self.root]
while stack:
    t=stack.pop(0)
    if t.leaf:
        dist=self.dist(t.coord,coord)
        heapq.heappush(neighbors,(-dist,t))
        if len(neighbors)>k:
            heapq.heappop(neighbors)
    else:
        for child in [t.BRll,t.BRlh,t.BRhl,t.BRhh]: 
        if child and child!=target and (len(neighbors)<k or self.inrange(coord,child,-neighbors[0][0])):
                        stack.append(child)
```

Step 3: Implement 5-fold cross-validation with both naive and quad tree nearest neighbors algorithms to predict the types of rice in the rice dataset. Provide confusion matrix with k=1 and k=5.

Results： 

- When k=1： 

```
The confusion matrix of quad_tree knn method:
[[1411  195]
 [ 219 1985]]
The confusion matrix of naive knn method:
[[1411  195]
 [ 219 1985]]
```
Accuracy = 89.13%
Sensitivity = 86.56%
Specificity = 91.06%
Precision = 87.86%

![cf_k=1](https://github.com/kristalz/BIS634/blob/main/Images/HW5/cm_k%3D1.png)

- When k=5:
```
The confusion matrix of quad_tree knn method:
[[1459  166]
 [ 171 2014]]
The confusion matrix of naive knn method:
[[1459  166]
 [ 171 2014]]
 ```
Accuracy = 91.15%
Sensitivity = 89.51%
Specificity = 92.39%
Precision = 89.78%

![cf_k=5](https://github.com/kristalz/BIS634/blob/main/Images/HW5/cm_k%3D5.png)

Interpretation:

The results are the same for both quad tree and naive k-nearest neighbors implementation. The overall prediction results were better when k = 5 compared with k = 1. 

When k = 1, the accuracy was 89%, meaning that the predicted and actual classification were the same: 1411 "Cammeo" were correctly classfied as "Cammeo" and 1985 "Osmancik" were correctly classfied as "Osmancik". However, there were 219 entires that should be "Osmancik" but were predicted as "Cammeo" and 195 entires that should be "Cammeo" but were predicted as "Osmancik". Given the two types, the abilities of the model could predict "Cammeo" and "Osmancik" correctly were 87 and 91, respectively. 

When k = 5, the accuracy improved to 91%: 1459 "Cammeo" were correctly classfied as "Cammeo" and 2014 "Osmancik" were correctly classfied as "Osmancik". However, there were 171 entires that should be "Osmancik" but were predicted as "Cammeo" and 166 entires that should be "Cammeo" but were predicted as "Osmancik". Given the two types, the abilities of the model could predict "Cammeo" and "Osmancik" correctly improved to 89.5 and 92, respectively.

We could see that using k=5 model is better because it flatouts noise. It will avoid classifying all the nearest points in the same type. For example, when one point that is in fact "Osmancik" are in a pool of "Cammeo" points, using k=1 might cause the model to predict that "Osmancik" point as "Cammeo". Using k=5 would be helpful to prevent this consequence, especially when we only have two types in the data set. 


## Appendix
Please also refer the scripts for five exercises in the Script/HW4 folder (https://github.com/kristalz/BIS634/tree/main/Scripts/HW5).

### Exercise 1: https://github.com/kristalz/BIS634/blob/main/Scripts/HW5/HW5-Exercise1.ipynb 

![image](https://user-images.githubusercontent.com/90003165/144676325-d180c710-fb5d-4ea5-9782-9bcddd49271f.png)

![image](https://user-images.githubusercontent.com/90003165/144676370-7512f16c-c244-4c70-87e5-1722b0c74a34.png)

![image](https://user-images.githubusercontent.com/90003165/144676410-543746a8-7cf6-43b7-ab2a-ac1f770ef34b.png)

![image](https://user-images.githubusercontent.com/90003165/144676452-85405ed3-5ec1-4cd0-aca3-a872354fe999.png)

![image](https://user-images.githubusercontent.com/90003165/144676492-d72d5e49-2a28-4837-9222-9d7967714029.png)

https://github.com/kristalz/BIS634/tree/main/Scripts/HW5/Exercise1-Flask

Templates: 

Index: 

![image](https://user-images.githubusercontent.com/90003165/144676659-5479a54c-a2cc-4b43-8884-6cc801ef7a72.png)

Info: 

![image](https://user-images.githubusercontent.com/90003165/144676771-a56d9ccf-15bd-4f9a-a090-e13a05684eae.png)

Error:

![image](https://user-images.githubusercontent.com/90003165/144676916-ce73524b-9537-4adb-8b56-de8cd30bbe6f.png)


### Exercise 2: https://github.com/kristalz/BIS634/blob/main/Scripts/HW5/HW5-Exercise2.ipynb
 
### Exercise 3: https://github.com/kristalz/BIS634/blob/main/Scripts/HW5/HW5-Exercise3.ipynb
