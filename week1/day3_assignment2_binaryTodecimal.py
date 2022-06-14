def binary_to_decimal(binary):
    i=  0
    decimal = 0
    while(binary != 0):
        remainder = binary%10
        decimal = decimal + remainder * pow(2, i)
        print(decimal)
        binary = binary//10
        i +=1
    print(decimal)


binary_to_decimal(101)