import numpy as np

nf1 = np.genfromtxt('pig.csv', delimiter=',', skip_header=1)
minWeight = nf1[:, 1].min(axis=0)
maxPrice = nf1[:, 2].max(axis=0)
print(minWeight, maxPrice)
for temp in nf1:
    if (temp[1] == minWeight):
        print(temp[0])
for temp in nf1:
    if (temp[2] == maxPrice):
        print(temp[0])
