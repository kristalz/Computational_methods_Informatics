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

def find_min_hash(a):
    min_list=[scale]*a
    proc_list=[]
    queue_list=[]
    
    # Evenly distribute the task of loading all 15-mer subsequences to 16 workers.
    range_list=loaddist(len(sequence)-14,16)
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

# Find min hash for all 100 families:
min_h = find_min_hash(100)
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
min_100_median # 170.5
min_100_median_scale = min_100_median/34359738367 
min_100_median_scale # 4.9622030930175156e-09
min_100 = (1/min_100_median_scale)-1
min_100 # 201523391.1818182

min_5_hash = min_h[:5]
min_5_median = statistics.median(min_5_hash)
min_5_median # 177

min_5_median_scale = min_5_median/34359738367 
min_5_median_scale # 5.15137799099179e-09
min_5 = (1/min_5_median_scale)-1
min_5 # 194122814.63276836

min_10_hash = min_h[:10]
min_10_median = statistics.median(min_10_hash)
min_10_median # 247.5

min_10_median_scale = min_10_median/34359738367 
min_10_median_scale # 7.203198038251232e-09
min_10 = (1/min_10_median_scale)-1
min_10 # 138827224.72525254

min_50_hash = min_h[:50]
min_50_median = statistics.median(min_50_hash)
min_50_median # 167.5

min_50_median_scale = min_50_median/34359738367 
min_50_median_scale # 4.874891601644773e-09
min_50 = (1/min_50_median_scale)-1
min_50 # 205132765.37014925