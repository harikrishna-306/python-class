class Bank:
    
    def info():
        print("Just Testing")     # this is class inside of function level to call the bank.info()


Bank.info()

class Bank:
    min_Bal = 500                  #his is class inside of property level to call the c1=bank()
    

c1 = Bank()
print(c1.__dict__)    # {}  - no instance variable
print(Bank.__dict__)  # displaying Bank Class info as dict format