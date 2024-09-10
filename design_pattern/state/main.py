class TrafficLightState:
    """ステートインターフェース。交通信号の振る舞いを定義。"""
    def handle_request(self):
        pass

class RedLight(TrafficLightState):
    """赤信号の状態を表すクラス。"""
    def handle_request(self):
        return "Stop", GreenLight()

class GreenLight(TrafficLightState):
    """緑信号の状態を表すクラス。"""
    def handle_request(self):
        return "Go", YellowLight()

class YellowLight(TrafficLightState):
    """黄信号の状態を表すクラス。"""
    def handle_request(self):
        return "Caution", RedLight()

class TrafficLight:
    """コンテキストクラス。現在の信号の状態を保持し、ステートオブジェクトに振る舞いを委譲する。"""
    def __init__(self):
        self.state = RedLight()

    def change(self):
        action, next_state = self.state.handle_request()
        self.state = next_state
        return action

# クライアントコード
def simulate_traffic_light(traffic_light, changes):
    results = []
    for _ in range(changes):
        results.append(traffic_light.change())
    return results

traffic_light = TrafficLight()
simulation_results = simulate_traffic_light(traffic_light, 6)
simulation_results
