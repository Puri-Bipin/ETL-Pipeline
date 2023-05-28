import subprocess

# Execute extract.py
extract_process = subprocess.Popen(['python', 'extract.py'])

# Wait for extract.py to complete
extract_process.wait()

# Execute transform.py
transform_process = subprocess.Popen(['python', 'transform.py'])

# Wait for transform.py to complete
transform_process.wait()

# Execute load.py
load_process = subprocess.Popen(['python', 'load.py'])

# Wait for load.py to complete
load_process.wait()

print("ETL process completed successfully.")
