class Bird():
    def sound(self):
        print('Birds make sound')

class Crow(Bird):
    def sound(self):
        print("Crows say 'Caw Caw'")

class Parrot(Bird):
    def sound(self):
        print('Parrot sounds, "squawk"')

bird1 = Crow()
bird2 = Parrot()

bird1.sound()
bird2.sound()
