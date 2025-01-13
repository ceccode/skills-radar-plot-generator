# Skills Radar Plot Generator

## Overview

The **Skills Radar Plot Generator** is a Python application that creates visually appealing radar plots for skills assessment. It's ideal for professionals and teams to analyze strengths and improvement areas in a structured and insightful way.

## Features

- **Customizable**: Easily adapt categories and scores to suit your needs.
- **Stylized Visuals**: Enhanced with colors, gridlines, and labels for readability.
- **Developer-Friendly**: Modular structure, making it easy to contribute or extend functionality.
- **Unit Tests**: Comprehensive test coverage to ensure reliability.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Docker** (optional, for containerized development)

### Setting Up a Virtual Environment (Recommended)

1. **Create and activate a virtual environment**:

```bash
pip install virtualenv
```

Navigate to your project directory and run the following command to create a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3.	Deactivate the environment when done:

```bash
deactivate
```

### Using Docker for Development (Optional)

1.	Build the Docker image:

```bash
docker build -t skills-radar-plot .
```

2.	Run the Docker container:

```bash
docker run --rm -v "$(pwd)/outputs:/app/outputs" skills-radar-plot
```

After the container completes its execution, the image will be available in the outputs/ directory on your host machine.


3.	(Optional) Using Docker Compose:


**Build the Services:**

```bash
docker-compose build
```

**Run the Application:**

```bash
docker-compose up app
```

**Run Tests:**

```bash
docker-compose up tests
```

**Cleanup:**

```bash
docker-compose up down
```


## Run the Application

To generate and display the radar plot, use:

•	With virtual environment:

```bash
python main.py
```

•	With Docker:

```
docker run --rm -it skills-radar-plot
```



## Customize Inputs

To use your own data, modify the categories and scores variables in main.py:

```python
categories = ["Problem-Solving", "Coding", "DevOps"]
scores = [5, 4, 3]
```

## Examples

### Example Input

You can also find examples in the examples/ directory. Here’s an example:

```python
from skills_radar_plot.plot import create_skills_radar_plot
import matplotlib.pyplot as plt

categories = ["Problem-Solving", "Coding", "DevOps"]
scores = [5, 4, 3]

fig, ax = create_skills_radar_plot(categories, scores)
plt.show()
```

Run the example from the root dir:

```bash
python -m examples.example_input
```

## Running Tests

The project includes unit tests to ensure functionality and reliability.

### Run All Tests

To run all tests, use:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### Example Test Output

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Contributing

We welcome contributions!

## Project Structure

```
skills-radar-plot-generator/
├── LICENSE
├── README.md
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── main.py
├── skills_radar_plot/
│   ├── __init__.py
│   ├── plot.py
│   └── utils/
│       ├── __init__.py
│       ├── grid.py
│       └── axes.py
├── examples/
│   ├── example_input.py
├── outputs/               # Directory for generated images
│   └── (e.g., radar_plot_20250112_150000.png)
└── tests/
    ├── __init__.py
    ├── test_plot.py
    ├── test_utils.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Feedback

We value your feedback! If you encounter any issues or have feature requests, please open an issue.
