class Handler:
    """承認プロセスのハンドラの抽象クラス。"""
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass

class Manager(Handler):
    """マネージャーの承認レベルを持つハンドラ。"""
    def handle_request(self, request):
        if request <= 1000:
            return f"Manager approved the request of {request}"
        elif self._successor is not None:
            return self._successor.handle_request(request)

class Director(Handler):
    """ディレクターの承認レベルを持つハンドラ。"""
    def handle_request(self, request):
        if request <= 10000:
            return f"Director approved the request of {request}"
        elif self._successor is not None:
            return self._successor.handle_request(request)

class CEO(Handler):
    """CEOの承認レベルを持つハンドラ。"""
    def handle_request(self, request):
        return f"CEO approved the request of {request}"

# チェーン
ceo = CEO()
director = Director(ceo)
manager = Manager(director)

print(manager.handle_request(500))
print(manager.handle_request(5000))
print(manager.handle_request(50000))
