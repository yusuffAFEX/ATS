try:
    num = float(input('Enter a number: '))
    if num > 0:
        print('The number is greater than zero')
    elif num < 0:
        print('It less than zero')
    else:
        print('It is zero')
   
except ValueError:
    print('Enter a number')
