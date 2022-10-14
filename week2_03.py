import numpy as np

nf1 = np.genfromtxt('pig.csv', delimiter=',', skip_header=1)
weight = np.array(nf1[:, 1])
price = np.array(nf1[:, 2])
arr1 = nf1[weight.argsort(), 0]
arr2 = nf1[price.argsort(), 0]
print(arr1[:5])
print(arr2[-1: -5: -1])
arr3 = weight.argsort()
print(arr3[:5])
