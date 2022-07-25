class A:
    def sum(self,a):
        print(a)
class B(A):
    def sum(self,a):
        print("hi",a)
ob=B()
ob.sum("Raman")
