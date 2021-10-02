# Write code to loop through all 15-mers, subsequences of 15 bases within chromosome 2 (CM000664.2).  (5 points)


# py -m pip install BioPython

from Bio import SeqIO
human_genome = SeqIO.parse("GCA_000001405.28_GRCh38.p13_genomic.fna", "fasta")
for chromosome in human_genome:
    if chromosome.name == "CM000664.2":
        sequence = str(chromosome.seq).lower().encode('utf8')
# Get all substrings of string
print(f"There are a total of {len(sequence)-14} (potentially duplicated) subsequences.")

# There are a total of 242193515 (potentially duplicated) subsequences.

# How many total subsequences are there (counting duplicates) that do not contain more than 2 Ns? (5 points)


subseq_noN=[i for i in range(len(sequence)-14) if sequence[i:i+15].count(b'n')<=2] # reference: https://www.biostars.org/p/14834/
print(f"There are a total of {len(subseq_noN)} subsequences that do not contain more than 2 Ns")

# There are a total of 240548031 subsequences that do not contain more than 2 Ns


# Using 100 hash functions from the family below and a single pass through the sequences, 
# estimate the number of distinct 15-mers in the reference genome's chromosome 2 using the big data method for estimating distinct counts discussed in class. (5 points) 


p = 2_549_536_629_329
bits_48 = 2 ** 48 - 1
scale = 0x07ffffffff
from hashlib import sha256
def get_ath_hash(a):
    def my_hash(subseq):
        return (((int(sha256(subseq).hexdigest(), 16) % bits_48) * a) % p) & scale
    return my_hash 

# Test the function in range a = 1....100 on a small subset of the subsequence 

# Found the min hash for the first 15000000 subsequences
first_hash = get_ath_hash(1)
min_h_test= first_hash(sequence[0:15000000])
min_h_test
# 23262025092

# Test the entire list of 15-mer subsequences on a = 1
for i in range(1, len(sequence)-14):
    new_h = first_hash(sequence[i:i+15])
    if new_h < min_h1:
        min_h1 = new_h
min_h1
# 520

# Print out the scale
0x07ffffffff = 34359738367

# Divided the min hash by scale to get the probability from 0 to 1
min_h1_scale = min_h1/34359738367 
min_h1_scale
# 1.5133991837941983e-08

# Find the minimal distingushed value using 
min = (1/min_h1_scale)-1
min
# 66076418.93653846

# Find the minimal hash value using a = 100

hundredth_hash = get_ath_hash(100)
min_h100 = hundredth_hash(sequence[0:15])
for i in range(1, len(sequence)-14):
    new_h = hundredth_hash(sequence[i:i+15])
    if new_h < min_h100:
        min_h100 = new_h
min_h100
# 80

# Divided the min hash by scale to get the probability from 0 to 1
min_h100_scale = min_h100/34359738367 
min_h100_scale
# 2.328306436606459e-09

# Find the minimal distingushed value 
min = (1/min_h100_scale)-1
min
# 429496728.5875


# How does your estimate change for different-sized subsets of these hash functions, 
# e.g. the one with a=1 only, or a=1, 2, .., 10, or a=1, 2, ...100, etc?

import statistics

# Test on a median size dataset

test = sequence[0:15000000]

def find_min_hash_median_test(a):
    min_list = []
    for i in range(1, a+1):
        my_hash = get_ath_hash(i)
        min_h = my_hash(test[0:15])
        for j in range(1, len(test)):
            new_h = my_hash(test[j:j+15])
            if new_h < min_h:
                min_h = new_h
        min_list.append(min_h)
    return statistics.median(min_list)

test_min_hash = find_min_hash_median_test(100)
test_min_hash 
# 2026.5

test_min_hash_scale = test_min_hash/34359738367 
test_min_hash_scale
# 5.897891242228736e-08

min = (1/test_min_hash_scale)-1
min
# 16955211.61633358

# Find the minimal hash value on the entire sequence 
def find_min_hash_median(a):
    min_list = []
    for i in range(1, a+1):
        my_hash = get_ath_hash(i)
        min_h = my_hash(sequence[0:15])
        for j in range(1, len(sequence)-14):
            new_h = my_hash(sequence[j:j+15])
            if new_h < min_h:
                min_h = new_h
        min_list.append(min_h)
    return statistics.median(min_list)

# Estimate min hash in a range of a = 1 to 5:       
min_h_5 = find_min_hash_median(5)
min_h_5 
# 177

# Divided the min hash by scale to get the probability from 0 to 1
min_h_5_scale = min_h_5/34359738367 
min_h_5_scale
# 5.15137799099179e-09

# Find the minimal distingushed value
min = (1/min_h_5_scale)-1
min
# 194122814.63276836

# Estimate min hash in a range of a = 1 to 10: 
min_h_10 = find_min_hash_median(10)
min_h_10 
# 247.5

# Divided the min hash by scale to get the probability from 0 to 1
min_h_10_scale = min_h_10/34359738367 
min_h_10_scale 
# 7.203198038251232e-09

# Find the minimal distingushed value 
min = (1/min_h_10_scale)-1
min
# 138827224.72525254

# Estimate min hash in a range of a = 1 to 50: 
min_h_50 = find_min_hash_median(50)
min_h_50 
# 167.5

# Divided the min hash by scale to get the probability from 0 to 1
min_h_50_scale = min_h_50/34359738367 
min_h_50_scale
# 4.874891601644773e-09

# Find the minimal distingushed value 
min = (1/min_h_50_scale)-1
min
# 205132765.37014925

# Estimate min hash in a range of a = 1 to 100
min_h_100 = find_min_hash_median(100)
min_h_100 # 170.5

# Divided the min hash by scale to get the probability from 0 to 100
min_h_100_scale = min_h_100/34359738367 
min_h_100_scale # 4.9622030930175156e-09

# Find the minimal distingushed value 
min = (1/min_h_100_median_scale)-1
min_100 # 201523391.1818182



