# Company Sales Data Analysis - Module 3

## Overview
This project contains an exploratory data analysis of a company's sales data. The focus of this module is on applying data visualization techniques using Python's `matplotlib` and `seaborn` libraries to uncover business insights and format professional charts.

## Visualizations Generated
The analysis currently generates the following visualizations:

### 1. Total Profit per Month (Line Plot)
- **Output File:** `line_plot.png`
- **Description:** A styled line chart tracking the company's total profit across different months. Using Seaborn's `whitegrid` theme and Matplotlib's customization, this visualization helps in identifying financial trends and seasonal peaks throughout the year.
- **Key Findings:**
  - Profit holds fairly steady (₦183K–₦225K) from month 1 through month 6.
  - A sharp late-year surge follows: month 7 (₦295K), month 8 (₦361K), a dip in month 9 (₦234K), a drop in month 10 (₦267K), a peak in month 11 (₦413K), then a settle at ₦300K in month 12.
  - Profit roughly doubles from the first-half average to the last few months, suggesting a seasonal effect concentrated in months 7–8 and 11.

### 2. Total Units Sold vs Total Profit (Scatter Plot)
- **Output File:** `scatter_plot.png`
- **Description:** A scatter plot analyzing the correlation between the volume of units sold and the resulting total profit. This helps in understanding sales efficiency and profit margins across different performance thresholds.
- **Key Findings:**
  - Points trend upward and roughly linearly — more units sold generally means more profit.
  - The relationship isn't perfectly clean: month 7 sells fewer total units than several other months yet still posts a high profit.
  - This suggests product mix, not just volume, affects profit — some products likely carry a better margin than others.

### 3. Distribution of Monthly Sales by Product (Histograms)
- **Output File:** `histograms.png`
- **Description:** A 2×3 grid of histograms (with KDE curves) — one per product — showing how often each product's monthly sales fall into a given range of units. Each subplot's x-axis is units sold in a month; the y-axis is how many months fell in that range. A tall, narrow shape means sales are consistent month to month; a wide or flat shape means sales fluctuate a lot.
- **Key Findings:**
  - **Bathingsoap** is shifted far to the right (7,000–14,000 units) and is the widest distribution — it sells the most and varies the most.
  - **Toothpaste** clusters in a mid-to-high range (4,500–8,300 units), fairly steady.
  - **Facecream** sits in a moderate, tighter band (2,100–3,700 units).
  - **Facewash, shampoo, and moisturizer** are all bunched at the low end (1,100–3,600 units) with narrow, peaked shapes — low-volume, low-variance products.

### 4. Spread of Monthly Sales by Product (Box Plots)
- **Output File:** `box_plot.png`
- **Description:** A single chart with one box per product, plotting the median, interquartile range (the box), and the full range (whiskers) of monthly unit sales, side by side. The line inside each box is the median month; the box covers the middle 50% of months; the whiskers show the min/max, and any dots beyond them would be outlier months.
- **Key Findings:**
  - **Bathingsoap** has by far the tallest box and highest median — it's both the top seller and the most unpredictable product month to month.
  - **Toothpaste** has the second-highest median with a moderate spread.
  - **Facewash, shampoo, and moisturizer** have small, tight boxes near the bottom of the chart — consistent, but low-impact, products.
  - No extreme outlier points appear, meaning the variation is spread across the year rather than caused by one unusual month.

## Overall Takeaway
Bathingsoap is the company's primary sales driver and its main source of month-to-month volatility, closely followed by toothpaste. Facecream, facewash, shampoo, and moisturizer form a stable, low-volume baseline with little variation. The late-year profit surge (months 7–8, 11) likely reflects strong bathingsoap and toothpaste performance layered on top of that stable baseline, though product mix — not volume alone — appears to shape overall profit.

## Technologies Used
- **Python:** Primary programming language.
- **Pandas:** Used for data ingestion (`company_sales_data.csv`).
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