import pandas as pd
import time




def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"Time taken to load CSV file: {load_time} seconds")
        print("Number of rows loaded:", len(df))
        return df

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None


# Call load_csv to load the data and print the first 10 rows
csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
sales_data =  load_csv(csv_file)

# Check if the dataframe was loaded successfully before attempting to print the first 10 rows
if sales_data is not None:
    print(sales_data.head(10))
# describe the dataframe field data types
if sales_data is not None:
    print(sales_data.dtypes)