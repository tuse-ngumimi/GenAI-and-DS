# Company Sales Data Analysis - Module 3

## Overview
This project contains an exploratory data analysis of a company's sales data. The focus of this module is on applying data visualization techniques using Python's `matplotlib` and `seaborn` libraries to uncover business insights and format professional charts.

## Visualizations Generated
The analysis currently generates the following visualizations:

### 1. Total Profit per Month (Line Plot)
- **Output File:** `line_plot.png`
- **Description:** A styled line chart tracking the company's total profit across different months. Using Seaborn's `whitegrid` theme and Matplotlib's customization, this visualization helps in identifying financial trends and seasonal peaks throughout the year.

### 2. Total Units Sold vs Total Profit (Scatter Plot)
- **Output File:** `scatter_plot.png`
- **Description:** A scatter plot analyzing the correlation between the volume of units sold and the resulting total profit. This helps in understanding sales efficiency and profit margins across different performance thresholds.

## Technologies Used
- **Python:** Primary programming language.
- **Pandas:** Used for data ingestion (`company_sales_data.csv`) 
- **Matplotlib (Pyplot):** Core library for building the figure structures, titles, labels, and exporting the high-resolution (150 DPI) charts.
- **Seaborn:** Utilized to set the foundational aesthetic themes for cleaner, more readable visuals.

## Setup and Execution
1. Ensure the required data science libraries are installed in your environment:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Verify that the dataset `company_sales_data.csv` is located in your `genai-ds/Module_3/` directory.
3. Execute the Python script. The plots will render on screen and automatically save as `.png` images in your working directory.

---
*Authored by Ngumimi Bethel*