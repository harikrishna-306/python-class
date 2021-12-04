try:
    x = int(input("Please Enter First Number:"))
    y = int(input("Please Enter Second Number:"))
    print(x/y)
except ZeroDivisionError:
    print("Please Enter proper value - except zero")      #to give 20/0 it will give  zero division error

except ValueError :                                 #to give point values and will output is enter only digits
    print("Enter only Digits")

