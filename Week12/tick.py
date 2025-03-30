class Tick:
    def __init__(self, host):
        self.host = host  # The host is a Mammal

    def suck_blood(self):
        print(f"{self.host.__class__.__name__} is being sucked by the tick!")

    def __str__(self):
        return "A blood-sucking tick"
