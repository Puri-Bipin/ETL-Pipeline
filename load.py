from google.cloud import bigquery
from transform import transformed_csv_file_path

# Google BigQuery details
project_id = 'projectid' # project ID of project in Google BigQuery
dataset_id = 'datasetid' #dataset ID of dataset in Google BigQuery
table_id = 'tabeleid'  #table ID of table in Google BigQuery

# Load the transformed CSV file into BigQuery
client = bigquery.Client(project=project_id)

# Define the BigQuery table schema (modify according to your CSV file structure)
schema = [
    bigquery.SchemaField('Row_ID', 'INTEGER'),
    bigquery.SchemaField('Order_ID', 'STRING'),
    bigquery.SchemaField('Order_Date', 'DATE'),
    bigquery.SchemaField('Ship_Date', 'DATE'),
    bigquery.SchemaField('Ship_Mode', 'STRING'),
    bigquery.SchemaField('Customer_ID', 'STRING'),
    bigquery.SchemaField('Customer_Name', 'STRING'),
    bigquery.SchemaField('Segment', 'STRING'),
    bigquery.SchemaField('Country', 'STRING'),
    bigquery.SchemaField('City', 'STRING'),
    bigquery.SchemaField('State', 'STRING'),
    bigquery.SchemaField('Postal_Code', 'STRING'),
    bigquery.SchemaField('Region', 'STRING'),
    bigquery.SchemaField('Product_ID', 'STRING'),
    bigquery.SchemaField('Category', 'STRING'),
    bigquery.SchemaField('Sub_Category', 'STRING'),
    bigquery.SchemaField('Product_Name', 'STRING'),
    bigquery.SchemaField('Sales', 'FLOAT'),
    bigquery.SchemaField('Quantity', 'INTEGER'),
    bigquery.SchemaField('Discount', 'FLOAT'),
    bigquery.SchemaField('Profit', 'FLOAT'),
    bigquery.SchemaField('Total_Sales', 'FLOAT'),
    bigquery.SchemaField('Average_Sales', 'FLOAT'),
]

# Create the BigQuery dataset if it doesn't exist
dataset_ref = client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)
if not client.get_dataset(dataset_ref):
    client.create_dataset(dataset)

# Define the job configuration
job_config = bigquery.LoadJobConfig(
    schema=schema,
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
)

# Start the load job
with open(transformed_csv_file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        dataset_ref.table(table_id),
        job_config=job_config
    )

load_job.result()  # Wait for the job to complete

# Check if the load job was successful
if load_job.state == 'DONE':
    print('Transformed CSV file loaded into BigQuery successfully.')
else:
    print('Transformed CSV file failed to load into BigQuery.')
