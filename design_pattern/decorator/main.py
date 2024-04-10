class Coffee:
    """コーヒーのコンポーネントのインターフェース（または抽象クラス）。"""
    def cost(self):
        pass

    def description(self):
        pass

class SimpleCoffee(Coffee):
    """具体的なコンポーネント：基本のコーヒー。"""
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

class CoffeeDecorator(Coffee):
    """デコレーターの基底クラス。"""
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

    def description(self):
        return self.coffee.description()

class MilkDecorator(CoffeeDecorator):
    """ミルクデコレーター。"""
    def cost(self):
        return self.coffee.cost() + 2

    def description(self):
        return self.coffee.description() + ", with milk"

class SugarDecorator(CoffeeDecorator):
    """砂糖デコレーター。"""
    def cost(self):
        return self.coffee.cost() + 1

    def description(self):
        return self.coffee.description() + ", with sugar"

# クライアントコード
simple_coffee = SimpleCoffee()
print(f"Cost: {simple_coffee.cost()}; Description: {simple_coffee.description()}")

milk_coffee = MilkDecorator(simple_coffee)
print(f"Cost: {milk_coffee.cost()}; Description: {milk_coffee.description()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Cost: {sugar_milk_coffee.cost()}; Description: {sugar_milk_coffee.description()}")
