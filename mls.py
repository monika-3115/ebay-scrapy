import meilisearch
import pandas as pd
import time

# Initialize the Meilisearch client
client = meilisearch.Client('http://localhost:7700', 'NFPFKbKlE6JtdzMoRmVNnIE2VrDovkE6C851tURz9BM')

# Read the CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Add an 'id' column if it doesn't exist
if 'id' not in df.columns:
    df.insert(0, 'id', range(1, len(df) + 1))

# Print the DataFrame to inspect the data (optional)
print(df.head())

# Ensure all NaN values are handled (e.g., replace NaN with None)
df = df.where(pd.notnull(df), None)

# Convert the DataFrame to a list of dictionaries
documents = df.to_dict(orient='records')

# Optionally, print the documents to inspect them
print(documents[:30])

# Specify the primary key when adding the documents to the Meilisearch index
index = client.index('sample')
task = index.add_documents(documents, primary_key='id')

# Print the task information
print("Task Info:", task)

# Check the status of the task using the task UID
task_id = task.task_uid
status = client.get_task(task_id)
print("Task Status:", status)

# Wait until the task is processed (optional)
while status.status not in ['succeeded', 'failed']:
    time.sleep(1)
    status = client.get_task(task_id)
    print("Task Status:", status)

# Print the final status
print("Final Task Status:", status)












# import meilisearch
# import json
# import pandas as pd

# client = meilisearch.Client('http://localhost:7700', 'GeQLTHiDCelBxqTEQF64T1K6k7nL0xV7u5nZjp-3RTg')

# df = pd.read_csv("data.csv")
# # json_file = open('data.json', encoding='utf-8')
# # products = json.load(json_file)
# client.index('items').add_documents(df)