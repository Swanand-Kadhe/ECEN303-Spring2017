import numpy as np
import random
x=random.randint(1,0)
y=0
if (x>=0.5):
  y=1
else:
  y=0
numberTrials=[]
for i in range (0,10000):
  flipcoins=0
  counter=1
  while (flipcoins==0):
    flipcoins=random.randint(1,0)
    if flipcoins==0:
      counter=counter+1
  numberTrials.append(counter)
average=sum(numberTrials)/10000
print average
