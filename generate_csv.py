import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker and settings
fake = Faker()
num_rows = 1_000_000
np.random.seed(42)

# Generate reusable fake data for performance
salespeople = [fake.name() for _ in range(50)]
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys']
regions = ['North', 'South', 'East', 'West']

# Generate data
data = {
    "Sale_ID": np.arange(1, num_rows + 1),
    "Date": [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_rows)],
    "Customer_ID": np.random.randint(1000, 9999, num_rows),
    "Product_ID": np.random.randint(100, 999, num_rows),
    "Product_Name": [fake.word().capitalize() for _ in range(num_rows)],
    "Category": np.random.choice(categories, num_rows),
    "Quantity": np.random.randint(1, 10, num_rows),
    "Unit_Price": np.round(np.random.uniform(5.0, 500.0, num_rows), 2),
    "Region": np.random.choice(regions, num_rows),
    "Salesperson": np.random.choice(salespeople, num_rows)
}

# Create DataFrame and compute total price
df = pd.DataFrame(data)
df["Total_Price"] = df["Quantity"] * df["Unit_Price"]

# Save to CSV
df.to_csv("sample_sales_data_1M.csv", index=False)
print("CSV file 'sample_sales_data_1M.csv' has been created successfully.")