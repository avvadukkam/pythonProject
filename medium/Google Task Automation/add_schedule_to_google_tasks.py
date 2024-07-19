import os
import json
import google.auth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the scope and token/credentials paths
SCOPES = ['https://www.googleapis.com/auth/tasks']
TOKEN_PATH = 'token.json'
CREDENTIALS_PATH = 'credentials.json'


# Authenticate and build the service
def authenticate_google_tasks():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as token:
            creds = google.auth.load_credentials_from_file(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    service = build('tasks', 'v1', credentials=creds)
    return service


# Create a new task list
def create_task_list(service, task_list_name):
    tasklist = {
        'title': task_list_name
    }
    result = service.tasklists().insert(body=tasklist).execute()
    return result['id']


# Add tasks from the text file to the task list
def add_tasks_from_file(service, task_list_id, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.strip():
            task = {
                'title': line.strip()
            }
            service.tasks().insert(tasklist=task_list_id, body=task).execute()


def main():
    service = authenticate_google_tasks()
    task_list_id = create_task_list(service, 'Weekly Schedule')
    add_tasks_from_file(service, task_list_id, 'schedule.txt')


if __name__ == '__main__':
    main()
