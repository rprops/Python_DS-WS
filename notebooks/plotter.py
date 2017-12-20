#this writes a file in your directory, check it(!)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib import cm
from matplotlib.ticker import MaxNLocator

def vmm_station_plotter(flowdata, label="flow (m$^3$s$^{-1}$)"):
    colors = [cm.viridis(x) for x in np.linspace(0.0, 1.0, len(flowdata.columns))] # list comprehension to set up the color sequence

    fig, axs = plt.subplots(3, 1, figsize=(16, 8))

    for ax, col, station in zip(axs, colors, flowdata.columns):
        ax.plot(flowdata.index, flowdata[station], label=station, color=col) # this plots the data itself
        
        ax.legend(fontsize=15)
        ax.set_ylabel(label, size=15)
        ax.yaxis.set_major_locator(MaxNLocator(4)) # smaller set of y-ticks for clarity
        
        if not ax.is_last_row():  # hide the xticklabels from the none-lower row x-axis
            ax.xaxis.set_ticklabels([])
            ax.xaxis.set_major_locator(mdates.YearLocator())
        else:                     # yearly xticklabels from the lower x-axis in the subplots
            ax.xaxis.set_major_locator(mdates.YearLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        ax.tick_params(axis='both', labelsize=15, pad=8) # enlarge the ticklabels and increase distance to axis (otherwise overlap)
    return fig, axs