class Employee:
    def __init__(self,a,b):
        self.emp_id =a           #init is to iniliaze the values
        self.emp_name = b
    
    def getEmployeeDetails(self):   #self is to refer current object
        print(self.emp_name)
        print(self.emp_id)
e = Employee(101, "Rahul Gandhi")   #this is object and to invoke the function values
e.getEmployeeDetails()