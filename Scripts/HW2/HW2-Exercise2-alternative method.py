# Alternative method -- multiprocessing to speed up the process
from Bio import SeqIO
human_genome = SeqIO.parse("GCA_000001405.28_GRCh38.p13_genomic.fna", "fasta")
for chromosome in human_genome:
    if chromosome.name == "CM000664.2":
        sequence = str(chromosome.seq).lower().encode('utf8')

p = 2_549_536_629_329
bits_48 = 2 ** 48 - 1
scale = 0x07ffffffff
from hashlib import sha256
import statistics
import multiprocessing as mp

def quick_min_hash(q,progress,a,range_l,range_r):
    # Set a min_list that has the largest hash values. Therefore, any hash value found later will be smaller than this list of values.
    min_list=[scale]*a
    # For each range of task (individual task distributed for each worker[explained in the loaddist function]), store the integer hash value of the entire sequence using sha256 function and take the reminder of bits_48 into a variable s256.
    for i in range(range_l,range_r):
        s256=int(sha256(sequence[i:i+15]).hexdigest(),16) % bits_48
        # Enumerate the min hash value list from index 1    
        for j,minval in enumerate(min_list,start=1):
            # Store the last couple digits of scale after multipling s256 with any index inside my min_list in a variable t. 
            t=((s256*j)%p)&scale
            # Compare t if t is smaller than the hash value in min_list. If yes, store the new hash value as t. 
            if t<min_list[j-1]:
                min_list[j-1]=t
        # Calculate the percentages of the progress after completing every 100,000 subsequences.
        if (i-range_l+1)%100000==0:
            progress.put(100000)
    progress.put((range_r-range_l)%100000)
    q.put(min_list) # Put the list of min hash value into the queue.

