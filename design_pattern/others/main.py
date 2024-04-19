class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

class ProductFactory:
    """Factory Method パターンを使用して商品オブジェクトを生成するファクトリクラス。"""
    @staticmethod
    def create_product(name, price):
        return Product(name, price)

class Database:
    """Singleton パターンでデータベース接続を管理するクラス。"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._connection = None
        return cls._instance

    def connect(self):
        if not self._connection:
            self._connection = "Database Connection Established"
        return self._connection

db = Database()
print(db.connect())
product = ProductFactory.create_product("Coffee Maker", 99.95)
print(product)

class Observer:
    """オブザーバーインターフェース。状態の変化を監視する。"""
    def update(self, message):
        pass

class OrderStatus:
    """注文の状態を管理し、オブザーバーに通知する。"""
    def __init__(self):
        self._observers = []
        self._status = "pending"

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._status)

    def change_status(self, status):
        self._status = status
        self.notify()

class EmailNotification(Observer):
    """Eメール通知を行う具体的なオブザーバー。"""
    def update(self, message):
        print(f"Email sent: Order status changed to {message}")

class SMSNotification(Observer):
    """SMS通知を行う具体的なオブザーバー。"""
    def update(self, message):
        print(f"SMS sent: Order status changed to {message}")

class PaymentStrategy:
    """支払い戦略のインターフェース。"""
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    """クレジットカードによる支払いを行う具体的な戦略。"""
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    """PayPalによる支払いを行う具体的な戦略。"""
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# クライアントコード
order_status = OrderStatus()
order_status.attach(EmailNotification())
order_status.attach(SMSNotification())

order_status.change_status("shipped")

payment_strategy = PayPalPayment()
payment_strategy.pay(120.00)

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

class ProductDecorator(Component):
    """デコレーターパターンを使い、商品に追加機能を動的に装飾するクラス。"""
    def __init__(self, component):
        self.component = component

    def get_price(self):
        return self.component.get_price()

class GiftWrapping(ProductDecorator):
    """ギフトラッピングサービスを表すデコレーター。"""
    def get_price(self):
        return self.component.get_price() + 5

# クライアントコード
coffee_maker = Product("Coffee Maker", 70)
toaster = Product("Toaster", 30)

cart = CompositeProduct()
cart.add(coffee_maker)
cart.add(toaster)

gift_wrapped_cart = GiftWrapping(cart)

total_price = gift_wrapped_cart.get_price()
total_price
