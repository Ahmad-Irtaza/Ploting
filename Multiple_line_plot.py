import matplotlib.pyplot as plt
months = [1, 2, 3, 4]
store1 = [100, 150, 200, 250]
store2 = [90, 160, 190, 230]
store3 = [120, 126, 190, 230]
plt.plot(months, store1, label='Store 1')
plt.plot(months, store2, label='Store 2')
plt.plot(months, store3, label='Store 3')

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()
