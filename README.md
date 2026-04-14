# Modern Operations Research with Python

**Optimization · Machine Learning · Simulation**

*Author: Troy Altus*
*Last Updated: April 14, 2026*

---

## Overview

This repository contains a comprehensive ebook that bridges **classical Operations Research**
with **modern Machine Learning** using Python. It covers foundational optimization techniques
through advanced topics including stochastic programming, nonlinear optimization, and
prescriptive analytics.

Built with [Quarto](https://quarto.org), rendered as HTML and PDF.

---

## Project Structure

```bash
or-ml-ebook/
├── book/                              # Quarto chapter files (.qmd)
│   ├── 01-introduction-to-or-ml.qmd
│   ├── 02-linear-programming.qmd
│   ├── 03-integer-programming.qmd
│   ├── 04-network-optimization.qmd
│   ├── 05-stochastic-optimization.qmd
│   ├── 06-nonlinear-optimization.qmd
│   ├── 07-supervised-learning.qmd
│   ├── 08-unsupervised-learning.qmd
│   ├── 09-reinforcement-learning.qmd
│   ├── 10-simulation-optimization.qmd
│   └── 11-prescriptive-analytics.qmd
├── notebooks/                         # Source Jupyter notebooks (.ipynb)
├── _book/                             # Rendered HTML output (generated)
├── _quarto.yml                        # Quarto book configuration
├── index.qmd                          # Book homepage
├── references.bib                     # Bibliography
├── requirements.txt                   # Python dependencies
├── convert_all_notebooks.py           # Notebook to QMD conversion utility
└── test_all_chapters.py               # Chapter render validation
```

---

## Quick Start

### Environment Setup

```bash
# Clone the repo
git clone https://github.com/altustd/or-ml-ebook.git
cd or-ml-ebook

# Activate the virtual environment
source ~/or-ml-opt/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Render the Book

```bash
# Full render to _book/
quarto render

# Live preview with hot reload (recommended during authoring)
quarto preview

# Open rendered book in browser
open _book/index.html
```

---

## Content

### Available Now

**Foundations**

| Chapter | Title |
|---|---|
| 1 | Introduction to Operations Research and Machine Learning |
| 2 | Linear Programming |
| 3 | Integer Programming |
| 4 | Network Optimization |

### In Progress

| Section | Title |
|---|---|
| Advanced Optimization | Stochastic Optimization |
| Advanced Optimization | Nonlinear Optimization |
| Machine Learning for OR | Supervised Learning |
| Machine Learning for OR | Unsupervised Learning |
| Machine Learning for OR | Reinforcement Learning |
| Integration & Applications | Simulation Optimization |
| Integration & Applications | Prescriptive Analytics |

---

## Dependencies

Core Python libraries used throughout:

| Purpose | Libraries |
|---|---|
| Linear & Integer Programming | `pulp` |
| Nonlinear Optimization | `scipy`, `cvxpy` |
| Network Optimization | `networkx` |
| Machine Learning | `scikit-learn` |
| Numerical Computing | `numpy`, `pandas` |
| Visualization | `matplotlib`, `seaborn` |
| Simulation | `simpy` |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Tech Stack

- **Python 3.11+** on Apple M4
- **Quarto** for document rendering (HTML + PDF)
- **PuLP / CBC** as the default LP/MIP solver
- **Jupyter** notebooks as authoring source

---

## License

See [LICENSE](LICENSE) for details.

---

*Built with Python, PuLP, SciPy, scikit-learn, and Quarto.*
