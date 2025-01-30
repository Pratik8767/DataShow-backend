# DataShow 
#Data Visualization Project (Python &amp; Flutter)

A streamlined tool for preprocessing datasets, handling missing values, and generating clean data reports with visualization capabilities.

![Workflow Diagram](Blank_diagram.png) *Add your workflow diagram here*

## Features ✨
- **File Handling**  
  - Upload datasets (up to 10MB)  
  - Preserve original data integrity
  - Export cleaned data as CSV/PNG

- **Data Cleaning**  
  - Remove duplicate entries  
  - Handle missing values (NaN) through multiple strategies:
    - Mean/Median/Mode imputation
    - Custom "unknown" placeholder
  - Cleanup summary statistics:
    - Rows/columns modified
    - Missing values filled
    - Pre vs. Post-cleanup comparison
  - Undo functionality for accidental cleanups

- **Data Analysis**  
  - Basic file info: rows, columns, memory usage  
  - Statistical overview:
    - Max/Min/Average values
    - Data type distribution
  - Data preview 

- **Visualization** 🔍
  - Distribution charts
  - Outlier detection plots
  - Data composition graphs
  - Interactive data exploration

## Installation 📥
```bash
git clone [your-repository-url]
pip install -r requirements.txt
