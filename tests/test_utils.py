import unittest
from skills_radar_plot.utils.grid import _customize_grid
from skills_radar_plot.utils.axes import _customize_axes
import matplotlib.pyplot as plt


class TestUtils(unittest.TestCase):

    def test_customize_grid(self):
        fig, ax = plt.subplots()
        _customize_grid(ax)

        # Check if the grid is enabled
        for line in ax.yaxis.get_gridlines():
            self.assertTrue(line.get_visible(),
                            "Y-axis gridline is not visible.")
        for line in ax.xaxis.get_gridlines():
            self.assertTrue(line.get_visible(),
                            "X-axis gridline is not visible.")

    def test_customize_axes(self):
        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        angles = [0, 1, 2]
        categories = ["Skill1", "Skill2", "Skill3"]
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
        _customize_axes(ax, angles, categories, colors)
        self.assertEqual(len(ax.get_xticks()), len(categories))


if __name__ == "__main__":
    unittest.main()
