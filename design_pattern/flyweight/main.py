class CharacterFlyweight:
    def __init__(self, font, size):
        self.font = font
        self.size = size

    def display(self, position):
        return f"Font: {self.font}, Size: {self.size}, Position: {position}"

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            font, size = key
            self.flyweights[key] = CharacterFlyweight(font, size)
        return self.flyweights[key]

    def total_flyweights(self):
        return len(self.flyweights)

# クライアントコード
factory = FlyweightFactory()

character1 = factory.get_flyweight(("Arial", 12))
character2 = factory.get_flyweight(("Arial", 12))
character3 = factory.get_flyweight(("Times New Roman", 14))

print(character1.display("1A"))
print(character2.display("2B"))
print(character3.display("3C"))

print("Total flyweights:", factory.total_flyweights())
