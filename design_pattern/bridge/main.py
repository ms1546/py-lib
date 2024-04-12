class Device:
    """デバイスの操作を定義する抽象クラス（インターフェイス）。"""
    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

    def get_volume(self):
        pass

    def set_volume(self, percent):
        pass

class RemoteControl:
    """リモートコントロールの実装クラス（インターフェイス）。"""
    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

class TV(Device):
    """テレビを操作する具体的なデバイスクラス。"""
    def __init__(self):
        self.enabled = False
        self.volume = 50

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = max(0, min(100, percent))

class Radio(Device):
    """ラジオを操作する具体的なデバイスクラス。"""
    def __init__(self):
        self.enabled = False
        self.volume = 30

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = max(0, min(100, percent))

# クライアントコード
tv = TV()
remote = RemoteControl(tv)
remote.toggle_power()
remote.volume_up()
remote.volume_down()
print(f"TV is {'on' if tv.is_enabled() else 'off'} with volume {tv.get_volume()}")

radio = Radio()
remote = RemoteControl(radio)
remote.toggle_power()
remote.volume_up()
print(f"Radio is {'on' if radio.is_enabled() else 'off'} with volume {radio.get_volume()}")
