# 🐍 Learning Python

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.0-013243?style=for-the-badge&logo=numpy)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.0-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0-0C55A1?style=for-the-badge)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**A comprehensive repository for mastering Python fundamentals and data analysis libraries**

[Explore](#-topics-covered) • [Quick Start](#-quick-start) • [Progress](#-learning-progress) • [Support](#-support)

</div>

---

## 📖 About

Welcome to my **Learning Python** repository! 🚀 This repository contains my practice programs, detailed notes, and mini-projects while learning Python from beginner to advanced concepts. It's designed for anyone looking to build a strong foundation in data analysis and scientific computing.

---

## 🎯 Topics Covered

<table>
  <tr>
    <td width="33%">
      <h3>🔢 NumPy</h3>
      <ul>
        <li>Arrays & Array Operations</li>
        <li>Indexing & Slicing</li>
        <li>Mathematical Functions</li>
        <li>Statistical Operations</li>
        <li>Random Module</li>
      </ul>
    </td>
    <td width="33%">
      <h3>📊 Matplotlib</h3>
      <ul>
        <li>Line Plots</li>
        <li>Bar Charts</li>
        <li>Scatter Plots</li>
        <li>Pie Charts & Histograms</li>
        <li>Subplots & Customization</li>
      </ul>
    </td>
    <td width="33%">
      <h3>🐼 Pandas</h3>
      <ul>
        <li>Series & DataFrame</li>
        <li>Reading CSV Files</li>
        <li>Data Cleaning</li>
        <li>Filtering & Sorting</li>
        <li>Grouping & Analysis</li>
      </ul>
    </td>
  </tr>
</table>

---

## 📁 Repository Structure

```
📦 learning-python
 ├── 📂 numpy/
 │   ├── arrays.py
 │   ├── operations.py
 │   ├── statistics.py
 │   └── ...
 ├── 📂 matplotlib/
 │   ├── basic_plots.py
 │   ├── subplots.py
 │   ├── customization.py
 │   └── ...
 ├── 📂 pandas/
 │   ├── dataframe_basics.py
 │   ├── data_cleaning.py
 │   ├── data_analysis.py
 │   └── ...
 ├── README.md
 └── requirements.txt
```

---

## 🎓 Learning Goals

| Goal | Status |
|------|--------|
| ✅ Master Python fundamentals | Completed |
| ✅ Learn NumPy array operations | Completed |
| ✅ Create visualizations with Matplotlib | Completed |
| 🔄 Advanced Pandas data analysis | In Progress |
| ⏳ Machine Learning fundamentals | Coming Soon |
| ⏳ Web scraping & APIs | Coming Soon |

---

## 🛠️ Technologies & Tools

<div align="center">

| Technology | Purpose |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white) | Core Language |
| ![NumPy](https://img.shields.io/badge/NumPy-Data_Processing-013243?logo=numpy) | Numerical Computing |
| ![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas) | Data Manipulation |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-0C55A1) | Data Visualization |
| ![VS Code](https://img.shields.io/badge/VS_Code-Editor-0078D4?logo=visual-studio-code) | Development |

</div>

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sumittiruwa/learning_Python_from_apna_college.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd learning_Python_from_apna_college
   ```

3. **Install required libraries**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or individually:
   ```bash
   pip install numpy matplotlib pandas
   ```

4. **Run any Python file**
   ```bash
   python filename.py
   ```

### Example Usage

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy example
arr = np.array([1, 2, 3, 4, 5])
print(f"Mean: {np.mean(arr)}")

# Pandas example
df = pd.read_csv('data.csv')
print(df.head())

# Matplotlib example
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

---

## 📈 Learning Progress

### Completed ✅

- [x] **Python Basics**
  - Variables, data types, operators
  - Control flow (if/else, loops)
  - Functions and modules
  - File handling

- [x] **NumPy**
  - Array creation and manipulation
  - Mathematical operations
  - Statistical functions
  - Broadcasting and vectorization

- [x] **Matplotlib**
  - Basic 2D plotting
  - Multiple subplots
  - Styling and customization
  - Different chart types

### In Progress 🔄

- [ ] **Pandas Advanced**
  - Complex data transformations
  - Time series analysis
  - Merging and joining datasets
  - Performance optimization

### Coming Soon ⏳

- [ ] Advanced Python Libraries
- [ ] Machine Learning Basics
- [ ] Data Science Projects
- [ ] Web Scraping & APIs
- [ ] Database Integration

---

## 📚 Learning Resources

Here are some helpful resources I've used:

- **Official Documentation**
  - [Python Docs](https://docs.python.org/3/)
  - [NumPy Guide](https://numpy.org/doc/)
  - [Pandas Documentation](https://pandas.pydata.org/docs/)
  - [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

- **Recommended Courses**
  - Apna College - Python Complete Course
  - Real Python Tutorials
  - DataCamp Python Courses

---

## 💡 Tips & Best Practices

- **Experiment freely** - Try different approaches and learn from mistakes
- **Read documentation** - Official docs are your best friend
- **Practice regularly** - Consistency is key to mastery
- **Build projects** - Apply knowledge to real-world problems
- **Join communities** - Learn from others and share your progress

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this repository:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you found this repository helpful:

- **Give it a star** ⭐ - It helps others discover the project
- **Share with friends** - Help spread the knowledge
- **Follow for updates** - Stay tuned for new content
- **Report issues** - Help improve the repository

---

## 📞 Get in Touch

Have questions or suggestions? Feel free to:

- Open an [Issue](https://github.com/sumittiruwa/learning_Python_from_apna_college/issues)
- Start a [Discussion](https://github.com/sumittiruwa/learning_Python_from_apna_college/discussions)
- Connect on [LinkedIn](https://linkedin.com)

---

<div align="center">

### Happy Coding! 🚀

**Made with ❤️ by [Your Name]**

*Last updated: June 2026*

</div>