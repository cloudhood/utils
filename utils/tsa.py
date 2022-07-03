import numpy as np
import matplotlib.pyplot as plt

_seed = 123
_rng = np.default_rng(seed=seed)

def ar1(rng=_rng, n=1000, rho=.9, plot=True):
  eps = rng.normal(size=steps)
  y = np.zeros(steps)
  for i in range(1, len(e)):
    y[i] = rho * y[i] + e[i]
  if plot:
    plt.plot(y)
    plt.show()
  return y
