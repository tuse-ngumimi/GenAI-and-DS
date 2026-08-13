import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv(r'C:\Users\Ngumimi\genai-ds\Module_3\company_sales_data.csv', encoding='latin1')

sbn.set_theme(style="whitegrid")

# Below is the lineplot
plt.figure(figsize=(9, 5))
plt.plot(df['month_number'], df['total_profit'], marker='o', color="#2D39A3", linewidth=3)
plt.title('Total Profit per Month', fontsize=13, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.xticks(df['month_number'])
plt.tight_layout()
plt.savefig('line_plot.png', dpi=150)
plt.show()

# Below is the scatter plot 
plt.figure(figsize=(8, 5))
plt.scatter(df['total_units'], df['total_profit'], color="#570D5A", s=80, edgecolor='black')
plt.title('Total Units Sold vs Total Profit', fontsize=14, fontweight='bold')
plt.xlabel('Total Units Sold')
plt.ylabel('Total Profit')
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=150)
plt.show()

