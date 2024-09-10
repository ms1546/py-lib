class CPU:
    """CPUの初期化を担当するクラス。"""
    def start(self):
        return "CPU started"

class Memory:
    """メモリの確保を担当するクラス。"""
    def allocate(self):
        return "Memory allocated"

class InputOutputSystem:
    """入出力システムのセットアップを担当するクラス。"""
    def initialize(self):
        return "Input/Output system initialized"

class ComputerFacade:
    """コンピュータの起動プロセスを統一インターフェースで提供するファサードクラス。"""
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.io_system = InputOutputSystem()

    def start_computer(self):
        steps = [
            self.cpu.start(),
            self.memory.allocate(),
            self.io_system.initialize()
        ]
        return "Computer started with following steps: " + ", ".join(steps)

# クライアントコード
computer_facade = ComputerFacade()
print(computer_facade.start_computer())
