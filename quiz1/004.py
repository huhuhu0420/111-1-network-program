import numpy as np

nf1 = np.genfromtxt('110goldpassbook.csv', delimiter=',', skip_header=1)
price = np.array(nf1[:, 3])
price2 = np.array(nf1[:, 4])

arr = nf1[price.argsort()]
i = 0
for a in arr:
    i += 1
    print(int(a[0]), int(a[3]), int(a[4]))
    if i == 5:
        break
print(np.median(price))
print(round(np.mean(price2), 2))
print(round(np.std(price2), 2))
# minweight = nf1[:, 1].min(axis=0)
# maxprice = nf1[:, 2].max(axis=0)
# print(minweight, maxprice)
# for temp in nf1:
#     if (temp[1] == minweight):
#         print(temp[0])
# for temp in nf1:
#     if (temp[2] == maxprice):
#         print(temp[0])
