class PaymentStrategy:
    """支払い戦略のインターフェイス。"""
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    """クレジットカードでの支払いを処理する戦略。"""
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

class DebitCardPayment(PaymentStrategy):
    """デビットカードでの支払いを処理する戦略。"""
    def pay(self, amount):
        return f"Paid {amount} using Debit Card"

class ElectronicMoneyPayment(PaymentStrategy):
    """電子マネーでの支払いを処理する戦略。"""
    def pay(self, amount):
        return f"Paid {amount} using Electronic Money"

class PaymentContext:
    """支払い戦略のコンテキスト。"""
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        return self._strategy.pay(amount)

# クライアントコード
context = PaymentContext(CreditCardPayment())
print(context.execute_payment(100))

context.set_strategy(DebitCardPayment())
print(context.execute_payment(200))

context.set_strategy(ElectronicMoneyPayment())
print(context.execute_payment(300))
