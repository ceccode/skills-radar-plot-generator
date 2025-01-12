def _customize_grid(ax):
    """Customize the grid appearance."""
    ax.set_facecolor('#f8f9fa')
    ax.yaxis.grid(True, color="grey", alpha=0.3, linestyle="-", linewidth=0.5)
    ax.xaxis.grid(True, color="grey", alpha=0.3, linestyle="-", linewidth=0.5)