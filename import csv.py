import csv
from faker import Faker
import pandas as pd

# Initialize Faker
fake = Faker()

# Function to generate fake data
def generate_fake_data(num_rows):
    data = []
    for _ in range(num_rows):
        name = fake.name()
        address = fake.address()
        email = fake.email()
        data.append([name, address, email])
    return data

# Ask the user how many rows they want
num_rows = int(input("Enter the number of rows you want to generate (up to 500): "))
if num_rows > 500:
    print("The maximum number of rows is 500.")
    num_rows = 500

# Generate the fake data
data = generate_fake_data(num_rows)

# Create a DataFrame
df = pd.DataFrame(data, columns=["Name", "Address", "Email"])

# Save the DataFrame to a CSV file
df.to_csv("fake_data.csv", index=False)

print(f"{num_rows} rows of fake data have been generated and saved to 'fake_data.csv'.")
