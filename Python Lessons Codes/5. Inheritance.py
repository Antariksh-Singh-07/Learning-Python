# Inheritance -> class child(parent)
# Multiple Inheritance -> class child(mother, father,...)
# Multilevel Inheritance -> class child(parent) --- class parent(grandparent)

class Pokemon:
    
    def __init__(self, name, nick, gen):
        self.name = name
        self.nick = nick
        self.gen = gen
        
    def announce(self):
        print(f"{self.name} from gen {self.gen} has the nick {self.nick}")
    
class Physical(Pokemon): #Inheritance
    
    def is_physical(self):
        print(f"{self.name} is a Physical attacker")

class Special(Pokemon): #Inheritance
    
    def is_special(self):
        print(f"{self.name} is a Special attacker")
        
class Kyogre(Special): #Multilevel Inheritance
    pass

class Groudon(Physical): #Multilevel Inheritance
    pass

class Rayqyaza(Physical, Special): #Multiple & Multilevel Inheritance
    pass

obese_macchi = Kyogre("Kyogre", "Obese Macchi", 3)
guddu = Groudon("Groudon", "Guddu", 3)
hawai_saanp = Rayqyaza("Rayquaza","Hawai Saanp",3)

obese_macchi.announce()
guddu.announce()
hawai_saanp.announce()

print() 

obese_macchi.is_special()
guddu.is_physical()
hawai_saanp.is_special()
hawai_saanp.is_physical()