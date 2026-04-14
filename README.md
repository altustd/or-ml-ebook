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
│   ├── # Part I: Mathematical Foundations
│   ├── 01-foundations-linear-algebra.qmd
│   ├── 02-foundations-probability-statistics.qmd
│   ├── 03-foundations-modeling.qmd
│   ├── # Part II: Core Optimization Techniques
│   ├── 01-introduction-to-or-ml.qmd
│   ├── 02-linear-programming.qmd
│   ├── 03-integer-programming.qmd
│   └── 04-network-optimization.qmd
├── _book/                             # Rendered HTML output (generated)
├── _quarto.yml                        # Quarto book configuration
├── index.qmd                          # Book homepage
├── references.bib                     # Bibliography
└── requirements.txt                   # Python dependencies
```

---

## Quick Start

### Environment Setup

```bash
# Clone the repo
git clone https://github.com/altustd/or-ml-ebook.git
cd or-ml-ebook

# Activate the conda environment
conda activate /opt/homebrew/Caskroom/miniforge/base/envs/orml

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

### Part I: Mathematical Foundations

| Chapter | Title | Status |
|---|---|---|
| 1 | Linear Algebra Foundations | Draft |
| 2 | Probability and Statistics Foundations | Stub |
| 3 | Mathematical Modeling Principles | Draft |

### Part II: Core Optimization Techniques

| Chapter | Title | Status |
|---|---|---|
| 1 | Introduction to Operations Research and Machine Learning | Draft |
| 2 | Linear Programming | Draft |
| 3 | Integer Programming | Draft |
| 4 | Network Optimization | Draft |

### In Progress

| Part | Title |
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
