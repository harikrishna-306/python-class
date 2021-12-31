#5. How to calculate the Entered Visa and Final Grade Average on Python?
visagrade = input('enter your visa grade : ')
finalgrade = input('enter your final grade : ')
average =(float(visagrade)*0.3)+(float(finalgrade)*0.7/2)
print("average :{0} ".format(average))