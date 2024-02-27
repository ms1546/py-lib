from pulp import *
import pandas as pd

# パラメータ設定
days = range(7)
shifts = ['Day', 'Night']
nurses = range(5)

prob = LpProblem("Nurse_Scheduling", LpMinimize)

x = LpVariable.dicts("shift", (nurses, days, shifts), cat='Binary')

prob += 0

# 制約
for nurse in nurses:
    # 各ナースは週に最大5日間勤務
    prob += lpSum(x[nurse][day][shift] for day in days for shift in shifts) <= 5

    for day in days:
        # 各ナースは1日に1シフトのみ
        prob += lpSum(x[nurse][day][shift] for shift in shifts) <= 1

for day in days:
    for shift in shifts:
        # 各シフトは少なくとも1人のナース
        prob += lpSum(x[nurse][day][shift] for nurse in nurses) >= 1

prob.solve()

# 結果出力
schedule_data = []
for nurse in nurses:
    for day in days:
        for shift in shifts:
            if x[nurse][day][shift].value() == 1:
                schedule_data.append({"Nurse": f"Nurse {nurse}", "Day": day, "Shift": shift})

df_schedule = pd.DataFrame(schedule_data)

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df_schedule["Day"] = df_schedule["Day"].apply(lambda x: day_names[x])

df_schedule_pivot = df_schedule.pivot(index="Nurse", columns="Day", values="Shift")
df_schedule_pivot_filled = df_schedule_pivot.fillna("")


print(df_schedule_pivot_filled)
