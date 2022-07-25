class Animal:
    def walk(self):
        print("Dog is walking")
class human(Animal):
    def walk(self):
        print("Human is walking")
obj=human()
obj.walk()
obj=Animal()
obj.walk()
