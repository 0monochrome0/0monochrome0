# username Login
# cant be longer than 9 characters
# cant contain Digits
# cant contain spaces


username = input('Enter a username: ')

if len(username) > 9:
    print('your username cant be more than 12 characters')
elif not username.isalpha():
    print('username cant contain Digits')
elif not username.find(' ') == -1:
    print('your username cant contain spaces')
else:
    print(f'Welcome {username}')