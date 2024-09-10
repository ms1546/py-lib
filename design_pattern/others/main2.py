class Command:
    """コマンドパターンのインターフェース。実行する操作の抽象化を提供する。"""
    def execute(self):
        pass

class AddProductCommand(Command):
    """商品をカートに追加する具体的なコマンド。"""
    def __init__(self, product, cart):
        self.product = product
        self.cart = cart

    def execute(self):
        self.cart.add(self.product)
        print(f"Added {self.product.name} to the cart.")

class RemoveProductCommand(Command):
    """カートから商品を削除する具体的なコマンド。"""
    def __init__(self, product, cart):
        self.product = product
        self.cart = cart

    def execute(self):
        self.cart.children.remove(self.product)
        print(f"Removed {self.product.name} from the cart.")

class CheckoutCommand(Command):
    """カートでチェックアウトを実行する具体的なコマンド。"""
    def __init__(self, cart):
        self.cart = cart

    def execute(self):
        total = self.cart.get_price()
        print(f"Checkout completed. Total: ${total}")

class Component:
    """コンポジットパターンのコンポーネントインターフェース。商品や追加サービスの共通のインターフェース。"""
    def get_price(self):
        pass

class Product(Component):
    """具体的な商品を表すクラス。"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

class CompositeProduct(Component):
    """複数の商品またはサービスを一つのグループとして扱うコンポジットオブジェクト。"""
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def get_price(self):
        return sum(child.get_price() for child in self.children)

# クライアントコード
cart = CompositeProduct()
coffee_maker = Product("Coffee Maker", 70)
toaster = Product("Toaster", 30)

add_coffee_maker = AddProductCommand(coffee_maker, cart)
add_coffee_maker.execute()

add_toaster = AddProductCommand(toaster, cart)
add_toaster.execute()

checkout = CheckoutCommand(cart)
checkout.execute()
