class Observer:
    def update(self, symbol, price):
        pass

class Subject:
    def attach(self, observer: Observer):
        pass

    def detach(self, observer: Observer):
        pass

    def notify(self):
        pass

class StockMarket(Subject):
    def __init__(self):
        self.__observers = []
        self.__stock_prices = {}

    def attach(self, observer: Observer):
        self.__observers.append(observer)

    def detach(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            for symbol, price in self.__stock_prices.items():
                observer.update(symbol, price)

    def add_stock(self, symbol, price):
        self.__stock_prices[symbol] = price
        self.notify()

class Investor(Observer):
    def __init__(self, name):
        self.name = name
        self.stock_portfolio = {}

    def update(self, symbol, price):
        self.stock_portfolio[symbol] = price
        print(f"{self.name} was notified about {symbol} price change to {price}")

stock_market = StockMarket()
investor1 = Investor("Alice")
investor2 = Investor("Bob")

stock_market.attach(investor1)
stock_market.attach(investor2)

stock_market.add_stock("AAPL", 150)
stock_market.add_stock("GOOGL", 2800)
