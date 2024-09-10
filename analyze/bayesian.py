import pymc3 as pm
import numpy as np
import matplotlib.pyplot as plt
import arviz as az

np.random.seed(42)
X = np.linspace(0, 10, 100)
Y = 2.5 * X + np.random.normal(0, 1, 100)

with pm.Model() as linear_model:
    intercept = pm.Normal('Intercept', mu=0, sigma=10)
    slope = pm.Normal('Slope', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)

    y_est = intercept + slope * X

    likelihood = pm.Normal('y', mu=y_est, sigma=sigma, observed=Y)

    trace = pm.sample(3000, return_inferencedata=False)

with linear_model:
    az.plot_trace(trace)
    plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(X, Y, c='blue', label='Data')
pm.plot_posterior_predictive_glm(trace, samples=100, eval=np.linspace(0, 10, 100), label='Posterior predictive regression lines')
plt.title('Posterior predictive regression lines')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
