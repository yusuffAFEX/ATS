# 2. Census program that stores firstname, lastname, middle name, age, gender, dob, occupation, marital status, email
# a. validates input
# b. saves in a csv file
# c. Ability to search by taking a search term and return matches

# 3. A signup and sign-in program that take basic info:
# On signup - username, first name, lastname, password and confirm password and saves it in a csv file.
# On signin, it takes username and password and return whether a message saying login successful or invalid login credentials. Add validation. Password must be minimum of 8 characters.

# 4. Modify (3) to include:
# a. After successful signup, it should prompt the user to signin.
# b. After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
# c. Edit profile should ask for more information like phone_number (required), address (optional), date of birth (optional) and gender (compulsory)


import csv
from re import A


# def program():
#     firstname = input('Enter your firstname: ')
#     lastname = input('Enter your lastname: ')
#     gender = input('Enter gender: ')
#     dob = input('Enter DOB: ')
#     occupation = input('Enter occupation: ')
#     marital_status = input('Enter Marital status: ')
#     email = input('Enter email: ')

#     try:
#         age = int(input('Enter your Age: '))
#     except ValueError:
#         return 'Age must be int not string'

#     filenames = ['firstname', 'lastname', 'gender', 'dob', 'occupation', 'marital_status', 'email', 'age']

#     def read_file():
#         l = []
#         with open('file.csv', 'r') as file:
#             u = csv.DictReader(file)
#             for i in u:
#                 l.append(i)
#             return l

#     with open('file.csv', 'a+', newline='') as f:
#         w = csv.DictWriter(f, filenames)
#         if len(read_file()) > 0:
#             w.writerow(
#                 {'firstname': firstname, 'lastname': lastname, 'gender': gender, 'dob': dob, 'occupation': occupation,
#                  'marital_status': marital_status, 'email': email, 'age': age})
#         else:
#             w.writeheader()
#             w.writerow(
#                 {'firstname': firstname, 'lastname': lastname, 'gender': gender, 'dob': dob, 'occupation': occupation,
#                  'marital_status': marital_status, 'email': email, 'age': age})

#         # if f.readlines() not in f:
#         #     w.writeheader()


# # print(program())

# def search(firstname):
#     with open('file.csv', 'r') as s:
#         y = []
#         for i in s.readlines():
#             y.append(i.split(','))
#         for j in y:
#             if j[0] == firstname:
#                 return ','.join(j)
        


# print(search('quadri'))

def read_file():
            c = []
            with open('f.csv', 'r') as k:
                p = csv.DictReader(k)
                for i in p:
                    c.append(i)
                return c
def edit_profile():
    phone_number = input('Enter your phone number: ')
    if not phone_number:
        print('Phone number is required.')
    else:
        address = input('Enter your address: ')
        dob = input('Enter your date of birth: ')
        gender = input('Ender your gender: ')
        if not gender:
            print('Gender is required')
            sign_in()

    

def change_password():
    new_password = input('Enter new password: ')
    g = read_file()
    pass

    

def sign_in():
    userName = input('Enter username: ')
    passWord = input('Enter password: ')

    n = read_file()
    for x in n:
        if x['username'] == userName and x['password1'] == passWord:
            print(f'Login Successful..\nWelcome '+ x['username'])
            v = input('Enter E to edit your profile.\nEnter C to change your password.\nPress L to logout. ')
            if v == 'E'.lower():
                return edit_profile()
            elif v == 'C'.lower():
                new_password = input('Enter new password: ')
                if len(new_password)<8:
                    print('The password must be 8 character..')
                else:
                    filenames = ['username', 'firstname', 'lastname', 'password1', 'password2']
                    with open('f.csv', 'w', newline='') as h:
                        q = csv.DictWriter(h, filenames)
                        q.writeheader()
                        for c in n:
                            if c['username'] == userName:
                                q.writerow({'username':c['username'], 'firstname':c['firstname'], 'lastname':c['lastname'], 'password1': new_password, 'password2': new_password})
                                continue
                            q.writerow({'username':c['username'], 'firstname':c['firstname'], 'lastname':c['lastname'], 'password1': c['password1'], 'password2': c['password2']})

                    exit()                                                                                                                                                                                                 
            elif v == 'L'.lower():
                exit()
    print('Invalid credential details')
    sign_in()
print(sign_in())

        
def sign_up():
    username = input('Enter your username: ')
    firstname = input('Enter your firstname: ')
    lastname = input('Enter your lastname: ')
    password1 = input('Enter your password: ')

    if len(password1) < 8:
        print('The password must be minimum of 8 character')
    else:
        password2 = input('Confirm the password: ')

        if password1 != password2:
            return 'Both password must be equal'

        filenames = ['username', 'firstname', 'lastname', 'password1', 'password2']

        with open('f.csv', 'a+', newline='') as z:
            w = csv.DictWriter(z, filenames)
            if len(read_file()) > 0:
                w.writerow(
                    {'username': username, 'firstname': firstname, 'lastname': lastname, 'password1': password1,
                    'password2': password2})
            else:
                w.writeheader()
                w.writerow(
                    {'username': username, 'firstname': firstname, 'lastname': lastname, 'password1': password1,
                    'password2': password2})
    print('SignUp Successful..')
    # sign_in()
# print(sign_up())



            

def fibonacci(num):
    a,b = 0, 1
    c=0
    while c<=num:
        print(a,b)
        a,b=b, a+b
        c+=1

# fibonacci(5)






    




