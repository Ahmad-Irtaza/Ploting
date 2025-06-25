import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.bar(['A', 'B', 'C'], [3, 5, 7])
plt.title("Plot 2")

plt.tight_layout()
plt.show()
