import numpy as np
import matplotlib.pyplot as plt

duration = 1
f = 5
t = np.linspace(0, duration, 1000)
y_continuous = np.sin(2 * np.pi * f * t)

# sampling fs = 2f = 10
fs = 500
Ts = 1/fs

n = np.arange(fs *duration)
t_sampled = n * Ts
y_sampled = np.sin(2 * np.pi * f * t_sampled)


plt.subplot(2,1,1)
plt.plot(t, y_continuous)
# plt.show()
plt.subplot(2,1,2)
plt.stem(t_sampled, y_sampled)
plt.show()


