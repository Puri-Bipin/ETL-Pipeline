import pandas as pd
import pyodbc

# SQL Server connection details
sql_server_driver = '{ODBC Driver 17 for SQL Server}' #ODBC driver for SQL Server
sql_server_name = 'DESKTOP-2EF0EHD\SQLEXPRESS' #SQL Server Name
sql_server_database = 'sample_superstore' #Database name

# Connect to SQL Server
connection_string = f'Driver={sql_server_driver};Server={sql_server_name};Database={sql_server_database};Trusted_Connection=yes;'
connection = pyodbc.connect(connection_string)

# Execute SQL query and retrieve data
query = '''
SELECT *
FROM dbo.sample_superstore
'''
df = pd.read_sql_query(query, connection)

# Save the data as a CSV file
csv_file_path = 'SQL_SampleSuperstore_Data.csv' 
df.to_csv(csv_file_path, index=False)
