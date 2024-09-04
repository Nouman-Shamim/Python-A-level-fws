class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    return animal.speak()

# Creating instances of different animal types
dog = Dog()
cat = Cat()
bird = Bird()

# Calling the function with different types of animals
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(bird))  # Output: Chirp!
