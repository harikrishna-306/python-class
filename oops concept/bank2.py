class Bank:
    def __init__(self):
        print("Constructor method")
    
    def m1(self):
        print("Instance Method")    #instance level using self
    
    @classmethod
    def m2(cls):
        print("class method")        #class is decorator is confirm @ symbol and instance and static are optional
    @staticmethod
    def m3():
        print("static method")
        
c1 = Bank()     #Constructor method
c1.m1()          #instance Method
c1.m2()          #class Method
Bank.m2()        #class method

c1.m3()          #static method
Bank.m3()        #static method