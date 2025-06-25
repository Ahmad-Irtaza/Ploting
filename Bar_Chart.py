import matplotlib.pyplot as plt

products = ['A', 'B', 'C']
sales = [100, 200, 150]

plt.bar(products, sales)
plt.title("Product Sales")
plt.ylabel("Units Sold")
plt.show()
