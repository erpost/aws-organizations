import boto3
import os


credentials = os.path.expanduser('.aws/credentials')
config = os.path.expanduser('.aws/config')

if os.path.isfile(credentials):
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = credentials
if os.path.isfile(config):
    os.environ['AWS_CONFIG_FILE'] = config


def get_accounts(profile):
    boto3.setup_default_session(profile_name=profile)
    client = boto3.client('organizations')

    response = client.list_accounts(MaxResults=20)

    return response


if __name__ == '__main__':
    accounts = get_accounts('org-readonly')
    account_num = 1
    for account in accounts['Accounts']:
        print('Account: {}'.format(account_num))
        print('Name: {}'.format(account['Name']))
        print('ARN: {}'.format(account['Arn']))
        print('Email: {}\n'.format(account['Email']))
        account_num += 1
