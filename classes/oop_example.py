# OOP is like building superhero  🦸‍♂️
# Author: Sithum Geeth - Beginner coder!

# Example 1: Basic Class
class Superhero:
    """A simple superhero class."""
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def introduce(self):
        print("I'm {}, with {} power! 💥".format(self.name, self.power))

# Example 2: Class with Methods
class EnergeticHero:
    """Hero with energy for actions."""
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy
    
    def fight(self):
        if self.energy >= 20:
            self.energy -= 20
            print("{} fights! Energy: {} ⚔️".format(self.name, self.energy))
        else:
            print("{} is tired! 😴".format(self.name))

# Example 3: Inheritance
class FlyingHero(Superhero):
    """Flying hero from Superhero."""
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed
    
    def fly(self):
        print("{} flies at {} km/h! ✈️".format(self.name, self.speed))

# Small Project: Hero Academy
class HeroAcademy:
    """Manages heroes."""
    def __init__(self):
        self.heroes = []
    
    def enroll(self, hero):
        self.heroes.append(hero)
        print("{} joined! 🎓".format(hero.name))
    
    def list_heroes(self):
        if not self.heroes:
            print("No heroes yet!")
        else:
            print("Heroes:")
            for h in self.heroes:
                print("- {}".format(h.name))

# Main demo
if __name__ == "__main__":
    print("=== OOP Demo ===")
    
    hero1 = Superhero("Captain Code", "Speed")
    hero1.introduce()
    
    hero2 = EnergeticHero("Power Punch", 80)
    hero2.fight()
    
    hero3 = FlyingHero("Sky Flyer", "Wind", 300)
    hero3.introduce()
    hero3.fly()
    
    academy = HeroAcademy()
    academy.enroll(hero1)
    academy.enroll(hero2)
    academy.enroll(hero3)
    academy.list_heroes()
    
    print("=== Heroes Ready! ===")
    print("*" * 40)
    print("\nLearn with Sithum")
