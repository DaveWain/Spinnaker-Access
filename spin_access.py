import requests
import json

# Constants
BASE_URL = "https://"
HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

# New users to add
new_users = ["sample@email.com"]

def get_session_cookie():
    return "get_session_cookie"

def get_pipeline(application, pipeline_name):
    url = f"{BASE_URL}/applications/{application}/pipelineConfigs/{pipeline_name}"
    response = requests.get(url, headers=HEADERS, cookies={'session': get_session_cookie()})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get pipeline: {pipeline_name} in application: {application}. Status code: {response.status_code}")
        return None

def update_pipeline(pipeline):
    url = f"{BASE_URL}/pipelines/{pipeline['id']}"
    response = requests.put(url, headers=HEADERS, cookies={'session': get_session_cookie()}, data=json.dumps(pipeline))
    if response.status_code == 200:
        print(f"Successfully updated pipeline: {pipeline['name']}")
    else:
        print(f"Failed to update pipeline: {pipeline['name']}. Status code: {response.status_code}")

def add_users_to_pipeline(pipeline, users):
    if 'variables' in pipeline and 'authorizedEmails' in pipeline['variables']:
        current_emails = set(pipeline['variables']['authorizedEmails'].split(','))
        updated_emails = current_emails.union(set(users))
        pipeline['variables']['authorizedEmails'] = ','.join(updated_emails)
        update_pipeline(pipeline)
    else:
        print(f"Template or variables not found in pipeline: {pipeline['name']}")

def process_applications(applications, keywords):
    for application in applications:
        print(f"Processing application: {application}")
        url = f"{BASE_URL}/applications/{application}/pipelineConfigs"
        response = requests.get(url, headers=HEADERS, cookies={'session': get_session_cookie()})
        if response.status_code == 200:
            pipelines = response.json()
            for pipeline in pipelines:
                if 'all' in keywords or any(keyword in pipeline['name'] for keyword in keywords):
                    print(f"Processing pipeline: {pipeline['name']} in application: {application}")
                    add_users_to_pipeline(pipeline, new_users)
                    print("-" * 40)
        else:
            print(f"Failed to get pipelines for application: {application}. Status code: {response.status_code}")

def read_applications_from_file(file_path):
    with open(file_path, 'r') as file:
        applications = [line.strip() for line in file if line.strip()]
    return applications

def main():
    file_path = 'applications.txt'  # Path to your text file
    applications = read_applications_from_file(file_path)
    keywords_input = input("Enter the pipeline keywords (comma separated, e.g., int,stag,prod or 'all' for all pipelines): ")
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]
    process_applications(applications, keywords)

if __name__ == "__main__":
    main()
