class Test:
    staticmethod
    def add(self,a,b):
        print("Addition", a+b)     #@ decorator is removed to static method will result is error so when we are placed in self keyword then will come result
        
    staticmethod
    def multi(self,a,b):
        print("Multiplication", a*b)
        
t = Test()
t.add(10,20)
t.multi(10,20)