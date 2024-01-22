import requests
import os

def get_env_variables():
    """Get environment variables."""
    token = os.getenv('COPILOT_BILLING_TOKEN')
    org = os.getenv('COPILOT_ORG')
    usernames = os.getenv('COPILOT_USERNAMES')
    return token, org, usernames

def process_usernames(usernames):
    """Process usernames: remove prefixes and '@', strip whitespaces."""
    if usernames.startswith("/users"):
        usernames = usernames.replace("/users", "", 1).strip()
    elif usernames.startswith("/user"):
        usernames = usernames.replace("/user", "", 1).strip()

    if usernames:
        usernames_list = usernames.split(',')
        selected_usernames = [username.strip().lstrip('@') for username in usernames_list if username.strip()]
    else:
        selected_usernames = []
    return selected_usernames

def add_users_to_copilot(token, org, selected_usernames):
    """Add selected users to Copilot plan."""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    data = {
        'selected_usernames': selected_usernames
    }

    response = requests.post(f'https://api.github.com/orgs/{org}/copilot/billing/selected_users', headers=headers, json=data)
    return response

def write_response_to_file(message, status_code):
    """Write the response message and status code to files."""
    with open('response_message.txt', 'w') as file:
        file.write(message)
    with open('response_status_code.txt', 'w') as file:
        file.write(str(status_code))

def main():
    """Main function to add users to Copilot plan."""
    token, org, usernames = get_env_variables()
    selected_usernames = process_usernames(usernames)
    response = add_users_to_copilot(token, org, selected_usernames)

    success_message = f'Successfully added selected users {selected_usernames} to Copilot Plan. You can now start using Copilot in your IDE ;)'
    failure_message = f'Failed to add selected users {selected_usernames} to Copilot Plan :(. Response code: {response.status_code}, message: {response.text}'

    message = success_message if response.status_code == 201 else failure_message
    print(message)

    write_response_to_file(message, response.status_code)

if __name__ == "__main__":
    main()