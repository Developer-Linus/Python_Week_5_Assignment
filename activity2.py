class Animals:
    def sound(self):
        pass
class Dog(Animals):
    def sound(self):
        print('The dog barks')
class Cat(Animals):
    def sound(self):
        print('The cat meows')

#Instantiating the classes dog and cat
dog = Dog()
cat = Cat()


dog.sound()
cat.sound()
