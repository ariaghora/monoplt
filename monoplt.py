from cycler import cycler


def apply_monochrome_style(plt, font_size: int = 16, use_tex: bool = True):
    monochrome = (
        cycler("color", ["k"])
        * cycler("linestyle", ["-", "--", ":", "-."])
        * cycler("marker", ["^", "o", "x"])
    )

    plt.rcParams["axes.grid"] = True
    plt.rcParams["axes.prop_cycle"] = monochrome
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["legend.framealpha"] = 1
    plt.rcParams["legend.facecolor"] = "white"
    plt.rcParams["legend.edgecolor"] = "black"
    plt.rcParams["legend.markerscale"] = 0.8
    plt.rcParams["legend.fontsize"] = "small"

    plt.rcParams.update(
        {
            "text.usetex": use_tex,
            "font.family": "serif",
            "font.serif": ["Palatino"],
            "font.size": font_size,
        }
    )


def generate_pattern_cycler():
    res = (
        cycler("hatch", ["///", "--", "...", "\\\//", "xx", "\\\\"])
        * cycler("color", "w")
        * cycler("edgecolor", "k")
    )
    return res()
