import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima.model import ARIMA

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"
data = pd.read_csv(url, parse_dates=['Date'], index_col='Date')

data = data.asfreq('D')

autocorrelation_plot(data)
plt.title('Autocorrelation of Daily Minimum Temperatures')
plt.show()

model = ARIMA(data, order=(5,1,0))
fitted_model = model.fit()

print(fitted_model.summary())
