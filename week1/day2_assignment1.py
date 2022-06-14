username = "yusuff"
passphase = 12345

user = input('Enter your username: ')
password = int(input('Enter your password: '))

if user.lower() == username and password == passphase:
    print(f'Welcome {user}\nLogin Successful')
else:
    print('Login failed')