def loaddist(size,worker,start=0):
    # Evenly distribute the entire task for each worker.
    distrib=[size//worker]*worker
    # The size of the entire task (going through the 100 hash families) 
    # divided by my total workers will not be an interger (my computer has 8 cores 16 threads).
    # Thus, whatever left-off after division(remainders) will again evenly distributed to each worker.
    for i in range(size%worker):
        distrib[i]+=1
    i=start
    result=[]
    for size in distrib:
        result.append((i,i+size))
        i+=size
    return result

def find_min_hash(a,seq):
    min_list=[scale]*a
    proc_list=[]
    queue_list=[]
    
    # Evenly distribute the task of loading all 15-mer subsequences to 16 workers.
    range_list=loaddist(len(seq)-14,16)
    print(range_list)
    
    # Store the queuing process in a progress bar.
    progbar=mp.Queue()

    for l,r in range_list:
        
        q=mp.Queue()
        # l=range_l, r=range_r
        p=mp.Process(target=quick_min_hash,args=(q,progbar,a,l,r))
        # Start the process 
        p.start()
        # Store results in the process and queue lists
        proc_list.append(p)
        queue_list.append(q)

    for i,p in enumerate(proc_list):    
    # Get the results by queuing each worker while looping through the process lsit
        for i,newval in enumerate(queue_list[i].get()):
            # Compare the new hash values with the original hash values in the min_list, storing the new min hash values
            if newval<min_list[i]:
                min_list[i]=newval
        # End the process by joining the results from all workers 
        p.join()
    return min_list

test = sequence[0:1000000]

# Find min hash for all 100 families in the first 100000 sequence:
min_h_test = find_min_hash(100,test)
print(min_h_test)
# [(0, 62500), (62500, 125000), (125000, 187499), (187499, 249998), (249998, 312497), (312497, 374996), 
# (374996, 437495), (437495, 499994), (499994, 562493), (562493, 624992), (624992, 687491), (687491, 749990), 
# (749990, 812489), (812489, 874988), (874988, 937487), (937487, 999986)]
# [37244, 26109, 20952, 36744, 42444, 15290, 31901, 22983, 26339, 72141, 2028, 24467, 36206, 58686, 50169, 25515, 
# 12867, 42114, 1559, 3799, 1471, 54522, 46895, 33867, 3677, 73007, 43458, 27537, 4859, 3217, 10678, 51030, 111119, 
# 35998, 14712, 123780, 9272, 19531, 62113, 7598, 70540, 2529, 35844, 77322, 4051, 93790, 23204, 7648, 47349, 49364, 
# 10537, 64677, 4202, 168448, 6641, 16769, 14479, 76560, 89466, 11397, 2187, 21356, 4413, 13509, 12072, 4256, 13087, 
# 1971, 28256, 29424, 93507, 31653, 71582, 9634, 11909, 27275, 8949, 134359, 8762, 15196, 43556, 9337, 40325, 5058, 508, 
# 38921, 15275, 12835, 9440, 22994, 22486, 90289, 1612, 19513, 39341, 15296, 80692, 29681, 27356, 5305]

min_h_test_median = statistics.median(min_h_test)
print(min_h_test_median)  # 23099.0
min_h_test_median_scale = min_h_test_median/34359738367 
print(min_h_test_median_scale) # 6.722693797396574e-07
min_test = (1/min_h_test_median_scale)-1
print(min_test) # 1487497.9552361574

# Find the median for the first 10
min_h10_test_median = statistics.median(min_h_test[:10])
print(min_h10_test_median) # 29120.0
min_h10_test_median_scale = min_h10_test_median/34359738367 
print(min_h10_test_median_scale) # 8.47503542924751e-07
min_10_test = (1/min_h10_test_median_scale)-1
print(min_10_test) # 1179935.0702953297

test_sub=[test[i:i+15] for i in range(len(test)-14)]
print(len(set(test_sub)))
# 931157 


# Find min hash for all 100 families in the entire sequence:
min_h = find_min_hash(100,sequence)
print(min_h)

# [(0, 15137095), (15137095, 30274190), (30274190, 45411285), (45411285, 60548380), 
# (60548380, 75685475), (75685475, 90822570), (90822570, 105959665), (105959665, 121096760), 
# (121096760, 136233855), (136233855, 151370950), (151370950, 166508045), (166508045, 181645139), 
# (181645139, 196782233), (196782233, 211919327), (211919327, 227056421), (227056421, 242193515)]
# [520, 177, 28, 354, 64, 318, 607, 63, 25, 417, 913, 444, 300, 46, 78, 126, 910, 124, 83, 29, 94, 
# 699, 227, 131, 170, 82, 88, 123, 230, 98, 893, 252, 629, 231, 267, 237, 28, 585, 85, 58, 65, 124, 165, 96, 
# 447, 297, 204, 38, 121, 340, 110, 303, 41, 34, 3, 245, 32, 650, 14, 87, 315, 324, 100, 884, 704, 593, 14, 87, 51, 287, 507, 393, 
# 836, 56, 459, 453, 274, 170, 243, 116, 241, 778, 340, 171, 58, 168, 105, 433, 40, 39, 4, 134, 180, 408, 494, 76, 368, 129, 319, 80]

min_100_median = statistics.median(min_h)
print(min_100_median) # 170.5

min_100_median_scale = min_100_median/34359738367 
print(min_100_median_scale) # 4.9622030930175156e-09
min_100 = (1/min_100_median_scale)-1
min_100 # 201523391.1818182

min_5_hash = min_h[:5]
min_5_median = statistics.median(min_5_hash)
print(min_5_median) # 177

min_5_median_scale = min_5_median/34359738367 
print(min_5_median_scale) # 5.15137799099179e-09
min_5 = (1/min_5_median_scale)-1
print(min_5) # 194122814.63276836

min_10_hash = min_h[:10]
min_10_median = statistics.median(min_10_hash)
print(min_10_median) # 247.5

min_10_median_scale = min_10_median/34359738367 
print(min_10_median_scale) # 7.203198038251232e-09
min_10 = (1/min_10_median_scale)-1
print(min_10) # 138827224.72525254

# Check the result of the function 

subseq=[sequence[i:i+15] for i in range(len(sequence)-14)]
print(len(set(subseq)))
# 145003145