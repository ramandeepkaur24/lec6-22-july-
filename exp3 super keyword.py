class A:
    a = "I am a class variable in class A"
    def __init__(self):
        self.var1 ="I am inside class A's constructor\n"
        self.a ="Instance var in class A"
        self.special =" Special\n"

class B(A):
    a = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        super().__init__()
        self.a = "Instance var in class B"
        #super().__init__()


b = B()
print(b.special, b.var1, b.a)



