import matplotlib.pyplot as plt
import numpy as np


# logistic map
def logistic_function(r, x):
    return r * x * (1 - x)


r = np.linspace(0, 4, 1000)
iterations = 50

x = np.random.rand(len(r))

plt.figure(figsize=(10, 6))
for i in range(iterations):
    x = logistic_function(r, x)
    plt.plot(r, x, ',k', alpha=1)

plt.title("Bifurcation diagram of the logistic map")
plt.xlabel("r")
plt.ylabel("x")
plt.show()
