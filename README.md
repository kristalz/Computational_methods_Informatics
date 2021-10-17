# Assignment 3

Author: Kristal Zhou

Date: 10/26/2021

## Exercise 1 
<br/>

### Code Instructions and answers
<br/>

#### Question 1: Use the requests module (or urllib) to use the Entrez API to identify the PubMed IDs for 1000 Alzheimers papers from 2019 and for 1000 cancer papers from 2019. 
<br/>

Packages requirement: 

```
import requests

import xml.dom.minidom as m
```

Step 1: Create a function `get_id` that passes the query `disease` as a parameter to search the PubMed IDs for the articles. 
Inside the function, create a `get` request that passes disease and year 2019 for `term` parameter (`{disease}+AND+2019[pdat]`) and 1000 for `retmax` parameter (the maximum result): https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={disease}+AND+2019[pdat]&retmode=xml&retmax=1000. 
Get all Pubmed ID tags by using `getElementsByTagName("Id")` since xml is structed by element nodes. To get the content inside each "ID" tags, loop through all element nodes and all text nodes inside the element nodes to extract the data (the IDs). Then return the IDs as result. (Reference: https://stackoverflow.com/questions/317413/get-element-value-with-minidom-with-python). 

Step 2: Execute the function by using `if __name__ == "__main__"` to find PubMed IDs for Alzheimers and cancer papers, respectively. 

Answer: The two lists of 1000 PubMed IDs for two diseases are displayed in `HW3-Exercise1` script. 

#### Quetion 2: Use the Entrez API via requests/urllib to pull the metadata for each such paper found above (both cancer and Alzheimers) (and save a JSON file storing each paper's title, abstract, MeSH terms (DescriptorName inside of MeshHeading), and the query that found it that is of the general form. 
<br/>

Packages requirement:

```
import json

import time

from os.path import exists
```

Step 1: Create a function `get_infor` that passes the list of PubMed IDs found above and query of disease as parameters. 
1. Inside the function, create a new file path to save the JSON file. 
2. If the file path exits, open the file with `append` mode `a` to add the metadata for each paper. (Reference:https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist and https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function). If the file does not exist, use the `write` mode `w` to create a new file for adding the metadata. 
3. Create a dictionary that store the article ID with the article information stored inside a nested dictionary. While looping through all PubMed IDs, create a nested dictionary that stores each article information. Use a `post` request to fetch (i.e.,`efetch` function) the metadata (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id={pmid}). Then parse the xml document using the `parseString` function inside the minidom module. 
4. First extract the article titles. If the title information exists, loop through all element nodes inside the title tag (https://docs.python.org/3/library/xml.dom.minidom.html) and childnodes inside each element node. If the childnodes are text nodes, add the whole text information to title. If not, it is an element node and there might be other nested child nodes. Then, loop through all nested childnodes and check if they are text nodes. If yes, add them to the title.
5. Repeat the step above to extract abstracts and mesh terms. 

While storing the abstracts, I simply concatenating all the abstract parts without specifying the structure of the abstract. This method is easy and generalizable for all embedding nodes inside the abstract including the edge cases. For example, some abstracts have italized node. However, since all parts are adding together in one text, we cannot distinguish which article have separate parts in their abstracts because the original structure was missing. 

Different from titles, and abstracts, there might be a list of mesh terms for each article. Need to make an empty mesh terms list first and append all mesh terms into the list. 
6. Save titles, abstracts, query of disease, and mesh terms into the dictionary created for each article. Use `time.sleep(1)` to query one article at a time. Finally, return the dictionary that stroing the metadata for all articles. 

Step 2: Before executing the function, need to first find if there are any overlap in the two sets of article. If yes, need to change the query that applies to both disease (i.e., Alzheimer/Cancer). (This step also refers to the next question in this exercise.)

Find the overlap PubMed Id by intersecting two lists of articles'IDs using the `intersection` function. Answer: There is only one overlap paper. The Pubmed ID is `32501203`. 

Step 3: Run the function created in `Step 1` to store all article information into the dictionary created inside the function. First store the Alzhiemer papers, then update the file with cancer papers. Update the `query` for the overlap paper with `Alzheimer/Cancer`. Use `write` mode `w` to convert the dictionary of all articles' metadata to json file by using the `json.dumps` function. Then, close the file to save memory for run time. 

Answer: Please see the Json file `pubmed_articles.json` under the main branch. 

During my extracting process, I checked my results by searching a couples papers which have some embedded childnodes inside their titles or abstracts. For example, inside the metadata for article  33939349 (<https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=33939349>), there are some embedded nodes such as "sup 1", "sup 2". 

![HW3_Exercise1 example1](https://github.com/kristalz/BIS634/blob/main/Images/HW3_Exercise1%20example1.png)

I checked that I have captured all parts in the abstract.

![HW3_Exercise1 VERIFY1](https://github.com/kristalz/BIS634/blob/main/Images/HW3_Exercise1%20VERIFY1.png)

In another example acticle, similar case also happened when some words are italized.

![HW3_Exercise1 example2](https://github.com/kristalz/BIS634/blob/main/Images/HW3_Exercise1%20example2.png.jpg)

I checked that I have captured those italized words as well.

![HW3_Exercise1 VERIFY2](https://github.com/kristalz/BIS634/blob/main/Images/HW3_Exercise1%20VERIFY2.png.jpg)


## Exercise 2
<br/>

### Code Instructions and answers
<br/>

#### Question 1: What fraction of the Alzheimer's papers have no MeSH terms? (2 points) What fraction of the cancer papers have no MeSH terms? (2 points)
<br/>

Package requirement: 
```
import json
```

Step 1: Open the Json file created in exercise 1 by using `json.load` and store in a `data` dictionary. 
1. Split all articles into separate dictionaries according to the queries (alzheimer, cancer, and alzheimer/caner): `alzheimer_data`, `cancer_data`, and `overlap_data`, by using key and value pair and appling an `if` condition to  `query` to filter the paper. For example, use `if (data["query"] == "Alzheimer") or (data["query"] == "Alzheimer/Cancer")` because the overlap paper also counts as an Alzheimer's paper. This is also true for cancer papers. In this exercise, the key is `pmid` and value is `data` for each article. 
2. Using the key and value pair and an `if` condition to filter both alzheimer and cancer articles without mesh terms.

Answer：The fraction for Alzheimer's papers have no MeSH terms is 164/1000. The fraction of the cancer papers have no MeSH terms is 768/1000. Cancer papers with no mesh terms are almost 5 times as Alzhiemer's papers with no mesh terms (0.768/0.164 = 4.62). This large difference might imply that cancer papers have fewer standardized terms. Because cancer is a more general topic than Alzhiemer's, the vast amount of cancer papers over Alzhimer's might lead to more delays to assign mesh terms. Different from Alzheimer's, cancer covers more than one diseases and thus create more difficulties in assigning standardized terms because there are various types of cancers. 

#### Question 2: What are the 10 most common MeSH terms for the Alzheimer's papers whose metadata you found in Exercise 1? Provide a graphic illustrating their relative frequency. 

Packages requirements:

```
from collections import Iterable
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
```

Step 1: Extract the mesh term lists in alzheimer papers `alzheimer_with_mesh`
1. Filter out the papers have mesh terms and store in a dictionary.
2. Extract the metadata for each paper by using `.values()` function and store in a list `alzheimer_with_mesh_list`.
3. Extract the mesh terms from the list of metadata and store in a list `alzheimer_with_mesh`.

Step 2: Convert a nested 2D  `alzheimer_with_mesh` list into a one-dimensional list (Reference: https://stackoverflow.com/questions/17485747/how-to-convert-a-nested-list-into-a-one-dimensional-list-in-python)
1. Create a function `flatten` that passes the list of mesh terms as parameter.
2. Inside the function, loop through all mesh terms in the list. If the mesh terms are in a nested list, convert the 2D list into a 1D list and return the mesh terms. If the mesh terms are already in a 1D list, simply return them. 

Step 3: Find the most common mesh terms in alzheimer papers (# Reference: https://www.delftstack.com/howto/python/python-counter-most-common/)
1. Use the `Counter` function to find all unique mesh terms
2. Use the `most_common(10)` to count the top 10 mesh terms from those unique mesh terms

Answer: 

The 10 most common Mesh terms for the Alzheimer papers are: 
```
[('Humans', 701),
 ('Alzheimer Disease', 699),
 ('Male', 351),
 ('Female', 299),
 ('Aged', 285),
 ('Animals', 273),
 ('Amyloid beta-Peptides', 211),
 ('Brain', 190),
 ('Aged, 80 and over', 170),
 ('Cognitive Dysfunction', 156)]
 ```
Step 4: 
1. Create a panda dataframe that stores the top 10 mesh terms in `word` column, and the count in `frequency` column. 
2. Plot the data frame into a bar chart.

![alz_mesh_terms](https://github.com/kristalz/BIS634/blob/main/Images/alz_mesh_terms.png)

#### Question 3: What are the 10 most common MeSH terms for the cancer papers whose metadata you found in Exercise 1? (2 points) Provide a graphic illustrating their relative frequency. (3 points)

Repeat the same steps to find the top 10 mesh terms for the cancer papers as above. 

Answer:

The 10 most common Mesh terms for the Alzheimer papers are: 

```
[('Humans', 222),
 ('Female', 96),
 ('Male', 63),
 ('Middle Aged', 63),
 ('Aged', 54),
 ('Adult', 52),
 ('Animals', 33),
 ('Neoplasms', 27),
 ('Retrospective Studies', 27),
 ('Aged, 80 and over', 21)]
 ```

![can_mesh_term](https://github.com/kristalz/BIS634/blob/main/Images/can_mesh_term.png)

#### Question 4: Make a labeled table with rows for each of the top 5 MeSH terms from the Alzheimer's query and columns for each of the top 5 MeSH terms from the cancer query. For the values in the table, provide the count of papers (combined, from both sets) having both the matching MeSH terms. (5 points)

Package requirements:
```
import numpy as np
```

Step 1: Find the top 5 mesh terms for both Alzheimer and cancer papers by using `Counter` and `most_common(5)`functions.

Step 2: Make an empty 5x5 2D matrix to store the counts for all 10 mesh terms.

Step 3: Loop through the two dimensions of matrix, compare top 5 the mesh terms in both paper to those in the original dictionary converted from the JSON file if those terms exist. If yes, add mesh terms' counts for Alzhimer's and Cancer papers into the matrix. 

Step 4: Because the original empty matrix store floats, convert floats to integer by using `astype(int)`. 

Step 5: Convert the matrix to a data frame with the top 5 mesh terms for Alzheimer's papers as index names (the row names) and the top 5 mesh terms for cancer papers as column names. 

Step 6: Generate a table of top 5 mesh terms from both papers by using the `table` function from maplotlib, storing the value from the 5x5 matrix in `CellText`, the top 5 mesh terms from two sets of papers as row and column labels, respectively. 

Answer: 

![top_5_mesh](https://github.com/kristalz/BIS634/blob/main/Images/top_5_mesh.jpg)


#### Question 5: Comment on any findings or limitations from the table and any ways you see to get a better understanding of how the various MeSH terms relate to each other.

Answer: It is not surprising to see that both sets of papers have the terms "humans, female, male, and aged" in their top five mesh terms list (with "humans" as the most common term), because Alzheimer and cancer are human disease. From the table, we can see that "male" appears more in both sets of papers than "female" does, implying that more studies are conducted on males for both diseases. The least common term from the table is "middle aged". This also makes sense because Alzheimer disease is more likely occur in the elderly, while some cancers can occur in middle age group. We can also see that when two different mesh terms combine, the counts that they appear in both sets of paper are fewer. For example, while the fourth most common mesh term "Alzheimer disease" in Alzheimer paper has total 699 counts, it has fewer counts when combine with other terms. There is a limitation in these mesh terms. The top five mesh terms in both sets of paper except for "Alzheimer disease" are so common and general that they can be applied in all other diseases as well. Thus, it might not be helpful to refine a search query for a speficific disease using these terms. 

## Exercise 3
<br/>

### Installation Instructions
<br/>
Install packages 'transformers', 'pytorch' and 'sklearn'. 

``` 
py -m pip install transformers
py -m pip install torch torchvision torchaudio
py -m pip install sklearn
```

### Code Instructions and answers
<br/>

Packages requirment
```
from transformers import AutoTokenizer, AutoModel
import json 
from sklearn import decomposition
import pandas as pd
import numpy as np
import plotnine as p9
```
#### Question 1 For each paper identified from exercise 1, compute the SPECTER embedding (a 768-dimensional vector). Keep track of which papers came from searching for Alzheimers, which came from searching for cancer. Apply principal component analysis (PCA) to identify the first three principal components. 

Step 1: Load the transformer model and tokenizer (Reference: https://github.com/allenai/specter).

Step 2: Load the Json file into a dictionary `papers`. 

Step 3: Preprocess the input that takes the titles and abstract for each paper. Results would be the model of the inputs. After modeling, take the first token in the batch as the embedding. Because the dictionary consists of lots of data, I could only preprocess one paper at a time by looping through metadata of all papers and store the embeddings for each paper into a list. 

Step 4: Convert the embeddings list into an array and pass it to the PCA model with 3 components. Store the values after PCA fit transformation into a pandas data frame with 3 columns (`'PC0', 'PC1', 'PC2'`). 

Step 5: Add a `query` columns into the data frame by extracting the queries from the `papers` dictionary. 

#### Question 2 Plot 2D scatter plots for PC0 vs PC1, PC0 vs PC2, and PC1 vs PC2; color code these by the search query used (Alzheimers vs cancer). Comment on the separation or lack thereof, and any take-aways from that.

Step 1: Create a list of PCA lables and store in a list: `'PC0', 'PC1', 'PC2'`. 

Step 2: Plot the paper data using plotnine and facet y=PCY, x=PCX. Loop through the PCA lables in x and y axes: If the PCA lable in the x axis is smaller than that in the y axis, plot the data frame with query names and PCA embeddings for each of the two components onto x and y axes. 

![PCs colored by Queries](https://github.com/kristalz/BIS634/blob/main/Images/PCs%20colored%20by%20Queries.png)

Visualize the results for PC0 vs PC1

![pc0 vs pc1](https://github.com/kristalz/BIS634/blob/main/Images/pc0%20vs%20pc1.png)

Visualize the results for PC0 vs PC2

![pc0 vs pc2](https://github.com/kristalz/BIS634/blob/main/Images/pc0%20vs%20pc2.png)

Visualize the results for PC1 vs PC2

![pc1 vs pc2](https://github.com/kristalz/BIS634/blob/main/Images/pc1%20vs%20pc2.png)

Commonts: There is increased lack of separation from the three groups of queries when the PCA components increased. We know that the axes of PCA components are ranked in order of important by the % of variability in which that PC0 > PC1 > PC2. There is lack of separation in the differences along the less important axes (PC1 and PC2). In both `PC0 vs PC2` and `PC1 vs PC2`, the third query "Alzheimer/Cancer" disappears from the plots. Thus, we know that the variation among the papers can be best explained by PC0 and PC1, which is also illustrated from the plots. 

#### Question 3 Repeat the above using LDA instead of PCA. In your commentary, be sure to compare PCA vs LDA. 

Package requirement: 
```
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
```
Step 1: Extract the query names from the pca data frame created above and store in a `target_name` list. Different from PCA, LDA is a supervised learning model and requires a target parameter. LDA only allows numbers of compenents as the number of features - 1. In this case, the number of features is three different queries, so the n components are 2.  

Step 2: Pass the embeddings array into the LDA model with 2 components. Store the values after LDA fit transformation into a pandas data frame with 2 columns (`'LD0', '1'LD`). Add a `query` columns into the data frame by extracting the queries from the `papers` dictionary.

Step 3: Plot the LDA data frame to visualize the results for LD0 vs LD1.

![LD0 vs LD1](https://github.com/kristalz/BIS634/blob/main/Images/LD0%20vs%20LD1.png)

From the plot, we see that the overlap paper `'Alzhiemer/Cancer'` is greatly separated from the other two queries. The cluster of `Alzheimer` and `Cancer` papers are clearly sparated as well. The separation among papers using an LDA model is better than using an PCA model, since maximizing separation is the main goal for LDA. Different from PCA, LDA takes the query label into consideration and minimizes the variation within each category of label. LDA reduces dimensionality while preserving as much of the class discrimination information as possible at the same time. In contrast, PCA does not require knowing the query labels beforehead. In general, PCA performs better when sample size per class is small, while LDA works better with large dataset having multiple classes. Thus, in our case, using a LDA model to predict query classification for each paper is better. 

## Exercise 4
<br/>


## Exercise 5
<br/>

Packages requirement 
```
import pandas as pd 
import plotnine as p9
from plotnine import position_dodge
from plotnine.data import mtcars
```
### Data
```
RANDS3.csv
```
This dataset is a round 3 healthcare survey conducted by  Research and Development Survey (RANDS) that include healthcare conditions, past medical history, lifestyle, and more. I downloaded from CDC.gov https:////www.cdc.gov/nchs/rands/data.htm. There are 2646 responses in this dataset.

### Prepare and clean the data 

First I loaded the data into a pandas data frame and changed all missing values into `NAN`. There are a variety forms of missing values: The `'.',' .','   . '`represent the missing values, whereas `998,98` reresent "implicit refusal (skipping the question)' according to the dataset codebook. I checked multiple times with the orginal csv file to make sure I standardize all the missing values. I will elaborate how I handled these missing values and what reasons I though they were missing later in this section. 
```
data = pd.read_csv('C:/Users/kryst/OneDrive/Desktop/Fall 1st/BIS 634/RANDS3.csv',na_values = ['.',' .','   . ',998,98]) # Replacing all missing values 
data.head()
```
Here is the glimpse of the data with missing values:

![Data with missing values](https://github.com/kristalz/BIS634/blob/main/Images/Data%20with%20missing%20values.jpg)

The column names were coded and would not be helpful in later analysis. I decided to changed them into meaningful names. I was interested to learn the relationships of hypertension and some of its potential risk factors available in the data. The risk factors for hypertension can be modifiable such as smoking, physical activities, and other related diseases (i.e., diabetes), and unmodifiable such as age and race. Thus, I selected the columns that represent the risk factors from the data: age, gender, race/ethnicity, depression prediabetes, diabetes (ages and types of diagnoses are also included), hypercholemia, smoking status and three levels of physical activities (light/moderate, muscular, and vigorous). The smoking status were described by two columns. The `Smoking` column captured the answers for "Have you smoked at least 100 cigarettes in your entire life? " and `Smoking frequency` for "Do you now smoke cigarettes every day, some days, or not at all?". 

I also included other demographic factors (education, employment, income) and geopgraphic information (region) to visualize the prevalence of hypertension in different parts of the U.S.. I included "depression" as a risk factor beccause I am interested about the psychological effects in hypertension. For both hypertension and hypercholemia diagnoses, I included the columns `Hypertension Past Year` and `Hypercholemia Past Year` to to present whether the responders had hypertension or hypercholemia during the past 12 months. These two columns are distinguished from the columns of `Hypertension Diagnose` and `Hypercholemia Diagnose` that captured the answers of responders' diagnose records not specified in a time frame. 

The new data frame with selected columns is displayed below. I renamed the data frame as `htn_data`. 
![HTN_data_with_missing_values](https://github.com/kristalz/BIS634/blob/main/Images/HTN_data_with_missing_values.jpg)

I printed out the missing values for each column: 

![Missing values counts](https://github.com/kristalz/BIS634/blob/main/Images/Missing%20values%20counts.jpg)

Since there are high percentages of missing values in the five columns `'Hypertension Past Year', 'Hypercholemia Past Year', 'Diabetes Age', 'Diabetes Type', 'Smoking Frequency'`, I decided to drop these fields. The two columns `'Diabetes Age', 'Diabetes Type'` missed almost the entire participants' responses (n=2367 for both columns). I considered the missing values for these two columns as MAR (missing at random) because people who do not have ever diagnosed with diabetes would not fill out these two columns. Given that there are many missing values in these two columns, I assume that the majority of participants have not diagnosed with diabetes. 

In contrast, I consider  `'Smoking Frequency', 'Hypertension Past Year', 'Hypercholemia Past Year'` are MNAR(missing not at random). There are no clear patterns in the missing values and non-missing values in these three columns. The reasons what cause those missing values are unclear and unobserved. I was not sure if people who smoked or who have those two diagnoses forgot the answers or simply refused to answer the questions, because missingness was not measured by the researchers. 

I also deleted the rows where values were missing in other columns, although I was aware that this might bias the data set and decrease the statistical power in my analsis. I also changed all values to integers. Here is the data set after reducing the missing values: 

![HTN_data_without_missing_values](https://github.com/kristalz/BIS634/blob/main/Images/HTN_data_without_missing_values.jpg)

Now there are no missing values in the data. I noticed that the ages were continuous variables. I decided to group the ages into discrete intervals `('18-34','35-54', '55-64','64-70')` for more convenient analysis. Since the values in the data set are all categorical numbers, I specified that using `astype('category')` to tell pandas how to handle the values. I replaced  "Yes/No" for values 1 or 2 in `Hypertension Diagnose` for more convenient analysis. Now I completed the data cleaning process for my data set. It's ready for more exploration. 

### Data exploration 

1. Visualize the hypertension diagnose prevalence by ages, genders, and races

I extracted a subset of dataframe by grouping `'Age','Gender','Race&Ethnicity'` using `groupby()` to count the numbers of hypertension diagnoses, and reset the index name as `Hypertension` for the counts of diagnoses. I replaced the responses for `'Gender'` and `'Race&Ethnicity'` with the answer choices provided by the codebook. Then I ploted the the subset dataframe using plotnine. I faceted the graph by race.

![age_gender_race](https://github.com/kristalz/BIS634/blob/main/Images/age_gender_race.png)

We can ses that hypertension is more prevalent in Whites(non-Hispanic) and 35-54 age group. The numbers of hypertension diagnose are relatively the same among females and males. 

2. Visualize the hypertension diagnose prevalence by ages, genders, and races separately.

I would like to know how is hypertension associated with each of the three factors I extracted in step one. Therefore, I extracted three separate subsets by grouping `'Hypertension'` with `'Age','Gender','Race&Ethnicity'` one at a time. 

Compare counts of hyptersion diagnose by genders: 

![htn_gender](https://github.com/kristalz/BIS634/blob/main/Images/htn_gender.png)

Compare counts of hyptersion diagnose by age groups: 

![htn_age](https://github.com/kristalz/BIS634/blob/main/Images/htn_age.png)

Compare counts of hyptersion diagnose by Race/Ethnicity groups:

![htn_races](https://github.com/kristalz/BIS634/blob/main/Images/htn_races.png)

Hypertension is more prevalent in the male responders, most prevalent in whites and in the elderly (64-70).We can observe that prevalences in ages are different when combining with race, in which hypertension is more prevalent in the middle ages (35-54) Whites. 

3. Visualize the hypertension diagnose prevalence in other demographic factors (education, employment, income, and region).

Compare counts of hyptersion diagnose by education, employment, income, and region: 

I followed the same procedures by grouping these four demographic factors above and counted the numbers of hypertension diagnose. First, I faceted the graph by employment status:

![ed_employ_region](https://github.com/kristalz/BIS634/blob/main/Images/ed_employ_region.png)

We can see that more employed repsonders are diagnosed with hypertension, especially in the South and Midwest regions. 

Then I faceted the graph by education levels:

![facet_by_ed](https://github.com/kristalz/BIS634/blob/main/Images/facet_by_ed.png)

Again, more repsonders who are employed are diagnosed with hypertension in the South and Midwest regions. Hypertension seems to be more prevalent in those who have higher educational degrees. 

4. Visualize hypertension diagnose prevalence by prediabetes, diabetes, hypercholemia, smoking status, and levels of depression

I would also like to know how other medical conditions affect hypertension. Thus, I extracted those factors out from the data set and counted the numbers of hypertension diagnoses for these grouped factors. 

Compare by diabetes/prediabetes, smoking states, and depression levels: 

![facet_by_depre_diab](https://github.com/kristalz/BIS634/blob/main/Images/facet_by_depre_diab.png)

![facet_by_depre_prediab](https://github.com/kristalz/BIS634/blob/main/Images/facet_by_depre_prediab.png)

The assocaition of hypertension and diabetes or prediabetes is stronger when the depression level is higher (weekly or daily). There are also more smokers diagnosed with hypertension. 

Compare by hypercholemia, smoking, and depression: 

![hypercholemia_depre_smok](https://github.com/kristalz/BIS634/blob/main/Images/hypercholemia_depre_smok.png)

The assocaition of hypertension and hypercholemia is stronger when the depression level is higher (weekly or daily).

5. Visualize hypertension diagnose prevalence by levels of activities. 

The survey asked the responders to answer their exercise frequencies for each levels (light/moderate, muscular, and vigorous) of physical activities if they do that type of exercise at least 10 minutes each time. 

I grouped the counts of hypertension by activity levels, age, and employment status. First I compared the effects of light/moderate activity, age, and employment status in hypertension.

![light_moderate activities](https://github.com/kristalz/BIS634/blob/main/Images/light_moderate%20activities.png)

We can see that most responders had at least 10 minutes light to moderate physical activities weekly. However, the relationship between activity frequency and hypertension is not clear. Hypertension is most prevalent in those who are employeed before age of 64. 

I also compred the effects in the two other levels of activities. 

![muscular_activity](https://github.com/kristalz/BIS634/blob/main/Images/muscular_activity.png)

![vigorous_activity](https://github.com/kristalz/BIS634/blob/main/Images/vigorous_activity.png)

Again, most responders had at least 10 minutes muscular and vigorous activities weekly. From the three graphs above, we can see that the relationship between activity frequency and hypertension is not clear, regardless of the type of activity. 