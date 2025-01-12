from skills_radar_plot.plot import create_skills_radar_plot
import matplotlib.pyplot as plt

categories = ["Problem-Solving", "Coding", "DevOps"]
scores = [5, 4, 3]

fig, ax = create_skills_radar_plot(categories, scores)
plt.show()