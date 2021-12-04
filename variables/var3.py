class Employee:
    
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
        

e1 = Employee()
e1.setName("Rahul Gandhi")
print(e1.getName())                # this output is Rahul Gandhi
print(e1.__dict__)                 #this format is key value pair output {'name': 'Rahul Gandhi'}