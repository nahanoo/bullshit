from bullshit import Player
from matplotlib import pyplot as plt
import scipy
import scipy.stats
import statsmodels.stats.proportion

for i in range(1,10):
    x = scipy.linspace(0,i,i+1)
    pmf = scipy.stats.binom.pmf(x,i,1/3)
    plt.plot(x,pmf)
    plt.title(str(i))
    c = statsmodels.stats.proportion.proportion_confint(pmf,1,alpha=0.05)
    for d,p in enumerate(pmf):
        if p >= 0.2:
            estimate = d
    print(estimate)
    plt.plot(estimate,pmf[estimate],'ro')
    plt.show()

