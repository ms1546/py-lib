class GraphicComponent:
    """コンポーネントのインターフェース。"""
    def draw(self):
        pass

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def get_child(self, index):
        pass

class Leaf(GraphicComponent):
    """リーフオブジェクト。単一の図形を表す。"""
    def __init__(self, name):
        self.name = name

    def draw(self):
        return f"Draw {self.name}"

class Composite(GraphicComponent):
    """コンポジットオブジェクト。複数のグラフィックコンポーネントを含む。"""
    def __init__(self, name):
        self.name = name
        self.children = []

    def draw(self):
        result = [f"Composite {self.name} includes:"]
        for child in self.children:
            result.append(child.draw())
        return "\n".join(result)

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_child(self, index):
        return self.children[index]

# クライアントコード
def client_code(component):
    print(component.draw())

simple_circle = Leaf("Circle")
client_code(simple_circle)

composite_shape = Composite("Group 1")
composite_shape.add(Leaf("Rectangle"))
composite_shape.add(Leaf("Triangle"))

sub_composite = Composite("Group 2")
sub_composite.add(Leaf("Square"))
sub_composite.add(Leaf("Ellipse"))
composite_shape.add(sub_composite)

client_code(composite_shape)
