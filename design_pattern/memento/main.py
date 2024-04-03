class Memento:
    """メメント：エディタの状態を保存する。"""
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class Editor:
    """起源者：テキストエディタの状態を持ち、メメントを通じてその状態を保存/復元する。"""
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        self._state = state

    def save_to_memento(self):
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()

    def get_state(self):
        return self._state

class Caretaker:
    """管理者：エディタのメメントを保持し、アンドゥ操作を管理する。"""
    def __init__(self):
        self._mementos = []

    def save_state(self, editor):
        self._mementos.append(editor.save_to_memento())

    def undo(self, editor):
        if not self._mementos:
            return
        memento = self._mementos.pop()
        editor.restore_from_memento(memento)

# クライアントコード
editor = Editor()
caretaker = Caretaker()

editor.set_state("State 1")
caretaker.save_state(editor)
print("Current State:", editor.get_state())

editor.set_state("State 2")
caretaker.save_state(editor)
print("Current State:", editor.get_state())

editor.set_state("State 3")
print("Current State:", editor.get_state())

caretaker.undo(editor)
print("After undo:", editor.get_state())

caretaker.undo(editor)
print("After undo:", editor.get_state())
