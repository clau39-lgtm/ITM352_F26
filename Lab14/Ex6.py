from io import StringIO

import pandas as pd
import requests

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

response = requests.get(url)

int_rate_table = pd.read_html(StringIO(response.text))[0]

# Converts the table to a string and prints out everything in the table. Also formatted the float values to 3 decimal places as it was shown in the website.
print(int_rate_table.to_string(index=False, float_format=lambda value: f"{value:.3f}"))
