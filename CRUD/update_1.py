

def user_update(param, email, users_emails, users_storage):

    message = ''

    execute = True

    while execute:

        if email in users_emails:

            if param == 'email':
                new_email = input('Enter new email: ')

                if new_email in users_emails:
                    print(f'Incorrect {param}')

                else:
                    users_storage[new_email] = users_storage.pop(email)
                    index = users_emails.index(email)
                    users_emails[index] = new_email

            elif param == 'name':
                users_storage[email]['name'] = input('Enter new name: ')
                execute = False
            elif param == 'password':
                users_storage[email]['password'] = input('Enter new password: ')
                execute = False
            elif param == 'phone':
                users_storage[email]['phone'] = input('Enter new phone: ')
                execute = False
            else:
                message = f'Incorrect param value {param}'
                execute = False

        else:
            message = f'No user with email: {email}'
            execute = False

    return message


