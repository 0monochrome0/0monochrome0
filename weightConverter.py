#weight converter

weight = float(input('Enter Your Weight: '))
unit = input('Kilograms or Pounds? (K or L): ')

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f'Your Weight is: {round(weight, 1)} {unit}')
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f'Your Weight is: {round(weight, 1)} {unit}')
else:
    print(f'{unit} was Not Valid')
