import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Ngumimi\genai-ds\Module_3\company_sales_data.csv', encoding='latin1')

sns.set_theme(style="whitegrid")

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
plt.figure(figsize=(9, 5))
plt.scatter(df['total_units'], df['total_profit'], color="#570D5A", s=80, edgecolor='black')
plt.title('Total Units Sold vs Total Profit', fontsize=14, fontweight='bold')
plt.xlabel('Total Units Sold')
plt.ylabel('Total Profit')
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=150)
plt.show()

#  Below is the histogram 
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

fig, axes = plt.subplots(2, 3, figsize=(15, 8))
for ax, product in zip(axes.flatten(), products):
    sns.histplot(df[product], kde=True, ax=ax, color="#A13A0B", bins=6)
    ax.set_title(product.capitalize())
plt.suptitle('Distribution of Monthly Sales by Product', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('3_histograms.png', dpi=150, bbox_inches='tight')
plt.show()

# Below are the box plots for company sales data
melted = df[products].melt(var_name='Product', value_name='Units Sold')

plt.figure(figsize=(11, 6))
sns.boxplot(data=melted, x='Product', y='Units Sold', hue='Product', palette='Set2', legend=False)
plt.title('Spread of Monthly Sales by Product', fontsize=14, fontweight='bold')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('4_box_plots.png', dpi=150)
plt.show()