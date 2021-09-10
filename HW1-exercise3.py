# Exercise 3


import pandas as pd
import plotnine as p9

covid_data = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
print(covid_data.head())
# Download on 9/8/2021

# Change to datetime

covid_data["date"] = pd.to_datetime(covid_data["date"])
print(covid_data.head())


# Make a function that takes a list of state names and plots their cases vs date using overlaid line graphs,
# one for each selected state.


def plot_state_by_cases(state_list):
    # Create a sublist that includes the data of my test state_list
    test_covid_data = covid_data[covid_data["state"].isin(state_list[:])]
    # Graph the test state_list
    graph = (
            p9.ggplot(test_covid_data, p9.aes("date", "cases", color="state")) +
            p9.geom_line() +
            p9.scale_y_continuous(trans='log10') +
            p9.theme(axis_text_x=p9.element_text(angle=20))
    )
    graph.draw()


# Test the above function

## Test three states in the East Coast

state_list_1 = ["New Jersey", "Connecticut", "New York"]
print(plot_state_by_cases(state_list_1))

## Test three states in the West Coast

state_list_2 = ["Washington", "Nevada", "California"]
print(plot_state_by_cases(state_list_2))

## Test three states in the Middle West

state_list_3 = ["Ohio", "Minnesota", "Illinois"]
print(plot_state_by_cases(state_list_3))


# Make a function that takes the name of a state and returns the date of its highest number of new cases.


import numpy as np


def find_date_highest_new_cases(test_state):
    test_cases = np.array(covid_data[covid_data["state"] == test_state]["cases"])
    test_dates = np.array(covid_data[covid_data["state"] == test_state]["date"])
    
    previous_cases_difference = test_cases[1] - test_cases[0]

    for i in range(2, len(test_dates)):
        current_cases_difference = test_cases[i] - test_cases[i-1]
        if previous_cases_difference <= current_cases_difference:
            previous_cases_difference = current_cases_difference
            current_highest_date = pd.to_datetime(test_dates[i])
    return current_highest_date


# Test the above function 


print(find_date_highest_new_cases("New York")) 
# Output: 2021-03-24 00:00:00

print(find_date_highest_new_cases("Connecticut")) 
# Output: 2020-12-28 00:00:00


print(find_date_highest_new_cases("New Jersey")) 
# Output: 2021-01-04 00:00:00


# Make a function that takes the names of two states and reports which one had its highest number of cases first and
# how many days separate that one's peak from the other one's peak.


def find_difference_in_days(states):
    state1 = states[0]
    state2 = states[1]
    date1 = (find_date_highest_new_cases(state1)) 
    print(f"{state1} has its highest number of cases on {date1}\n")
    date2 = (find_date_highest_new_cases(state2))
    print(f"{state2} has its highest number of cases on {date2}\n")
    days_differences = (date1 - date2).days
    if days_differences > 0:
        print(
            f"{state1} has its highest number of cases first. \n{state1} and {state2} have {days_differences} "
            f"between them.\n")
    elif days_differences < 0:
        print(
            f"{state2} has its highest number of cases first. \n{state1} and {state2} have {days_differences} "
            f"between them.\n")
    elif days_differences == 0:
        print(f"{state1} and {state2} have the same peak number in cases.\n")


# Test the above function


states_1 = ["Washington", "Connecticut"]
print(find_difference_in_days(states_1))

# Output: Washington has its highest number of cases on 2021-09-07 00:00:00

# Connecticut has its highest number of cases on 2020-12-28 00:00:00

# Washington has its highest number of cases first. 
# Washington and Connecticut have 253 between them.


states_2 = ["New York", "Connecticut"]
print(find_difference_in_days(states_2))

# Output: New York has its highest number of cases on 2021-03-24 00:00:00

# Connecticut has its highest number of cases on 2020-12-28 00:00:00

# New York has its highest number of cases first. 
# New York and Connecticut have 86 between them.

states_2 = ["New Jersey", "Connecticut"]
print(find_difference_in_days(states_2))

# Output: New Jersey has its highest number of cases on 2021-01-04 00:00:00

# Connecticut has its highest number of cases on 2020-12-28 00:00:00

# New Jersey has its highest number of cases first. 
# New Jersey and Connecticut have 7 between them.