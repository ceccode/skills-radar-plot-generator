import unittest
from skills_radar_plot.plot import create_skills_radar_plot

class TestSkillsRadarPlot(unittest.TestCase):
    def test_plot_creation(self):
        categories = ["Skill1", "Skill2", "Skill3"]
        scores = [3, 4, 5]
        fig, ax = create_skills_radar_plot(categories, scores)
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)

if __name__ == "__main__":
    unittest.main()