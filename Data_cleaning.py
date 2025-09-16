import pandas as pd 
import numpy as np 

# Load files

orders = pd.read_csv('order_details_table.csv')
delivery_person = pd.read_csv('delivery_person_table.csv')

# Standardize column names

orders.columns = orders.columns.str.strip().str.lower().str.replace(' ','_')
delivery_person.columns = delivery_person.columns.str.strip().str.lower().str.replace(' ','_')

print(orders.describe())
print(delivery_person.describe())

#  Handle missing values In Tables

print('orders-\n' ,orders.isnull().sum())
print('delivery_person-\n' ,delivery_person.isnull().sum())

# Fill missing ratings with mean

delivery_person['delivery_person_ratings'] = pd.to_numeric(delivery_person[
    'delivery_person_ratings'] , errors= 'coerce')

delivery_person['delivery_person_ratings'] = delivery_person['delivery_person_ratings'].fillna(
    delivery_person['delivery_person_ratings'].mean())

# Fill missing ages with median

delivery_person['delivery_person_age']= pd.to_numeric(delivery_person['delivery_person_age'], errors= 'coerce')

delivery_person['delivery_person_age']= delivery_person['delivery_person_age'].fillna(
    delivery_person['delivery_person_age'].median())


# Handle Duplicates

print('orders-\n' ,orders.duplicated().sum())
print('delivery_person-\n' ,delivery_person.duplicated().sum())

# No Duplicates

# Clean Time_takenmin column

orders['time_taken(min)'] = orders['time_taken(min)'].str.replace(r'\(min\)\s*', '', regex=True)

# # Convert to numeric

orders['time_taken(min)'] = pd.to_numeric(orders['time_taken(min)'], errors='coerce')

print(orders['time_taken(min)'].dtype)

orders['order_date'] = pd.to_datetime(orders['order_date'], format='%d-%m-%Y')


# to save

orders.to_csv("cleaned_orders.csv", index=False)
delivery_person.to_csv("cleaned_delivery_person.csv", index=False)



from sqlalchemy import create_engine

# Replace with your database details
user = "root"
password = "****"
host = "localhost"
database = "supply_chain_analysis"

# Create connection engine
engine = create_engine(f"mysql+pymysql://{'root'}:{'*****'}@{'localhost'}/{'supply_chain_analysis'}")

# Save orders table to SQL
orders.to_sql("orders", engine, index=False, if_exists="replace")


# Save delivery_person table
delivery_person.to_sql("delivery_person", engine, index=False, if_exists="replace")

print("✅ Data successfully uploaded to SQL database!")


