print("*** running simple_value_estimator.py ***")
def estimate_home_value(size_in_sqft, number_of_bedrooms):

    # Assume all homes are worth at least £40,000
    value = 40000

    # Adjust the value estimate based on the size of the house
    value = value + (size_in_sqft * 95)

    # Adjust the value estimate based on the number of bedrooms
    value =value + (number_of_bedrooms * 12000)

    return value

# Estimate the value of our house:
# - 5 bedrooms
# - 3800 sq ft
# Actual value: $450,000

value = estimate_home_value(4500, 6)

print("Estimated valued:£"+value.__str__())
