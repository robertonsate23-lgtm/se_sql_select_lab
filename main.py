import sqlite3
import pandas as pd

# STEP 1: Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2: Select employeeNumber and lastName
df_first_five = pd.read_sql("SELECT employeeNumber, lastName FROM employees", conn)

# STEP 3: Select lastName and employeeNumber
df_five_reverse = pd.read_sql("SELECT lastName, employeeNumber FROM employees", conn)

# STEP 4: Select with Alias
df_alias = pd.read_sql("SELECT employeeNumber AS ID, lastName FROM employees", conn)

# STEP 5: CASE Function
query_executive = """
SELECT *,
CASE
    WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
    ELSE 'Not Executive'
END AS role
FROM employees
"""
df_executive = pd.read_sql(query_executive, conn)

# STEP 6: Built-in Strings (Length)
df_name_length = pd.read_sql("SELECT LENGTH(lastName) AS name_length FROM employees", conn)

# STEP 7: Built-in Strings (Substring)
df_short_title = pd.read_sql("SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees", conn)

# STEP 8: Built-in Numerics (Sum and Round)
query_total = "SELECT SUM(ROUND(priceEach * quantityOrdered)) AS sum_total_price FROM orderDetails"
sum_total_price = pd.read_sql(query_total, conn)

# STEP 9: Dates
# Assuming the table is 'orders' which contains orderDate
query_dates = """
SELECT orderDate,
       strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM orders
"""
df_day_month_year = pd.read_sql(query_dates, conn)

# Close the connection
conn.close()