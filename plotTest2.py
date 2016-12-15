import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y = np.arange(6)
#
# plt.ion()
# hl, = plt.plot(x, y)
#
# for i in range(5):
#     x = x*1.5
#     hl.set_xdata(x)
#     print("step", i)
#     plt.pause(0.5)

# plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    # y = np.random.random()
    plt.plot(x*i, y)
    plt.pause(0.5)

# while True:
#     plt.pause(0.05)