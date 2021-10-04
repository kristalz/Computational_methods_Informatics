# Write code to loop through all 15-mers, subsequences of 15 bases within chromosome 2 (CM000664.2).  (5 points)

# py -m pip install BioPython

from Bio import SeqIO
human_genome = SeqIO.parse("GCA_000001405.28_GRCh38.p13_genomic.fna", "fasta")
for chromosome in human_genome:
    if chromosome.name == "CM000664.2":
        sequence = str(chromosome.seq).lower().encode('utf8')
        subseq=[sequence[i:i+15] for i in range(len(sequence)-14)]

print(f"There are a total of {len(subseq)} (potentially duplicated) subsequences.")
# There are a total of 242193515 (potentially duplicated) subsequences.


# How many total subsequences are there (counting duplicates) that do not contain more than 2 Ns? (5 points)

subseq_noN=[i for i in range(len(subseq)) if sequence[i:i+15].count(b'n')<=2] 
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
min_test= first_hash(sequence[0:15000000])
print(min_test)
# 23262025092

test_seq= sequence[0:15000000]

# Check the result of the function 

test_subseq=[test_seq[i:i+15] for i in range(len(test_seq)-14)]
print(len(set(test_subseq)))
# 13178676

# Looping through the entire test sequence to find the minimal hash
for i in range(1, len(test_seq)):
    new_hash = first_hash(test_seq[i:i+15])
    if new_hash < min_test:
        min_test = new_hash
print(min_test)
# 13349

# Print out the scale
print(0x07ffffffff) # 34359738367

# Divided the min hash by scale to get the probability from 0 to 1
min_test_scale = min_test/34359738367 
print(min_test_scale)
# 3.8850703277824525e-07

# Find the minimal distingushed value using 
min_1 = (1/min_test_scale)-1
print(min_1)
# 2573954.979249382

# Modify the function on entire list of 15-mer subsequences on a = 1

first_hash = get_ath_hash(1)
min_h1= first_hash(sequence[0:15])

for i in range(1, len(sequence)-14):
    new_h = first_hash(sequence[i:i+15])
    if new_h < min_h1:
        min_h1 = new_h
print(min_h1)
# 520

# Divided the min hash by scale to get the probability from 0 to 1
min_h1_scale = min_h1/34359738367 
print(min_h1_scale)
# 1.5133991837941983e-08

# Find the minimal distingushed value using 
min_1 = (1/min_h1_scale)-1
print(min_1)
# 66076418.93653846

# Check the result of the function 

print(len(set(subseq)))
# 145003145

# Using only a=1 was not closed to the actual distinct values. 

# Find the minimal hash value using a = 100

hundredth_hash = get_ath_hash(100)
min_h100 = hundredth_hash(sequence[0:15])
for i in range(1, len(sequence)-14):
    new_h = hundredth_hash(sequence[i:i+15])
    if new_h < min_h100:
        min_h100 = new_h
print(min_h100)
# 80

# Divided the min hash by scale to get the probability from 0 to 1
min_h100_scale = min_h100/34359738367 
print(min_h100_scale)
# 2.328306436606459e-09

# Find the minimal distingushed value 
min_100 = (1/min_h100_scale)-1
print(min_100)
# 429496728.5875

# Using only a=100 was even further away from the actual distinct values. 

# How does your estimate change for different-sized subsets of these hash functions, 
# e.g. the one with a=1 only, or a=1, 2, .., 10, or a=1, 2, ...100, etc?

import statistics


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

# Test on a median size dataset

test = sequence[0:1000000]

# Estimate min hash in a range of a = 1 to 10
test_min_hash1 = find_min_hash_median(1,test)
print(test_min_hash1)
# 37244

test_min_hash_scale1 = test_min_hash1/34359738367 
print(test_min_hash_scale1)
# 1.083943061562137e-06

min1 = (1/test_min_hash_scale1)-1
print(min1)
# 922556.683573193

test_min_hash2 = find_min_hash_median(10,test)
print(test_min_hash2)
# 29120.0

test_min_hash_scale2 = test_min_hash2/34359738367 
print(test_min_hash_scale2)
# 8.47503542924751e-07

min2 = (1/test_min_hash_scale2)-1
print(min2)
# 1179935.0702953297

# Estimate min hash in a range of a = 1 to 100
test_min_hash3 = find_min_hash_median(100,test)
print(test_min_hash3)
# 23099.0

