# compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input('Enter the Principle amount: '))
    if principle <= 0:
        print('principle cant be less than zero')
    else:
        break

while True:
    rate = float(input('Enter the interest rate amount: '))
    if rate <= 0:
        print('interest rate cant be less zero')
    else:
        break

while True:
    time = int(input('Enter the time in years: '))
    if time <= 0:
        print('time cant be less than zero')
    else:
        break

total = principle * pow((1+ rate / 100), time)

print(f'Balance after {time} year/s: ${total:.2f}')
