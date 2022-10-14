import numpy as np
import statistics

nf1 = np.genfromtxt('pig.csv', delimiter=',', skip_header=1)
weight = np.array(nf1[:, 1])
price = np.array(nf1[:, 2])
print(statistics.stdev(weight))
print(np.median(price))
print(np.percentile(weight, 75))
