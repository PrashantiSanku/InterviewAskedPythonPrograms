'''
Arctic Temperatures: Fun with Python Built-in Math Functions
Exercise 1: Analyzing Antarctic Temperatures
Instructions:
Begin with the antarctic_temperatures list, which contains the daily temperature recordings.
Apply the max() function to the antarctic_temperatures list to obtain the highest temperature recorded.
Apply the min() function on the antarctic_temperatures list to determine the lowest temperature recorded.
Print the highest and lowest temperatures.
Calculate the average temperature by summing all temperatures in the antarctic_temperatures list using the sum() function and dividing by the number of temperatures, which you can determine using the len() function. Round the calculated average temperature to one decimal place using the round() function.
Print the rounded average temperature.
Calculate the absolute value of the coldest temperature using the abs() function.
Print the absolute value of the coldest temperature.
'''

antarctic_temperatures = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

# Find the highest and lowest temperatures
highest_temp = max(antarctic_temperatures)
lowest_temp = min(antarctic_temperatures)

print("Highest temperature:", highest_temp, "°C")
print("Lowest temperature:", lowest_temp, "°C")

# Calculate the average temperature
average_temp = sum(antarctic_temperatures)/len(antarctic_temperatures)
average_temp = round(average_temp, 1)
print("Average temperature:", average_temp, "°C")

# Find the absolute value of the coldest temperature
coldest_temp_abs = abs(lowest_temp)
 ### Insert code here
print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")