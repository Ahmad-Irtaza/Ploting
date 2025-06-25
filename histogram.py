import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(10, 80, 50)
plt.hist(ages, bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
