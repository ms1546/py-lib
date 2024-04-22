import numpy as np

G = 6.67430e-11  # 万有引力定数 (m^3 kg^-1 s^-2)
M = 5.972e24     # 地球の質量 (kg)
c = 299792458    # 光速 (m/s)
r_earth = 6371000  # 地球の半径 (m)

# シュヴァルツシルト半径の計算
r_s = 2 * G * M / c**2

def time_dilation(r):
    """ r: 観測地点の地球中心からの距離 (m)  時間遅延を計算する"""
    return np.sqrt(1 - r_s / r)

time_dilation_earth = time_dilation(r_earth)

heights = np.linspace(0, 40000, 5)
time_dilations = time_dilation(r_earth + heights)

print("Time dilation at Earth's surface:", time_dilation_earth)
print("Time dilation at various heights above Earth:")
for h, dilation in zip(heights, time_dilations):
    print(f"  {h} meters: {dilation}")
