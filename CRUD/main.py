from create_1 import create_user
from read_1 import user_info, all_users_info
from update_1 import user_update
from delete_1 import user_del
from help import user_help

help_txt = 'help.txt'

users_emails = []
users_storage = {}

action = input('Do yo need help? (yes/no) ')
if action == 'yes':
    user_help()

else:

    while True:

        action = input('Please enter create or read, or update, or delete actions: ')

        if action == 'create':

            print(f'action = {action}')

            email = input('Email: ')
            name = input('Name: ')
            password = input('Password: ')
            phone = input('Phone: ')

            users_emails = create_user(email,
                                       name,
                                       password,
                                       phone,
                                       users_emails,
                                       users_storage)

            print(f'users_emails = {users_emails}')
            print('users_storage:')

            for you_email in users_emails:
                print(you_email, users_storage[you_email])

        elif action == 'read_all':

            print(f'action = {action}')

            all_users_info(users_storage)

        elif action == 'read_user':

            print(f'action = {action}')

            user_e = input('Enter user email ')
            message = user_info(user_e, users_emails, users_storage)
            print(f'User: {message}')

        elif action == 'update':

            print(f'action = {action}')

            user_u = input('Enter user email ')
            param = input('Enter  value to change: ')

            message = user_update(param, user_u, users_emails, users_storage)
            print(f'User: {message}')

            print(f'users_emails = {users_emails}')
            print(f'users_storage = {users_storage}')

        elif action == 'delete':

            print(f'action = {action}')

            user_d = input('Enter user email ')
            message = user_del(user_d, users_emails, users_storage)
            print(f'User {message} delete')

        else:
            print('Please enter create or read, or update, or delete actions: ')

