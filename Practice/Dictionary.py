# Simple Dictionary example with capital and population

country_capitals = {
    "Germany": {"capital": "Berlin", "population": 83294633},
    "France": {"capital": "Paris", "population": 68106885},
    "Italy": {"capital": "Rome", "population": 58870762},
}

print("Country data:", country_capitals)
print(country_capitals["Germany"]["capital"])
print(country_capitals["Germany"]["population"])

country_capitals["England"] = {"capital": "London", "population": 55977130}
print(country_capitals["England"]["capital"])
print(country_capitals["England"]["population"])

print("Germany" in country_capitals)
print("Spain" not in country_capitals)