# Exercise 2


import pandas as pd 
import sqlite3

with sqlite3.connect("hw1-population.db") as db:
    data = pd.read_sql_query("SELECT * FROM population", db)


# Find the names of the columns


print(data.head())
list(data.columns)


# Find the number of rows


print(len(data["name"]))


# Examine the distribution of ages


mean_age = data["age"].mean()
print(mean_age)
sd_age = data["age"].std()
print(sd_age)
min_age = data["age"].min()
print(min_age)
max_age = data["age"].max()
print(max_age)

# Plot the distribution of ages


import plotnine as p9


(
        p9.ggplot(data, p9.aes("age")) + p9.geom_histogram(bins=100)
)



# Find the distribution of weights


mean_weight = data["weight"].mean()
print(mean_weight)
sd_weight = data["weight"].std()
print(sd_weight)
min_weight = data["weight"].min()
print(min_weight)
max_weight = data["weight"].max()
print(max_weight)

# Plot the distribution of weights


(
        p9.ggplot(data, p9.aes("weight")) + p9.geom_histogram(bins=50)
)


# plot the weights vs the ages

(
        p9.ggplot(data, p9.aes("age", "weight")) + p9.geom_point()
)

# The short way: 

data_outlier = data[data["age"] >= 25]
data_outlier = data_outlier[data_outlier["age"] <= 50]
print(data_outlier)
print(data_outlier[data_outlier["weight"] < 25]["name"])

# The long way: 

## Visualize the statistics of data


data.describe()

## Fine q1 and q3 values


q1, q3 = data.weight.quantile([0.25, 0.75])
print(q1, q3)

## Compute IRQ


irq = q3 - q1
print(irq)

## Find lower and upper bounds

lower_bound = q1 - (1.5 * irq)
upper_bound = q3 + (1.5 * irq)
print(lower_bound, upper_bound)

## Find the outlier

data_outlier = data[data["age"] >= 25]
data_outlier = data_outlier[data_outlier["age"] <= 50]
print(data_outlier)
print(data_outlier[data_outlier["weight"] < lower_bound]["name"])
