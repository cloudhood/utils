import string
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


def enrich(**kwargs):
    """
    Enrich and annotate mpl plots.
    """
    plt.gca().set(**kwargs)
    plt.tight_layout
    plt.show()


def mavg_normal(
    xlab="Steps",
    title="Moving Average of Normal Variates",
    start_date="2022-01-01",
    n_series=4,
    periods=365,
    roll=7,
    freq="D",
    rotate=45,
    palette="tab10",
    linewidth=2,
    seed=123,
):
    """
    Simulate a set of daily Normal series and plot the moving average across time.
    """
    rng = np.random.default_rng(seed=seed)
    cols = list(string.ascii_uppercase[:n_series])
    dates = pd.date_range(start_date, periods=periods, freq=freq)
    vals = rng.normal(size=(periods, n_series)).cumsum(axis=0)
    dat = pd.DataFrame(vals, dates, columns=cols).rolling(roll).mean()
    ax = sns.lineplot(data=dat, palette=palette, linewidth=linewidth)
    plt.xticks(rotation=rotate)
    enrich(xlabel=xlab, title=title)
