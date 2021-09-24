# Exercise 4

# 4a. Make a function that takes a population size n and a number of drug users d and returns a list of size n 
# with d True values and n - d False values. The Trues represent drug users, the Falses represent non-drug users. 


import random


def simulate_drug_use(n, d):

    # n = population size
    # d = number of true drug users in the population 

    drug_users = [True for n in range(d)] 
    non_drug_users = [False for n in range(n - d)]
    drug_users = drug_users + non_drug_users
    random.shuffle(drug_users)
    return drug_users


# Test the above function (can take out)


print(simulate_drug_use(100, 50))


# 4b. Make a function that selects a sample of size s (think: study participants) from such a population and returns that 
# sample's responses to the protocol from the slides. In particular, for each study participant, they flip a coin 
# (choose one of two paths randomly with equal probability). If they flip "heads", they flip a coin and either report 
# True or False (with equal probability). If instead, they flip "tails", they report their drug use status (True or False). 
 

def simulate_sample_response(n, d, s):
    
    # n = population size
    # d = number of true drug users in the population 
    # s = sample size
    
    drug_use_response = simulate_drug_use(n, d) # List of drug use in populaiton 
    sample = random.sample(drug_use_response, s) # Randomly select a list of drug use in a chosen number of sample 


    for s in range(0, len(sample)): 
        s = random.randint(0, 1)  
        heads = 0
        tails = 0
        if (s == 0):
            return random.choices([True,False], weights=(50, 50), k=len(sample))
        else:
            return sample
        


# Test the above function 


print(simulate_sample_response(1000, 100, 50))



# 4c. Make a function that takes parameters for the total population, the true number of drug users in the population,
# the sample size, and returns the estimated number of drug users in the population that would be predicted using
# such a sample and the randomized response protocol. (Hint: recall from class that the E[yes] = 0.25 + 0.5p,
# where p is the fraction of drug users; use the measured yes rate to predict the fraction.)


def predict_drug_user_fraction(n, d, s):

    # n = population size
    # d = number of true drug users in the population 
    # s = sample size

    sample = simulate_sample_response(n, d, s)
    espected_drug_users = sample.count(True)
    espected_drug_users_rate = espected_drug_users/s

    fraction_estimated_drug_users = (espected_drug_users_rate - 0.25)/0.5
    if fraction_estimated_drug_users <= 0:
        fraction_estimated_drug_users = 0
    return fraction_estimated_drug_users


# 4d. Suppose that we have a population of 1000 people, 100 of whom are drug users and we do a survey using this
# protocol that samples 50 people from the total population. What is the estimated number of drug users you get
# from such an approach?

fraction_estimated_drug_users = predict_drug_user_fraction(1000, 100, 50)
print(fraction_estimated_drug_users)
# Output: 0.54

estimated_drug_users = fraction_estimated_drug_users*1000
print(estimated_drug_users)
# Output: 540


# 4e. Your results in part d will obviously depend on which 50 people you surveyed and how their coin-flips worked out.
# To get a sense of the distribution, repeat the experiment many times (justify how you decided how many was enough in
# your readme; 2 points) and plot a histogram showing the predictions (4 points).


number_of_trials = 1000

result_4e = []
for trials in range(number_of_trials):
    fraction_estimated_drug_users = predict_drug_user_fraction(1000, 100, 50)
    estimated_drug_users = fraction_estimated_drug_users*1000
    result_4e.append(estimated_drug_users)    
print(result_4e)

from matplotlib import pyplot as plt

plt.hist(result_4e)


# 4f. Repeat parts d and e but with a population of 100_000 people, 10_000 drug users and sampling 5_000 people;
# i.e. with everything scaled up by a factor of 100. (5 points) How do your results compare? (3 points)

fraction_estimated_drug_users = predict_drug_user_fraction(100000, 10000, 5000)
print(fraction_estimated_drug_users)
# Output: 0.4936

estimated_drug_users = fraction_estimated_drug_users*100000
print(estimated_drug_users)
# Output: 49360


number_of_trials = 100

result_4f = []
for trials in range(number_of_trials):
    fraction_estimated_drug_users = predict_drug_user_fraction(100000, 10000, 5000)
    estimated_drug_users = fraction_estimated_drug_users*100000
    result_4f.append(estimated_drug_users)    
print(result_4f)

plt.hist(result_4f)


# 4g. Repeat parts d and e but with 500 drug users in a population of 1_000 and sampling 50 people. i.e.
# with the smaller population but with higher drug usage rates. (5 points) How do your results compare? (3 points)


fraction_estimated_drug_users = predict_drug_user_fraction(1000, 500, 50)
print(fraction_estimated_drug_users)
# Output: 0.38

estimated_drug_users = fraction_estimated_drug_users*1000
print(estimated_drug_users)
# Output: 380


number_of_trials = 1000

result_4g = []
for trials in range(number_of_trials):
    fraction_estimated_drug_users = predict_drug_user_fraction(1000, 500, 50)
    estimated_drug_users = fraction_estimated_drug_users*1000
    result_4g.append(estimated_drug_users)    
print(result_4g)

plt.hist(result_4g)
