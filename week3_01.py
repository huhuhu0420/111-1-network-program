import matplotlib.pyplot as plt
import numpy as np
import random

n = 10
scores = [random.randint(0, 100) for i in range(n)]
print(scores)
range_count = [0] * 2
labels = ['0~59', '60~100']
xIndex = [0, 1]
yIndex = np.arange(0, 10)
fig, axes = plt.subplots(nrows=2, ncols=2)

for score in scores:
    if score < 60:
        range_count[0] += 1;
    elif score >= 60:
        range_count[1] += 1;
axes[0, 0].bar(labels, range_count, width=0.5)
axes[0, 0].set(xticks=xIndex, yticks=yIndex, title = 'bar')
axes[0, 0].set_xlabel('score')
axes[0, 0].set_ylabel('count')
axes[0, 0].legend(['count'])

range_count2 = [0] * 21
for score in scores:
    index = int(score / 5)
    range_count2[index] += 1
print(range_count2)
axes[0, 1].plot([i for i in range(0, 101, 5)], range_count2)
axes[0, 1].set(title="plot", xticks=[i for i in range(0, 101, 5)], yticks=[i for i in range(0, 10, 1)])
axes[0, 1].legend(['count'])

range_count3 = [0] * 11
for score in scores:
    index = int(score / 10)
    range_count3[index] += 1
print(range_count3)
axes[1, 0].scatter(np.arange(0, 110, 10), range_count3, marker='3', c='red')
axes[1, 0].set(title="scatter", xticks=[i for i in range(0, 101, 10)], yticks=[i for i in range(0, 10, 1)])
axes[1, 0].legend(['count'])

range_count4 = [0] * 3
for score in scores:
    if 0 < score <= 59:
        range_count4[0] += 1
    elif 60 < score <= 80:
        range_count4[1] += 1
    elif 81 < score <= 100:
        range_count4[2] += 1
labels = ['0~59', '60~80', '81~100']
axes[1, 1].pie(range_count4, labels=labels)
axes[1, 1].set(title="pie")

plt.show()
