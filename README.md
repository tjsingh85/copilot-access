# Copilot Access

This repository contains scripts and GitHub Actions workflows to manage GitHub Copilot seats for your organization.

## Functionality

The repository contains two main functionalities:

1. **Add Copilot Teams**: This functionality is implemented in the `add_teams.py` script and the corresponding GitHub Actions workflow in `.github/workflows/add-copilot-teams.yml`. It allows you to add teams to your GitHub Copilot plan. The teams to be added are specified in the body of an issue comment starting with '/team'.

2. **Add Copilot Users**: This functionality is implemented in the `add_users.py` script and the corresponding GitHub Actions workflow in `.github/workflows/add-copilot-users.yml`. It allows you to add individual users to your GitHub Copilot plan. The usernames to be added are specified in the body of an issue comment starting with '/user'.

Both workflows are triggered by the creation or editing of an issue comment. They use the `COPILOT_BILLING_TOKEN` secret to authenticate with the GitHub API and add the specified teams or users to the Copilot plan. The workflows then write a response message and status code to files, and post a confirmation comment on the issue.

## Prerequisites

Before using this repository, please ensure the following:

- You are an owner of the organization for which you want to configure GitHub Copilot.
- You have authenticated using an access token with the `manage_billing:copilot` scope.
- Your organization has a GitHub Copilot Business subscription and a configured suggestion matching policy.
- Users or teams that require access to GitHub Copilot are part of the org.

To use the workflows, you need to set the `COPILOT_BILLING_TOKEN` secret in your repository with a token that has the `manage_billing:copilot` scope.Here is the guide on [how to create a secret for a repository](https://docs.github.com/en/enterprise-cloud@latest/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)

## Usage

To add teams or users to your Copilot plan, create or edit an issue comment with the following format:

- To add teams, start your comment with '/team' followed by the team names.
- To add users, start your comment with '/user' followed by the usernames.

The workflows will then run and add the specified teams or users to your Copilot plan. They will post a confirmation comment on the issue with the result.

If you want to bulk add users using the csv file or want to Remove teams/users, you can use the [copilot-license-management action](https://github.com/marketplace/actions/copilot-license-management) from the marketplace
