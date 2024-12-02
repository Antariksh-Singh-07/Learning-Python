class McLarenF1LM:
    
    Units = 6
    
    def __init__(self, model, color, name):
        self.model = model
        self.color = color
        self.name = name
        McLarenF1LM.Units -= 1

    def describe(self):
        print(
            f"The {self.model} owned by {self.name} colored {self.color} is the unit number {6-McLarenF1LM.Units} of 6"
        )
        
XP1 = McLarenF1LM("XP1 Prototype", "Papaya Orange", "McLaren Locomotives")
XP1.describe()
LM001 = McLarenF1LM("LM001", "Papaya Orange", "Sultan of Brunei")
LM001.describe()
LM002 = McLarenF1LM("LM002", "Papaya Orange", "Yoshio Tsuzuki")
LM002.describe()
LM003 = McLarenF1LM("LM003", "Papaya Orange", "Ralph Lauren")
LM003.describe()
LM004 = McLarenF1LM("LM004", "Grey/Black", "Sultan of Brunei")
LM004.describe()
LM005 = McLarenF1LM("LM005", "Grey/Black", "Sultan of Brunei")
LM005.describe()