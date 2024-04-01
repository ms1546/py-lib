class HeavyResource:
    """重いリソースを表すクラス。インスタンス化に時間がかかる。"""
    def __init__(self):
        import time
        time.sleep(2)

    def process(self):
        return "HeavyResource is processed"

class HeavyResourceProxy:
    """HeavyResourceのプロキシ。遅延初期化とアクセス制御を提供する。"""
    def __init__(self):
        self._heavy_resource = None

    def process(self):
        if self._heavy_resource is None:
            self._heavy_resource = HeavyResource()
        return self._heavy_resource.process()

def client_code(resource):
    print(resource.process())

heavy_resource = HeavyResource()
client_code(heavy_resource)

heavy_resource_proxy = HeavyResourceProxy()
client_code(heavy_resource_proxy)
