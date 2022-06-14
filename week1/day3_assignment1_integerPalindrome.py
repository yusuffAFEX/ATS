# def palindrome(five_digit):
#     to_string = str(five_digit)
#     if len(to_string) > 5:
#         print('Invalid input, enter five digits')
#     else:
#         f = []
#         for i in to_string:
#             f.append(i)
#         d = f[::-1]
#         print(d==f)


    
# palindrome(55555)

def palindrome(five_digit: int) -> int:
    if five_digit > 9999 and five_digit < 100000:
        original_num = five_digit
        reversed_integer = 0
        while five_digit != 0:
            remainder = five_digit%10
            reversed_integer = reversed_integer * 10 + remainder
            five_digit = five_digit//10
        if original_num == reversed_integer:
            print(f'{original_num} is a palindrome')
        else:
            print(f'{original_num} is not a palindrome')
    else:
        print("Invalid input. Enter five digits")    

        

    
palindrome(22222)