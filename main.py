import os
from datetime import datetime
from skills_radar_plot.plot import create_skills_radar_plot
import matplotlib.pyplot as plt


def main():

    # Define categories and scores
    categories = [
        "Problem-Solving & Debugging",
        "Coding Proficiency",
        "System Design",
        "Version Control",
        "DevOps & Deployment",
        "Testing & QA",
        "Infrastructure as Code",
        "Monitoring & Incident Mgmt",
        "Application Security",
        "IAM",
        "Threat Detection & Response",
        "AI Concepts & Applications",
        "Working with LLMs",
        "AI Ethics & Bias",
        "Design Patterns Knowledge",
        "Architectural Patterns",
        "Domain-Driven Design",
        "Time Mgmt & Prioritization",
        "Empowering Team Members",
        "Emotional Intelligence",
        "Facilitating Collaboration",
        "Communication & Collaboration",
    ]

    scores = [5, 4, 3, 3, 4, 3, 2, 2, 3, 2, 4, 3, 4, 3, 4, 3, 3, 4, 4, 3, 5, 4]

    # Define output path for Docker
    output_dir = "/app/outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"radar_plot_{timestamp}.png")

    # Create and save the radar plot
    create_skills_radar_plot(categories, scores, output_path=output_path)


if __name__ == "__main__":
    main()
