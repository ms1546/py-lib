class Car:
    """製品:Carオブジェクト"""
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)

class Builder:
    """Builderインターフェイス"""
    def reset(self):
        pass

    def set_engine(self, engine):
        pass

    def set_seats(self, seats):
        pass

    def set_tires(self, tires):
        pass

class CarBuilder(Builder):
    """具体的なBuilder：Carのビルドプロセスを実装"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_engine(self, engine):
        self.car.add(f"Engine: {engine}")

    def set_seats(self, seats):
        self.car.add(f"Seats: {seats}")

    def set_tires(self, tires):
        self.car.add(f"Tires: {tires}")

    def get_product(self):
        product = self.car
        self.reset()
        return product

class Director:
    """Director: ビルドの手順を定義"""
    def __init__(self, builder):
        self._builder = builder

    def build_minimal_viable_product(self):
        self._builder.set_engine("4-cylinder")
        self._builder.set_seats("4")

    def build_full_featured_product(self):
        self._builder.set_engine("V8")
        self._builder.set_seats("4")
        self._builder.set_tires("Off-road")

# クライアントコード
builder = CarBuilder()
director = Director(builder)

director.build_minimal_viable_product()
car = builder.get_product()
print("Minimal car built:", car.list_parts())

director.build_full_featured_product()
car = builder.get_product()
print("Full featured car built:", car.list_parts())
