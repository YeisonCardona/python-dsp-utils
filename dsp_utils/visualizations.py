from dataclasses import dataclass
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec



########################################################################
@dataclass
class Visualizer:
    figsize: tuple = (16, 7)
    dpi: int = 100
    grid: bool = True

    ## ----------------------------------------------------------------------
    #def __post_init__(self):
        #plt.rcParams["figure.figsize"] = self.figsize
        #plt.rcParams["figure.dpi"] = self.dpi


    # ----------------------------------------------------------------------
    @classmethod
    def plot_signal(self, signal, *, ax=None, fn='plot', time=None, title=None, xlabel=None, ylabel=None, labels=None, **kwargs):
        """"""

        if ax is None:
            plt.figure(figsize=self.figsize, dpi=self.dpi)
            ax = plt.subplot(111)


        fn_plot = getattr(ax, fn)

        if title:
            plt.title(title)

        if not time is None:
            if signal.ndim == 2:
                [fn_plot(time, s, **kwargs) for s in signal]
            else:
                fn_plot(time, signal, **kwargs)
        else:
            if signal.ndim == 2:
                [fn_plot(s, **kwargs) for s in signal]
            else:
                fn_plot(signal, **kwargs)

        if xlabel:
            ax.set_xlabel(xlabel)

        if ylabel:
            ax.set_ylabel(ylabel)

        if labels:
            ax.legend(labels)

        ax.grid(self.grid)
        #plt.show()


    # ----------------------------------------------------------------------
    def plot_kde(self, signal, *, fn='plot', time=None, title=None, xlabel=None, ylabel=None, labels=None):
        """"""

        fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        gs = GridSpec(1, 2, width_ratios=[3, 1])

        ax1 = fig.add_subplot(gs[0])
        self.plot_signal(signal, ax=ax1, fn=fn, time=time, title=title, xlabel=xlabel, ylabel=ylabel, labels=labels)


        ax2 = fig.add_subplot(gs[1], sharey=ax1)
        ax2.grid(self.grid)
        sns.kdeplot(y=signal, ax=ax2, bw_adjust=0.5, label="Curva de Densidad")
        #ax2.yaxis.set_ticks([])

        plt.subplots_adjust(wspace=0.07)
