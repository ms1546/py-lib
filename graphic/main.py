import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# 円
circle, = ax.plot([], [], 'bo', ms=10)

def init():
    """アニメーションの初期フレームを設定する"""
    circle.set_data([], [])
    return circle,

def update(frame):
    """フレームごとに円の位置を更新する"""
    x = np.sin(frame * np.pi / 50) * np.cos(frame * np.pi / 25)
    y = np.sin(frame * np.pi / 50) * np.sin(frame * np.pi / 25)
    circle.set_data(x, y)
    return circle,

ani = FuncAnimation(fig, update, frames=np.arange(0, 500), init_func=init, blit=True)

plt.show()
