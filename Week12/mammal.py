from heart import Heart

class Mammal:
    def __init__(self, age):
        self.age = age
        self.heart = Heart()  # Composition with Heart

    def speak(self):
        print("Generic mammal sound")

    def __str__(self):
        return f"Mammal, Age: {self.age}, Heart Rate: {self.heart}"
