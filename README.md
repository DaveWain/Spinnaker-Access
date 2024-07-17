# Spinnaker Pipeline User Management

This script allows you to add new users to the `authorizedEmails` list of specified pipelines across multiple applications in Spinnaker. It uses the Spinnaker API to fetch, update, and push pipeline configurations.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Setup

1. **Clone the Repository:**

2. pip install requests

# Getting the Session Token
To interact with the Spinnaker API, you need a session token. Follow these steps to get it:

# Authenticate with Okta:

Go to your Spinnaker instance and log in via Okta.
Open the developer tools in your browser (F12 or right-click and select "Inspect").
Navigate to the "Network" tab.
Refresh the Spinnaker page and look for a request that includes session in the cookies.
Copy the session token from the request headers.
Update the Script:

Replace the placeholder in the get_session_cookie function with your session token.

# How to Use
1. Prepare the Applications List:

Create a text file named applications.txt (or any name you prefer) in the root directory.
List all application names in the file, one per line. Example:
- app1
- app2
- app3

2. Update Users to Add:

Update the new_users list with the email addresses of the users you want to add:
``new_users = ["new_user1@example.com", "new_user2@example.com"]``

3. Run the Script:
``python spin_access.py``

Script Details
- get_session_cookie: Function to return the session cookie. Update this with your session token.
- get_pipeline(application, pipeline_name): Fetches the pipeline configuration for a given application and pipeline name.
- update_pipeline(pipeline): Updates the given pipeline configuration.
- add_users_to_pipeline(pipeline, users): Adds the specified users to the authorizedEmails list in the pipeline variables.
- process_applications(applications, keywords): Processes each application and updates the specified pipelines with new users.
- read_applications_from_file(file_path): Reads the application names from the specified file.
- main: Main function to read the applications list, prompt for pipeline keywords, and call the processing function.

# Example Keywords Input

- Specific Pipelines:
  - Input: int,stag,prod
  - Action: Updates pipelines that include int, stag, or prod in their names.
- All Pipelines:
  - Input: all
  - Action: Updates all pipelines for the specified applications.
 
# Additional Notes
- Ensure your session token is valid. If the token expires, you will need to retrieve a new one using the steps mentioned above.
- The script assumes that the pipeline configurations include the variables section with the authorizedEmails field.
