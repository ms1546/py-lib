from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.datasets import load_rossi
import matplotlib.pyplot as plt

data = load_rossi()

kmf = KaplanMeierFitter()
kmf.fit(durations=data['week'], event_observed=data['arrest'])
kmf.plot_survival_function()
plt.title('Survival Function')
plt.xlabel('Time in Weeks')
plt.ylabel('Survival Probability')
plt.show()

cph = CoxPHFitter()
cph.fit(data, duration_col='week', event_col='arrest')

print(cph.summary)
