import pandas as pd

data = pd.read_csv(r'C:\Users\Ngumimi\genai-ds\Module_2\realtor-data.csv', encoding='latin1')

print(data.head(10))
print()
print(data.describe())
print()
print("The columns present in this dataset include: ", data.columns.tolist())

print("************************" * 5)
print("\nMean Values")
print("\nBelow is the Average Housing Price:")
print(data['price'].mean())

print("\nBelow is the Average Land Size (in acres) :")
print(data['acre_lot'].mean())

print("\nBelow is the Average Living Space Size (in square feet) :")
print(data['house_size'].mean() )


print("************************" * 5)
print("\nBelow are the median values for the numeric columns:")
print("Median housing price: ", data['price'].median())
print("Median land size (in acres): ", data['acre_lot'].median())
print("Median living space (in square feet): ", data['house_size'].median())


print("************************" * 5)
print("\nBelow are the mode values for the numeric columns:")
print("Mode housing price: ", data['price'].mode().tolist())
print("Mode land size (in acres): ", data['acre_lot'].mode().tolist())
print("Mode living space (in square feet): ", data['house_size'].mode().tolist())

print("\nBelow are the mode values for categorical columns:")
cat_columns = ['brokered_by', 'city', 'bed', 'state', 'street', 'property_type', 'bath', 'zip_code']
for column in cat_columns:
  if column in data.columns:
   print(f"Mode {column}:", data[column].mode().tolist())

print("************************" * 5)
print("\nStandard deviation for numeric columns:")
print(data[['price', 'acre_lot', 'house_size']].std())

print("************************" * 5)
print("\nCorrelation matrix for numeric features:")
print(data.corr())
