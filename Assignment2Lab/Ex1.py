import pandas as pd

csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

try:
    df = pd.read_csv(csv_file, engine='pyarrow', on_bad_lines='skip')
    outfile = 'sales_data_test.csv'
    (df.head(10)).to_csv(outfile, index=False)
    print(f"First 10 rows of {csv_file} have been written to {outfile}.")
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")