#15. How to find numbers between 1 and 100 that are divided by 3 and 5 on Python?
for i in range(1,101):
    if i%3==0 or i%5==0 or i%2==0:
        print(i)