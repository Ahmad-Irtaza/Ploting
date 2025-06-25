import matplotlib.pyplot as plt
labels = ['Shoes', 'Bags', 'Clothes']
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Category-wise Sales Distribution")
plt.show()
