

def user_info(email, users_emails, users_storage):

    if email in users_emails:

        message = f'User-email = {email}' \
                  f' \n ' \
                  f'User_info: {users_storage[email]}'
        return message

    else:
        message = f'No user with email: {email}'
        return message


def all_users_info(users_storage):

    message = ''

    for k, v, in users_storage.items():

        users_emails = f'User_email {k}'
        user_info_1 = f'User_info {v}'

        print(users_emails, '\n', user_info_1)
