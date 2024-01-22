import requests
import os

def get_env_variables():
    """Get environment variables."""
    token = os.getenv('COPILOT_BILLING_TOKEN')
    org = os.getenv('COPILOT_ORG')
    teams = os.getenv('COPILOT_TEAMS')
    return token, org, teams

def process_teams(teams):
    """Process teams: remove prefixes and '@', strip whitespaces."""
    if teams.startswith("/teams"):
        teams = teams.replace("/teams", "", 1).strip()
    elif teams.startswith("/team"):
        teams = teams.replace("/team", "", 1).strip()

    if teams:
        teams_list = teams.split(',')
        selected_teams = [team.split('/')[-1].strip() for team in teams_list if team.strip()]
    else:
        selected_teams = []
    return selected_teams

def add_teams_to_copilot(token, org, selected_teams):
    """Add selected teams to Copilot plan."""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    data = {
        'selected_teams': selected_teams
    }

    response = requests.post(f'https://api.github.com/orgs/{org}/copilot/billing/selected_teams', headers=headers, json=data)
    return response

def write_response_to_file(message, status_code):
    """Write the response message and status code to files."""
    with open('response_message.txt', 'w') as file:
        file.write(message)
    with open('response_status_code.txt', 'w') as file:
        file.write(str(status_code))

def main():
    """Main function to add teams to Copilot plan."""
    token, org, teams = get_env_variables()
    selected_teams = process_teams(teams)
    response = add_teams_to_copilot(token, org, selected_teams)

    success_message = f'Successfully added selected teams {selected_teams} to Copilot Plan. You can now start using Copilot in your IDE ;)'
    failure_message = f'Failed to add selected teams {selected_teams} to Copilot Plan :(. Response code: {response.status_code}, message: {response.text}'

    message = success_message if response.status_code == 201 else failure_message
    print(message)

    write_response_to_file(message, response.status_code)

if __name__ == "__main__":
    main()