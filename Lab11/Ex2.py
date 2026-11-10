# Create a dataframe from a CSV file and create a pivot table to aggregate sales by region and order type.
# Name: Coleman Lau
# Date: October 30, 2026

import pandas as pd
import numpy as np

# Tell Pandas to print all columns when displaying a DataFrame
pd.set_option('display.max_columns', None)

csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    # print(df.head())

    # Calculate sales total per row, for later use in the pivot table
    df['sales'] = df['quantity'] * df['unit_price']

    # Create a pivot table aggregating sales by region and order type
    pivot_table = pd.pivot_table(df, 
                                 values='sales',
                                 index='sales_region',
                                 columns='order_type',
                                 aggfunc=np.sum,
                                 margins=True,
                                 margins_name='Total Sales')

    print(pivot_table)

except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")

