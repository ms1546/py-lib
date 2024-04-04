class ShapeVisitor:
    """ビジターインターフェイス。異なるシェイプに対する操作を定義する。"""
    def visit_circle(self, circle):
        pass

    def visit_rectangle(self, rectangle):
        pass

    def visit_triangle(self, triangle):
        pass

class Shape:
    """要素インターフェイス。ビジターを受け入れる。"""
    def accept(self, visitor: ShapeVisitor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_rectangle(self)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        visitor.visit_triangle(self)

class DrawVisitor(ShapeVisitor):
    """シェイプを描画するためのビジター。"""
    def visit_circle(self, circle):
        print(f"Drawing a circle with radius {circle.radius}")

    def visit_rectangle(self, rectangle):
        print(f"Drawing a rectangle with width {rectangle.width} and height {rectangle.height}")

    def visit_triangle(self, triangle):
        print(f"Drawing a triangle with base {triangle.base} and height {triangle.height}")

class AreaVisitor(ShapeVisitor):
    """シェイプの面積を計算するためのビジター。"""
    def visit_circle(self, circle):
        area = 3.14 * circle.radius ** 2
        print(f"Area of the circle is {area}")

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Area of the rectangle is {area}")

    def visit_triangle(self, triangle):
        area = 0.5 * triangle.base * triangle.height
        print(f"Area of the triangle is {area}")

# クライアントコード
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
triangle = Triangle(base=3, height=4)

draw_visitor = DrawVisitor()
area_visitor = AreaVisitor()

circle.accept(draw_visitor)
rectangle.accept(draw_visitor)
triangle.accept(draw_visitor)

circle.accept(area_visitor)
rectangle.accept(area_visitor)
triangle.accept(area_visitor)
