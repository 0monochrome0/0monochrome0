unit = input('Is this temperature in Celsius or Fahrenheit (C/F): ')
temp = float(input('Enter the Temperature: '))

if unit == 'C':
    temp = round((9*temp)/5+32,1)
    print(f'The temprature in Fehrenheit is: {temp}*F')
elif unit == 'F':
    celsius = round((temp - 32)* 5/9,1)
    print(f'The temprature in Celsius is: {temp} *C')
else:
    print(f'{unit} is a invaid unit of measurement')
