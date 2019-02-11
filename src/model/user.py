import fileReader

def is_user_registered(user_name, password):
    existing_users = fileReader.get_user_names_and_passwords()
    current_user = user_name + ":" + password
    return user_exists(existing_users,current_user)

#----------------------------------------------------------------------------------------
def _user_exists(existing_users, current_user):
    for user in existing_users
        if user == current_user:
            return True
    return False