test_min_hash_scale3 = test_min_hash3/34359738367 
print(test_min_hash_scale3)
# 6.722693797396574e-07

min3 = (1/test_min_hash_scale3)-1
print(min3)
# 1487497.9552361574

test_sub=[test[i:i+15] for i in range(len(test)-14)]
print(len(set(test_sub)))
# 931157

# From the results above, we can see that from a=1 is closest to the true distinct values of the subsequence in the test dataset. 

# Test on some fake dataset

import random
random.seed(1) 

# Randomly generate different nucleic acids to compose a fake chromosome sequence 
nucleic_acid_choices = ['a','c','t','g','n']
fake_seq_list= []
for i in range(1000000):
    fake_seq_list.append(random.choice(nucleic_acid_choices))
    # Joining each individual numbers into the entire sequence 
    fake_seq = "".join(fake_seq_list)

fake_seq = fake_seq.encode('utf8')

# Create a fake_subseq for the fake sequence subsetting every 15-mer as a subsequence
fake_subseq=[fake_seq[i:i+15] for i in range(len(fake_seq)-14)]

# Find the minimal hash value on the fake dataset

fake_min_h_1 = find_min_hash_median(1,fake_seq)
print(fake_min_h_1) # 2081562

fake_min_h_1_scale = fake_min_h_1/34359738367 
print(fake_min_h_1_scale) # 6.058142753494267e-05

fake_min_1 = (1/fake_min_h_1_scale)-1
print(fake_min_1) # 3168547.3554961267

fake_min_h_10 = find_min_hash_median(10,fake_seq)
print(fake_min_h_10) # 1207660.5

fake_min_h_10_scale = fake_min_h_10/34359738367 
print(fake_min_h_10_scale) # 3.5147546442317184e-05

fake_min_10 = (1/fake_min_h_10_scale)-1
print(fake_min_10) # 1049952.8080061115

fake_min_h_100 = find_min_hash_median(100,fake_seq)
print(fake_min_h_100) # 1316809.0

fake_min_h_100_scale = fake_min_h_100/34359738367 
print(fake_min_h_100_scale) # 3.832418588101643e-05

fake_min_100 = (1/fake_min_h_100_scale)-1
print(fake_min_100) # 1002734.6086791572

print(len(set(fake_subseq)))
# 999967

# From the results above, we can see that from a=100 is closest to the true distinct values of the subsequence in the fake dataset. 



# Find the minimal hash value on the entire sequence using different subsets

# Estimate min hash in a range of a = 1 
min_h_1 = find_min_hash_median(1,sequence)
print(min_h_1)
# 520

# Divided the min hash by scale to get the probability from 0 to 1
min_h1_scale = min_h_1/34359738367 
print(min_h1_scale)
# 1.5133991837941983e-08

# Find the minimal distinct value
min1 = (1/min_h1_scale)-1
print(min1)
# 66076418.93653846

# Estimate min hash in a range of a = 1 to 5:       
min_h_5 = find_min_hash_median(5,sequence)
print(min_h_5)
# 177

# Divided the min hash by scale to get the probability from 0 to 1
min_h_5_scale = min_h_5/34359738367 
print(min_h_5_scale)
# 5.15137799099179e-09

# Find the minimal distinct value
min5 = (1/min_h_5_scale)-1
print(min5)
# 194122814.63276836

# Estimate min hash in a range of a = 1 to 10: 
min_h_10 = find_min_hash_median(10,sequence)
print(min_h_10)
# 247.5

# Divided the min hash by scale to get the probability from 0 to 1
min_h_10_scale = min_h_10/34359738367 
print(min_h_10_scale)
# 7.203198038251232e-09

# Find the minimal distinct value 
min10 = (1/min_h_10_scale)-1
print(min10)
# 138827224.72525254

# Estimate min hash in a range of a = 1 to 100
min_h_100 = find_min_hash_median(100,sequence)
print(min_h_100) # 170.5

# Divided the min hash by scale to get the probability from 0 to 100
min_h_100_scale = min_h_100/34359738367 
print(min_h_100_scale) # 4.9622030930175156e-09

# Find the minimal distinct value 
min100 = (1/min_h_100_scale)-1
print(min100) # 201523391.1818182

# From the results above, we can see that from a=1-10 is closer to the true distinct values of the subsequence. 
