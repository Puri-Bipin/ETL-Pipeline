import pandas as pd

# Load the CSV file
csv_file_path = 'SQL_SampleSuperstore_Data.csv'
df = pd.read_csv(csv_file_path)

# Perform data transformations
df['Total_Sales'] = df['Sales'].sum()  # Calculate total sales
df['Profit'] = df['Sales'] - df['Profit']  # Calculate profit
df['Average_Sales'] = df['Sales'].mean()  # Calculate average sales

sales_by_category = df.groupby('Category')['Sales'].sum().reset_index()  # Calculate sales by category
sales_by_segment = df.groupby('Segment')['Sales'].sum().reset_index()  # Calculate sales by customer segment
sales_by_country = df.groupby('Country')['Sales'].sum().reset_index()  # Calculate sales by country

# Save the updated data as a CSV file
transformed_csv_file_path = 'Transformed_SampleSuperstore_Data.csv'
df.to_csv(transformed_csv_file_path, index=False)

print('Sales by Category:')
print(sales_by_category)
print('Sales by Segment:')
print(sales_by_segment)
print('Sales by Country:')
print(sales_by_country)