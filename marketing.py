import pandas as pd
import numpy as np
import random

# Sample realistic marketing campaign names, locations, and products
campaign_names = [
    "Spring Sale", "Winter Clearance", "Summer Discount Blast", "Holiday Specials", 
    "Back to School", "Black Friday", "Cyber Monday", "New Year Deals", 
    "Anniversary Celebration", "Mega Savings", "Limited Time Offer", "Exclusive Launch"
]

countries = ["USA", "Canada", "UK", "Australia", "Germany", "India", "Japan", "Brazil", "South Africa", "France"]
cities = {
    "USA": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"],
    "UK": ["London", "Manchester", "Birmingham", "Leeds", "Glasgow"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
    "Germany": ["Berlin", "Munich", "Frankfurt", "Hamburg", "Stuttgart"],
    "India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"],
    "Japan": ["Tokyo", "Osaka", "Kyoto", "Nagoya", "Sapporo"],
    "Brazil": ["Sao Paulo", "Rio de Janeiro", "Brasilia", "Salvador", "Fortaleza"],
    "South Africa": ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse", "Nice"]
}

products = [
    "Electronics", "Clothing", "Home Appliances", "Books", "Toys", 
    "Beauty Products", "Sports Equipment", "Furniture", "Groceries", "Automotive"
]

# Generate dataset
data = {
    'Campaign_ID': [f'CAMP{i:05d}' for i in range(1, 100001)],
    'Campaign_Name': [random.choice(campaign_names) for _ in range(100000)],
    'Country': [random.choice(countries) for _ in range(100000)],
    'City': [],
    'Product': [random.choice(products) for _ in range(100000)],
    'Start_Date': [pd.Timestamp('2022-01-01') + pd.to_timedelta(random.randint(0, 1095), unit='D') for _ in range(100000)],
    'End_Date': [],
    'Budget': np.random.randint(10000, 50000, size=100000),
    'Spend': np.random.randint(5000, 45000, size=100000),
    'Revenue': np.random.randint(10000, 60000, size=100000),
    'Leads_Generated': np.random.randint(100, 1000, size=100000),
    'Conversions': np.random.randint(10, 300, size=100000),
    'Channel': np.random.choice(['Email', 'Social Media', 'TV', 'Radio', 'Billboard'], size=100000),
}

# Add city and end date based on start date
data['City'] = [random.choice(cities[country]) for country in data['Country']]
data['End_Date'] = [start_date + pd.to_timedelta(random.randint(1, 30), unit='D') for start_date in data['Start_Date']]

df = pd.DataFrame(data)

# Save the dataset
file_path = r'C:\\Users\\ronal\\Downloads\\Ronald Analytics\\marketing_campaign_dataset.csv'
df.to_csv(file_path, index=False)

print(f"Dataset saved to {file_path}")
