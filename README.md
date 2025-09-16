 # 🏬 E-Commerce Supply Chain Analysis

This project is an **end-to-end data analysis pipeline** where I analyzed 45K+ e-commerce orders to uncover insights about delivery performance, order trends, and factors impacting efficiency.  
I built this project to practice real-world **data cleaning, SQL analysis, and dashboard design** — just like a data analyst would do in a company.

---

## 📊 Project Overview

The goal was to explore:
- How traffic, weather, and festival days affect delivery time
- Which cities and vehicle types handle the most orders
- Trends in demand over time
- Rider performance through ratings and delivery speed

---

## 🛠 Tech Stack

- **Python** – Pandas, NumPy (data cleaning & preprocessing)
- **MySQL** – SQL queries for aggregations and joins
- **Power BI** – Interactive dashboard for visualization

---

## 🔧 Data Preparation

- Cleaned and standardized columns  
- Converted `time_taken(min)` to numeric values  
- Filled missing data (ratings, age, city) where appropriate  
- Removed duplicates and validated data quality  
- Saved final dataset into CSV and loaded it into MySQL for analysis

---

## 📑 SQL Analysis

Some of the questions I solved with SQL:
- Total orders and city-wise distribution  
- Average delivery time by city, traffic density, and weather  
- Festival impact on delivery times  
- Orders by type of order and type of vehicle  
- Driver ratings and age distribution  
- Pickup delay (time between order placed and picked)

---

## 📈 Power BI Dashboard

The dashboard includes:
- **KPIs:** Total Orders, Avg Delivery Time, Avg Pickup Delay, Avg Driver Rating  
- **Charts:**  
  - Orders by City, Traffic Density, Weather, Festival  
  - Avg Delivery Time by Vehicle, City  
  - Orders over Time (trend analysis)
- **Slicers:** City, Month, Traffic Condition, Vehicle Type  

---

## 🔑 Key Insights

- Semi-Urban deliveries have the highest average delivery time (~50 mins)  
- Traffic jams add ~15 minutes to average delivery time  
- March shows peak demand compared to other months  
- Motorcycles are the fastest and handle most deliveries   

---

## 🚀 How to Run This Project

1. Clone this repository
2. Open `Data_cleaning.py` to see the Python data cleaning steps
3. Run SQL scripts from `sql_query.sql` to explore data
4. Open `E-commerce_suply_chain_analysis.pbix` in Power BI to view the dashboard

---

## 🎯 Learning & Takeaways

This project helped me:
- Practice **data cleaning** and building a reproducible ETL process
- Write **SQL queries** to answer real business questions
- Build a professional, interactive **Power BI dashboard**
- Translate data into **business insights** that could improve operations

---
