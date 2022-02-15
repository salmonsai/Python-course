

def user_del(email, users_emails, users_storage):

    message = ''

    if email in users_emails:

        message = f'User-email = {email}' \
                  f' \n ' \
                  f'User_info: {users_storage[email]}'

        users_storage.pop(email)
        users_emails.remove(email)

    else:
        message = f'No user with email: {email}'

    return message
