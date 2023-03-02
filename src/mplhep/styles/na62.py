from __future__ import annotations

import matplotlib as mpl
from cycler import cycler

from .._deprecate import deprecated_dict

colors = [
    "#1a1af3",  # blue
    "#fa8f02",  # orange
    "#00bd00",  # green
    "#ff1414",  # red
    "#7228b5",  # purple
    "#6e260e",  # brown
    "#f026b2",  # pink
    "#7f7f7f",  # grey
    "#acad00",  # yellow-green
    "#02b7c9",  # cyan
]

markers = [
    "o",  # circle
    "s",  # squares
    "D",  # diamonds
    "^",  # triangle up
    "v",  # triangle down
    "<",  # triangle left
    ">",  # triangle right
    "P",  # plus (filled)
    "X",  # x (filled)
    "*",  # star
]

NA62 = {
    # Plot properties
    "axes.labelsize": 32,
    "axes.linewidth": 2,
    "axes.facecolor": "white",
    "axes.labelpad": 20.0,
    # Custom colors
    "axes.prop_cycle": cycler("color", colors) + cycler("marker", markers),
    "axes.formatter.min_exponent": 3,
    "axes.unicode_minus": False,
    # Figure properties
    "figure.figsize": (12, 9),
    "figure.dpi": 100,
    # Outer frame color
    "figure.facecolor": "white",
    "figure.autolayout": True,
    # Attempt to match font in ROOT
    "font.family": "sans-serif",
    "font.serif": ["Arial"],
    "font.size": 26,
    "font.weight": 400,
    # Legend
    "legend.frameon": True,
    "legend.fancybox": False,
    "legend.facecolor": "white",
    "legend.numpoints": 1,
    "legend.labelspacing": 0.2,
    "legend.fontsize": 28,
    "legend.title_fontsize": 28,
    "legend.loc": "best",
    "legend.handletextpad": 0.75,
    "legend.borderaxespad": 0,
    "legend.edgecolor": "black",
    "legend.framealpha": 1,
    # Colorbar
    "image.cmap": "jet",
    # Lines settings
    "lines.linewidth": 2,
    "lines.markeredgewidth": 2,
    "lines.markersize": 4,
    # Grid settings
    "grid.linestyle": "dotted",
    # errorbars
    "errorbar.capsize": 4,
    # Saved figure settings
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
    "savefig.format": "pdf",
    # Ticks settings
    # - add minor ticks & add to both sides of axes
    "xtick.minor.visible": True,
    "ytick.minor.visible": True,
    "xtick.top": True,
    "xtick.major.top": True,
    "xtick.minor.top": True,
    "xtick.major.bottom": True,
    "xtick.minor.bottom": True,
    "ytick.right": True,
    "ytick.major.left": True,
    "ytick.minor.left": True,
    "ytick.major.right": True,
    "ytick.minor.right": True,
    #
    "xtick.major.size": 14,
    "xtick.minor.size": 7,
    "xtick.major.width": 2,
    "xtick.minor.width": 2,
    "xtick.major.pad": 10,
    "xtick.minor.pad": 10,
    "xtick.direction": "in",
    "xtick.labelsize": 30,
    #
    "ytick.major.size": 14,
    "ytick.minor.size": 7,
    "ytick.major.width": 2,
    "ytick.minor.width": 2,
    "ytick.major.pad": 10,
    "ytick.minor.pad": 10,
    "ytick.direction": "in",
    "ytick.labelsize": 30,
    # Legend frame border size
    # WARNING: this affects every patch object
    # (i.e. histograms and so on)
    "patch.linewidth": 2,
    "xaxis.labellocation": "right",
    "yaxis.labellocation": "top",
    # text
    "text.fontsize": "smaller",
}

# Filter extra (labellocation) items if needed
NA62 = {k: v for k, v in NA62.items() if k in mpl.rcParams}

ROOT = deprecated_dict(
    NA62, message="'ROOT' style dict is deprecated, please use 'NA62' instead"
)

NA62Tex = {
    **NA62,
    # Use LaTeX rendering by default
    # (overrides default font)
    "text.usetex": True,
    # Use the LaTeX version of Times New Roman
    "text.latex.preamble": r"\usepackage{mathptmx}",
    "pgf.rcfonts": False,
}

ROOTTex = deprecated_dict(
    NA62Tex, message="'ROOT' style dict is deprecated, please use 'NA62' instead"
)
