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


def display_initial_rows(data):
    """Prompt for and display a requested number of initial DataFrame rows."""
    try:
        row_count = int(input("How many initial rows would you like to see? "))
        if row_count < 0:
            print("Please enter a non-negative whole number.")
            return
    except ValueError:
        print("Invalid input. Please enter a non-negative whole number.")
        return

    print(data.head(row_count))
    return


def main():
    csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    print(sales_data.dtypes)
    while True:
        display_initial_rows(sales_data)


if __name__ == "__main__":
    main()