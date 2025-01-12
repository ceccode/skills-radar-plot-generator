import numpy as np

def _customize_axes(ax, angles, categories, colors):
    """Customize the axes appearance."""
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], color="darkgrey", size=12, fontweight='bold')
    ax.set_xticks(angles)
    ax.set_xticklabels(categories, size=11)

    for label, angle, color in zip(ax.get_xticklabels(), angles, colors):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')
        label.set_rotation(angle * 180 / np.pi - 90)
        label.set_fontweight('bold')
        label.set_color(color)