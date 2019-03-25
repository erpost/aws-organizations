import boto3
import os


os.environ['AWS_SHARED_CREDENTIALS_FILE'] = os.path.expanduser('.aws/credentials')
os.environ['AWS_CONFIG_FILE'] = os.path.expanduser('.aws/config')


def get_accounts(profile):
    boto3.setup_default_session(profile_name=profile)
    client = boto3.client('organizations')

    response = client.list_accounts(MaxResults=20)

    return response


if __name__ == '__main__':
    accounts = get_accounts('jau-org-admin')
    account_num = 1
    for account in accounts['Accounts']:
        print('Account: {}'.format(account_num))
        print('Name: {}'.format(account['Name']))
        print('ARN: {}'.format(account['Arn']))
        print('Email: {}\n'.format(account['Email']))
        account_num += 1
