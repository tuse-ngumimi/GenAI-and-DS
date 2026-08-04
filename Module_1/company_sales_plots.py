import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\Ngumimi\genai-ds\Module_1\company_sales_data.csv', encoding='latin1')

month_number = df['month_number'].tolist()


# Exercise 1
total_profit = df['total_profit'].tolist()

plt.plot(month_number, total_profit, label='Profit Data of Last Year', marker='o', markerfacecolor='black', linestyle='-', linewidth=3, color='black')
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.xticks(month_number)
plt.title('Company profit per month')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()



# Exercise 2: bathing soap and facewash subplot
bathing_soap = df['bathingsoap'].tolist()
facewash = df['facewash'].tolist()

# first plot
plt.subplot(1, 2, 1)
plt.plot(month_number, bathing_soap, label='Bathing Soap Sales Data',color='yellow', marker='o', linewidth=2)
plt.title('Bathing soap sales data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.xticks(month_number)
plt.legend()

# second plot 
plt.subplot(1, 2, 2)
plt.plot(month_number, facewash, label='Face Wash Sales Data', color='red', marker='o', linewidth=2)
plt.title('Face wash sales data')
plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.xticks(month_number)
plt.legend()

plt.tight_layout()
plt.show()
