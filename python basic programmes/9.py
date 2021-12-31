#9. How to find out if the entered number is Positive, Negative, or 0 on Python?
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")