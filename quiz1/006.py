import matplotlib.pyplot as plt
import numpy as np
import random
height = np.random.normal(170,10,1000)
range_count = [0] * 2
labels = ['0~59', '60~100']
xIndex = [0, 1]
yIndex = np.arange(0, 10)
fig, axes = plt.subplots(nrows=2, ncols=1)
count = [0]*12
for h in height:
    try:
        index = (int(h) - 141) // 5
        count[index] += 1
    except IndexError:
        continue
print(count)
ticks = ['141-145', '146-150', '151-155', '156-160', '161-165', '166-170', '171-175', '176-180', '181-185', '186-190', '191-195', '196-200']
axes[0].plot(count)
axes[0].set(title="height line chart")
axes[0].set_xticks([0,1,2,3,4,5,6,7,8,9,10,11], ticks)

count = [0]*6
for h in height:
    try:
        index = (int(h) - 141) // 10
        count[index] += 1
    except IndexError:
        continue
print(count)
labels = ["141-150", "151-160", "161-170", "171-180", "181-190", "191-200"]
axes[1].pie(count, labels=labels)
axes[1].set(title="height pie chart")


plt.show()