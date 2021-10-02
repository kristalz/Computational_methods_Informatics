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

test = sequence[0:1000000]

def find_min_hash_median(a,seq):
    min_list = []
    for i in range(1, a+1):
        my_hash = get_ath_hash(i)
        min_h = my_hash(seq[0:15])
        for j in range(1, len(seq)-14):
            new_h = my_hash(seq[j:j+15])
            if new_h < min_h:
                min_h = new_h
        min_list.append(min_h)
    return statistics.median(min_list)

# Estimate min hash in a range of a = 1 to 10
test_min_hash1 = find_min_hash_median(10,test)
#29120.0

test_min_hash_scale1 = test_min_hash1/34359738367 
test_min_hash_scale1
# 8.47503542924751e-07

min1 = (1/test_min_hash_scale1)-1
min1
# 1179935.0702953297

# Estimate min hash in a range of a = 1 to 100
test_min_hash2 = find_min_hash_median(100,test)
test_min_hash2
# 23099.0

test_min_hash_scale2 = test_min_hash2/34359738367 
test_min_hash_scale2
# 6.722693797396574e-07

min2 = (1/test_min_hash_scale2)-1
min2
# 1487497.9552361574

test_sub=[test[i:i+15] for i in range(len(test)-14)]
len(set(test_sub))
# 931157

# From the results above, we can see that from a=1-10 is closer to the true distinct values of the subsequence in the test dataset. 

# Test on some fake dataset

import random

# Randomly generate different nucleic acids to compose a fake chromosome sequence 
nucleic_acid_choices = ['a','c','t','g','n']
fake_seq_list= []
for i in range(100000):
    fake_seq_list.append(random.choice(nucleic_acid))
    # Joining each individual numbers into the entire sequence 
    fake_seq = "".join(fake_seq_list)

fake_seq = str(chromosome.seq).lower().encode('utf8')

# Create a fake_subseq for the fake sequence subsetting every 15-mer as a subsequence
fake_subseq=[fake_seq[i:i+15] for i in range(len(fake_seq)-14)]

# Find the minimal hash value on the fake dataset

fake_min_h_10 = find_min_hash_median(10,fake_seq)
fake_min_h_10 # 1207660.5

fake_min_h_10_scale = fake_min_h_10/34359738367 
fake_min_h_10_scale # 3.5147546442317184e-05

fake_min_10 = (1/fake_min_h_10_scale)-1
fake_min_10 # 28450.488118556495


fake_min_h_100 = find_min_hash_median(100,fake_seq)
fake_min_h_100 # 1316809.0

fake_min_h_100_scale = fake_min_h_100/34359738367 
fake_min_h_100_scale # 3.832418588101643e-05

fake_min_100 = (1/fake_min_h_100_scale)-1
fake_min_100 # 26092.18311691369

len(set(fake_subseq))
# 16554

# From the results above, we can see that from a=1-100 is closer to the true distinct values of the subsequence in the fake dataset. 

# Find the minimal hash value on the entire sequence 


# Estimate min hash in a range of a = 1 to 5:       
min_h_5 = find_min_hash_median(5,sequence)
min_h_5 
# 177

# Divided the min hash by scale to get the probability from 0 to 1
min_h_5_scale = min_h_5/34359738367 
min_h_5_scale
# 5.15137799099179e-09

# Find the minimal distingushed value
min5 = (1/min_h_5_scale)-1
min5
# 194122814.63276836

# Estimate min hash in a range of a = 1 to 10: 
min_h_10 = find_min_hash_median(10,sequence)
min_h_10 
# 247.5

# Divided the min hash by scale to get the probability from 0 to 1
min_h_10_scale = min_h_10/34359738367 
min_h_10_scale 
# 7.203198038251232e-09

# Find the minimal distingushed value 
min10 = (1/min_h_10_scale)-1
min10
# 138827224.72525254

# Estimate min hash in a range of a = 1 to 100
min_h_100 = find_min_hash_median(100,sequence)
min_h_100 # 170.5

# Divided the min hash by scale to get the probability from 0 to 100
min_h_100_scale = min_h_100/34359738367 
min_h_100_scale # 4.9622030930175156e-09

# Find the minimal distingushed value 
min100 = (1/min_h_100_scale)-1
min100 # 201523391.1818182

# Check the result of the function 

subseq=[sequence[i:i+15] for i in range(len(sequence)-14)]
len(set(subseq))
# 145003145

# From the results above, we can see that from a=1-10 is closer to the true distinct values of the subsequence. 
