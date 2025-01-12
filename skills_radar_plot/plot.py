import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from .utils.grid import _customize_grid
from .utils.axes import _customize_axes

def create_skills_radar_plot(categories, scores, figsize=(18, 18), output_path=None):
    """
    Create and optionally save a radar plot for skills assessment.
    
    Args:
        categories (list): List of skill categories to display.
        scores (list): List of scores corresponding to categories.
        figsize (tuple): Figure size in inches (width, height).
        output_path (str): Path to save the generated plot. If None, the plot is not saved.
    """
    # Define color scheme
    colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
        '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
    ]
 
    # Create plot
    fig, ax = plt.subplots(figsize=figsize, subplot_kw=dict(polar=True))
 
    # Calculate angles
    num_vars = len(categories)
    offset = np.pi / num_vars
    angles = [(angle + offset) for angle in np.linspace(0, 2 * np.pi, num_vars, endpoint=False)]
 
    # Close the plot
    scores_plot = scores + scores[:1]
    angles_plot = angles + angles[:1]
    ax.fill(angles_plot, scores_plot, color='#dbdb8d', alpha=0.5)
    ax.plot(angles_plot, scores_plot, color='gray', linewidth=1, alpha=0.3)

    # Add scatter points and labels
    for i, (angle, score, category, color) in enumerate(zip(angles, scores, categories, colors)):
        ax.scatter(angle, score, c=color, s=200, zorder=3, label=category)
        ax.text(angle, score + 0.2, str(score), ha='center', va='center', color=color, fontweight='bold')

    _customize_grid(ax)
    _customize_axes(ax, angles, categories, colors)
    plt.title("Skills Radar Plot", pad=30, size=20, fontweight='bold', color='#333333')
    plt.tight_layout(pad=5.0)
    
    # Save the plot if an output path is provided
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
        print(f"Plot saved to {output_path}")

    return fig, ax
