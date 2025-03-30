from mammal import Mammal
from tick import Tick

class Puma(Mammal):
    def __init__(self, age, tick=None):
        super().__init__(age)
        self.tick = tick  # Aggregation with Tick

    def speak(self):
        print("Roar")

    def __str__(self):
        return f"Puma, Age: {self.age}, Heart Rate: {self.heart}, Tick Attached: {self.tick is not None}"
