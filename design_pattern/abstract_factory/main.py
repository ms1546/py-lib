class WidgetFactory:
    """抽象ファクトリー：ウィジェットを生成するためのインターフェース。"""
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

class WindowsWidgetFactory(WidgetFactory):
    """Windowsスタイルのウィジェットを生成する具体的なファクトリー。"""
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacWidgetFactory(WidgetFactory):
    """Macスタイルのウィジェットを生成する具体的なファクトリー。"""
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class Button:
    """ボタンの抽象クラス。"""
    def paint(self):
        pass

class Checkbox:
    """チェックボックスの抽象クラス。"""
    def paint(self):
        pass

class WindowsButton(Button):
    """Windowsスタイルのボタン。"""
    def paint(self):
        return "Painting a Windows style button"

class WindowsCheckbox(Checkbox):
    """Windowsスタイルのチェックボックス。"""
    def paint(self):
        return "Painting a Windows style checkbox"

class MacButton(Button):
    """Macスタイルのボタン。"""
    def paint(self):
        return "Painting a Mac style button"

class MacCheckbox(Checkbox):
    """Macスタイルのチェックボックス。"""
    def paint(self):
        return "Painting a Mac style checkbox"

# クライアントコード
def client_code(factory: WidgetFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

windows_factory = WindowsWidgetFactory()
client_code(windows_factory)

mac_factory = MacWidgetFactory()
client_code(mac_factory)
