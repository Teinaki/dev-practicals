# Create a lambda function called fahrenheit_to_celsius which converts its
# argument to celcius. Round the output to the nearest two demcial places
# using the round() function.

fahrenheit_to_celsius = lambda x: round((x-32) * 5 / 9 , 2)
print(fahrenheit_to_celsius(64.99))

# Expected output:
# 18.33
