class Cars:

    def __init__(self, model, year, price, max, acc):
        self.model = model
        self.year = year
        self.price = price
        self.max = max
        self.acc = acc

    def describe(self):
        print(
            f"The {self.year} {self.model} coming at $ {self.price} can go to the max of {self.max} kmph with 0-100kmph in {self.acc} seconds"
        )


GT3RS = Cars("Prosche 911 GT3 RS", 2022, 220000, 296, 3.2)
Diablo = Cars("Lamborghini Diablo VT Roadster", 1999, 190000, 325, 3.9)
F1_LM = Cars("McLaren F1 Le Mans", 1995, 19800000, 362, 2.9)

GT3RS.describe()
Diablo.describe()
F1_LM.describe()
