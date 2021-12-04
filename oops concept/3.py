class Employee:
    """ Test Employee class """
    def __init__(self):
        print("Constructor Executing")
        
    def getEmployee(self):
        print("getEmployee method()/function")
    

e = Employee()
e.getEmployee()
e1= Employee()    #e,e1 are same o/p is "__mai__.employee"
print(type(e))
print(type(e1))