from mammal import Mammal
from person import Person
from puma import Puma
from tick import Tick

def main():
    # Create a generic Mammal
    generic_mammal = Mammal(age=5)
    generic_mammal.speak()
    print(generic_mammal)

    # Create a Person and have them beat their heart
    person = Person(name="John", age=30, height=175)
    person.speak()
    person.heart.beat()
    print(person)

    # Create a Tick and suck blood
    tick = Tick(host=person)
    tick.suck_blood()

    # Create a Puma with a Tick attached
    puma_tick = Tick(host=Puma(age=4))
    puma = Puma(age=4, tick=puma_tick)
    puma.speak()
    puma.tick.suck_blood()
    print(puma)

if __name__ == "__main__":
    main()
