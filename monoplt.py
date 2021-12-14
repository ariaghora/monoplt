from cycler import cycler


monoplt_config = {"primary_color": "black", "font_size": 16}


def apply_monochrome_style(
    plt, font_size: int = 16, use_tex: bool = True, primary_color: str = "black"
):
    monoplt_config["primary_color"] = primary_color
    monoplt_config["font_size"] = font_size

    monochrome = (
        cycler("color", [monoplt_config["primary_color"]])
        * cycler("linestyle", ["-", "--", ":", "-."])
        * cycler("marker", ["^", "o", "x"])
    )

    plt.rcParams["axes.grid"] = False
    plt.rcParams["axes.prop_cycle"] = monochrome
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    plt.rcParams["legend.framealpha"] = 1
    plt.rcParams["legend.facecolor"] = "white"
    plt.rcParams["legend.edgecolor"] = monoplt_config["primary_color"]
    plt.rcParams["legend.markerscale"] = 0.8
    plt.rcParams["legend.fontsize"] = "small"

    plt.rcParams.update(
        {
            "text.usetex": use_tex,
            "font.family": "serif",
            "font.serif": ["Palatino"],
            "font.size": monoplt_config["font_size"],
        }
    )


def generate_pattern_cycler():
    res = (
        cycler("hatch", ["", "///", "OO", "--", "**", "...", "\\\//", "xx", "\\\\"])
        * cycler("color", "w")
        * cycler("edgecolor", monoplt_config["primary_color"])
    )
    return res()
