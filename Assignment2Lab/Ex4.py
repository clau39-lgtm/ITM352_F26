import pandas as pd
import time
import sys


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


def exit_program(data):
    """Exit the application."""
    print("Exiting the program.")
    sys.exit(0)


def sales_by_region_order_type(data):
    """Display the number of unique employees in each sales region."""
    pivot_table = pd.pivot_table(
        data,
        values='employee_id',
        index='sales_region',
        aggfunc='nunique',
    )
    print(pivot_table)


def show_employees_by_region(data):
    sales_by_region_order_type(data)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    """Display available actions and return the user's selection."""
    print("\nMenu:")
    for number, (description, _) in enumerate(menu_options, start=1):
        print(f"{number}. {description}")
    return input("Select an option: ").strip()


def main():
    csv_file = 'https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    while True:
        selection = display_menu()
        try:
            option_number = int(selection)
        except ValueError:
            print(f"Invalid selection. Enter a number from 1 to {len(menu_options)}.")
            continue

        if not 1 <= option_number <= len(menu_options):
            print(f"Invalid selection. Enter a number from 1 to {len(menu_options)}.")
            continue

        _, action = menu_options[option_number - 1]
        action(sales_data)


if __name__ == "__main__":
    main()