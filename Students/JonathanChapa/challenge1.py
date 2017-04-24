import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

countheads=0    #heads is defined as 1 in toss
counttails=0    #tails is defined as 0 in toss
flip=0
trials=0
num_trials=[]
bins=[1,2,3,4,5,6,7,8,9,10,11,12]


def coinflip(p=0.5):
    global countheads
    global counttails

    for i in range(1000):
        random_number= random.randint(0,1)
        print(random_number)
        if (random_number==1):
            countheads+=1
        else:
            counttails+=1

def flipUntil():
    global flip
    global trials
    global num_trials
    for i in range(10000):
        trials=0
        while flip != 1:
            flip=random.randint(0,1)
            trials+=1
        flip=0
        num_trials.append(trials)





coinflip()
flipUntil()
empirical_probheads=float(countheads)/1000
empirical_probtails=float(counttails)/1000


plt.hist(num_trials,bins, histtype='bar', rwidth=1)
plt.xlabel('# of Trials before first heads')
plt.ylabel('Frequency of # of Trials')
plt.title('Number or Trials Before First Heads')
plt.show()

print(countheads)
print(counttails)
print(float(empirical_probheads))
print(float(empirical_probtails))
print(flip)
print(trials)
print(num_trials)
