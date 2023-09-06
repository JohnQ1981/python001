import matplotlib.pyplot as plt

# Data
x = ['Apple', 'Banana', 'Orange', 'Grapes', 'Cherry']
y = [5, 3, 6, 2, 4]

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(x, y, color='blue')

# Add labels and title
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Quantity of Fruits')

# Show grid lines for better readability
plt.grid(True)

# Display the chart
plt.show()
