# Skills Radar Plot Generator

## Overview

The **Skills Radar Plot Generator** is a Python program designed to create visually appealing radar plots for skills assessment. It is ideal for individuals and teams to analyze strengths and areas for improvement in a structured manner.

## Features
- Customizable inputs for skill categories and corresponding scores.
- Enhanced visuals with configurable colors, gridlines, and labels.
- Radar-style plotting for clear data representation.
- Display of skill scores directly on the plot for better readability.

## Installation

1. **Clone the repository**:

```bash
git clone <repo_url>
cd skills-radar-plot-generator
```

2. Install required dependencies:

Ensure Python is installed on your system, then install the necessary libraries:

```
pip install matplotlib numpy
```


## Usage

1. Run the program:

```
python skills_radar_plot.py
```

2. Customize your skills and scores:

Open the skills_radar_plot.py script and modify the categories and scores lists to fit your needs.

3. Output:

The program will display a radar plot highlighting skills with their respective scores.

Example Input

```
categories = [
    "Problem-Solving", "Coding", "System Design", 
    "Version Control", "DevOps", "Testing"
]
scores = [5, 4, 3, 4, 2, 3]
```

Example Output

The radar plot will visually display the input categories and scores, with distinct colors and labels for easy analysis.

## Debugging

1.	Input Validation:
    •	Ensure the categories and scores lists have the same length.
	•	Ensure all scores are numeric values.
2.	Common Issues:
	•	IndexError: Caused by mismatched lengths of categories and scores.
	•	ModuleNotFoundError: Ensure all dependencies are installed.
3.	Enhancements:
	•	Add CLI support for dynamic input.
	•	Save the radar plot as an image file.
	•	Add unit tests for individual functions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.