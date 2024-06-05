# Step 1: Import necessary modules
import os
import json
from openai import OpenAI
from data import training_data, validation_data

# Step 2: Initialize the OpenAI client with the API key from environment variables
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

# Step 3: Define the names of the training and validation data files
training_file_name = "training_data.jsonl"
validation_file_name = "validation_data.jsonl"

# Step 4: Function to prepare data and write it to a JSONL file
def prepare_data(data: list[dict], file_name):
    with open(file_name, "w") as file:
        for item in data:
            file.write(json.dumps(item) + "\n")

# Step 5: Call the prepare_data function for both training and validation data
prepare_data(training_data, training_file_name)
prepare_data(validation_data, validation_file_name)

# Step 6: Upload the training data file to OpenAI and get the file ID
training_file_id = client.files.create(
  file=open(training_file_name, "rb"),
  purpose="fine-tune"
)

# Step 7: Upload the validation data file to OpenAI and get the file ID
validation_file_id = client.files.create(
  file=open(validation_file_name, "rb"),
  purpose="fine-tune"
)

# Step 8: Print the file IDs for reference
print("Training File ID:", training_file_id)
print("Validation File ID:", validation_file_id)

# Step 9: Create a fine-tuning job with the uploaded files and specific hyperparameters
response = client.fine_tuning.jobs.create(
  training_file=training_file_id.id,
  validation_file=validation_file_id.id,
  model="davinci-002",
  hyperparameters={
    "n_epochs": 15,
    "batch_size": 3,
    "learning_rate_multiplier": 0.3
  }
)

# Step 10: Retrieve the job ID and status from the response
job_id = response.id
status = response.status

# Step 11: Print the job ID and initial status
print("Fine-tuning Job ID:", job_id)
print("Initial Status:", status)

# Step 12: Import signal and datetime modules for handling interruptions and timestamps
import signal
import datetime

# Step 13: Define a signal handler to manage interruptions
def signal_handler(sig, frame):
  status = client.fine_tuning.jobs.retrieve(job_id).status
  print("Fine-tuning interrupted. Job is in", status, "state at", datetime.datetime.now())
  return

# Step 14: Print the start of event streaming
print("Event Streaming Started at", datetime.datetime.now(), "for Job ID:", job_id)

# Step 15: Set up the signal handler for keyboard interruptions
signal.signal(signal.SIGINT, signal_handler)

# Step 16: List events for the fine-tuning job and print them with timestamps
events = client.fine_tuning.jobs.list_events(fine_tuning_job_id=job_id)
try:
  for event in events:
    print(datetime.datetime.fromtimestamp(event.created_at), event.type, event.message)
except Exception as e:
  print("Stream interrupted:", e)

# Step 17: Import time module for sleep function
import time

# Step 18: Check the status of the fine-tuning job and wait if it is not in a terminal state
status = client.fine_tuning.jobs.retrieve(job_id).status
while status not in ["succeeded", "failed"]:
  print("Job is in", status, "state at", datetime.datetime.now())
  time.sleep(60)
  status = client.fine_tuning.jobs.retrieve(job_id).status
print("Job completed with status:", status)

# Step 19: Print the status of other fine-tuning jobs in the subscription
result = client.fine_tuning_jobs.list()
print("Found  ", len(result), "fine-tuning jobs in the subscription.")

# Step 20: Retrieve and print the ID of the fine-tuned model
fine_tuned_model_id = client.fine_tuning.jobs.retrieve(job_id).fine_tuned_model
print("Fine-tuned Model ID:", fine_tuned_model_id)
