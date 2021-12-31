class Bank:
    min_Bal = 500     # static variable
    def __init__(self,name):
        self.name =name      #instance 
       
        #print("Constructor executing automatically")
    def deposit(self, amount):
        self.amount =  amount # instace variable
        Bank.BranchName = "Marathahalli"
c1 = Bank("Rahul")
c2 = Bank("Priyanka")
c1.loc ="New Delhi"
c1.deposit(50000)     
print(c1.__dict__)     #o/p is {'name': 'Rahul', 'loc': 'New Delhi', 'amount': 50000}
print(c2.__dict__)    #o/p is {'name': 'Priyanka'}


print(Bank.min_Bal)      #500
print(Bank.BranchName)    #marathahalli
print(Bank.__dict__)     #{'__module__': '__main__', 'min_Bal': 500, '__init__': <function Bank.__init__ at 0x0454ED68>, 'deposit': <function Bank.deposit at 0x0454EDF8>, '__dict__': <attribute '__dict__' of 'Bank' objects>, '__weakref__': <attribute '__weakref__' of 'Bank' objects>, '__doc__': None, 'BranchName': 'Marathahalli'}