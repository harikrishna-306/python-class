try:
    print('one')
    print(10/0)
except:
    print('three')
finally:
     print('four')           #o/p is one three four  because of two line error automatically to execute three
                        # except block means to catch the above try block errors