import boto3
import os


credentials = os.path.expanduser('.aws/credentials')
config = os.path.expanduser('.aws/config')

if os.path.isfile(credentials):
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = credentials
if os.path.isfile(config):
    os.environ['AWS_CONFIG_FILE'] = config


def get_organization_accounts(event, context):
    boto3.setup_default_session()
    client = boto3.client('organizations')

    response = client.list_accounts(MaxResults=20)
    account_num = 1
    for account in response['Accounts']:
        print('Account: {}'.format(account_num))
        print('Name: {}'.format(account['Name']))
        print('ARN: {}'.format(account['Arn']))
        print('Email: {}\n'.format(account['Email']))
        account_num += 1


if __name__ == '__main__':
    get_organization_accounts(None, None)
