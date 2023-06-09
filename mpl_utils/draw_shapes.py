from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.collections import LineCollection
from matplotlib.patches import FancyArrowPatch
from matplotlib.colors import Normalize
import numpy as np

__all__ = ["draw_arrows", "draw_earth", "draw_multicolored_line", "add_colorbar"]


def draw_arrows(axis, x, y, N=None, color="k"):
    r""" Draws arrows along a path on the axis """
    N = len(x) // 5 if N is None else N
    d = len(x) // (N + 1)

    idx = np.arange(d, len(x), d)
    for i in idx:
        ar = FancyArrowPatch((x[i - 1], y[i - 1]), (x[i], y[i]), arrowstyle="->", mutation_scale=20, color=color)
        axis.add_patch(ar)


def draw_earth(axis, R=1, N=50, zorder=999):
    r""" Draws the Earth on the axis (with shading indicating day/night) """
    # Nightside
    theta = np.linspace(np.pi / 2, 3 * np.pi / 2, N)
    Xn = R * np.cos(theta)
    Yn = R * np.sin(theta)
    Xn = np.append(Xn, Xn[0])
    Yn = np.append(Yn, Yn[0])
    # Dayside
    theta = np.linspace(-np.pi / 2, np.pi / 2, N)
    Xd = R * np.cos(theta)
    Yd = R * np.sin(theta)
    Xd = np.append(Xd, Xd[0])
    Yd = np.append(Yd, Yd[0])
    # Plot
    axis.plot(Xd, Yd, "-k", zorder=zorder)
    axis.plot(Xn, Yn, "-k", zorder=zorder)
    axis.fill(Xd, Yd, color="w")
    axis.fill(Xn, Yn, color="k")


def draw_multicolored_line(axis, x, y, c, cmap="jet", vmin=None, vmax=None, set_lim=False):
    r""" Draws a line with colors on a scale determined by c """

    vmin = c.min() if vmin is None else vmin
    vmax = c.max() if vmax is None else vmax

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    norm = Normalize(vmin, vmax)
    lc = LineCollection(segments, cmap=cmap, norm=norm)
    lc.set_array(c)
    line = axis.add_collection(lc)
    if set_lim:
        Lx = x.max() - x.min()
        Ly = y.max() - y.min()
        ax.set_xlim(x.min() - 0.1 * Lx, x.max() + 0.1 * Lx)
        ax.set_ylim(y.min() - 0.1 * Ly, y.max() + 0.1 * Ly)

    return line


def add_colorbar(axis, where="right", pad=0.05, size="2%"):
    r""" Adds colorbar next to an axis """
    divider = make_axes_locatable(axis)
    return divider.append_axes(where, size=size, pad=pad)
