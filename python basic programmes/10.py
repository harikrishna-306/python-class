#11. How to show if the person whose age is entered can get a driver’s license on Python?
age = input('enter age : ')
if (int(age))<18:
    print("Your Age Is Not Eligible To Get A Driver's License")
else:
    print("Your Age Is Eligible To Get Your License")