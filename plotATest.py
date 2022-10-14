import matplotlib.pyplot as plt
line_up, = plt.plot([0,3,5],[1,2,3], label='Line Up~')
line_down, = plt.plot([4,3,2,1], label='Line Down~')
plt.legend(handles=[line_up], loc=3)
plt.show()
