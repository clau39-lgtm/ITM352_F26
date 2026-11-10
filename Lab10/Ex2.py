# Create a Pandas DataFrame from individual lists.
# Do some simple stats on the data

import pandas as pd

# list of individuals' names, ages, and genders.
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

raw_data = zip(ages, gender)

# Create a DataFrame from the lists
df = pd.DataFrame(raw_data, index=names, columns=["Age", "Gender"])

summary = df.describe()
print(summary)

# Calculate average by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()
print(average_age_by_gender)