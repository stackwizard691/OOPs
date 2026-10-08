#simple inheritance
#Base class

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f"{self.name} makes a sound.")


# object
# animal=Animal("Dog")
# animal.speak()

#Derived class
# class Dog(Animal):
#     def __init__(self,name):
#         self.behaviour="Friendly"
#         self.name=name
#     def speak(self):
#         print(f"{self.name} barks. He is very {self.behaviour}")

# dog=Dog("Tommy")
# dog.speak()

#super keyword
#super

#Base class
class Animal:
    def __init__(self):
        self.name="Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

#Derived class
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed

    def speak(self):
        super().speak() #call the base class method
        print(f"{self.name} barks .It is a {self.breed}.")

## create an instance of Dog
dog=Dog("Golden Retriver")
dog.speak() 