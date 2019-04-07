#!/usr/bin/env python3.6
from user import User
from cred import Cred

def create_user(fname, lname, usrname, pssword):
    '''
    Function to create new user
    '''
    new_user = User(fname, lname, usrname, pssword)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(number):
    '''
    Function to check is a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def create_cred(accnt, uname, pword):
    '''
    Function to create new cred
    '''
    new_cred = Cred(accnt, uname, pword)
    return new_cred

def save_cred(cred):
    '''
    Function to save cred
    '''
    cred.save_cred()

def delete_cred():
    '''
    Function to delete cred
    '''
    cred.delete_cred()

def find_cred():
    '''
    Function that finds a cred by number and returns the cred
    '''
    return Cred.find_by_account(account)

def check_existing_creds(number):
    '''
    Function to check is a cred exists with that number and return a Boolean
    '''
    return Cred.cred_exist(number)

def display_creds():
    '''
    Function that returns all saved creds
    '''
    return Cred.display_creds()



def main():
    print("Hello, welcome to Password Locker.")
    print("Use the following short codes for navigation: ca - create a new account, da - delete your account, li - log in to your account, exa - exit application")

    while True:
        short_code = input()
        if short_code == 'ca':
            print('Please fill in the following details to create a new account')
            print("New User")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Username...")
            username = input()

            print("Ensure your password is secure by using uncommon passwords")
            print("Password ...")
            password = input()

            print('\n')
            save_user(create_user(f_name, l_name, username, password))
            print('\n')

            print('\n')
            print(f"New User {f_name} {l_name} created")
            print('\n')

        elif short_code == 'da':
            print('Enter the username of the account you would like to delete')
            delete_name = input()
            if check_existing_users(delete_name):
                search_user = find_user(delete_name)
                delete_user(search_user)
                print(f"{search_user.first_name} {search_user.last_name} has been deleted")
            else:
                print("Account does not exist")


        elif short_code == 'li':
            print("Welcome to log in")
            print("Enter your username: ")
            username = input()
            if check_existing_users(username):
                print("Enter your password:")
                password = input()
                search_user = find_user(username)
                if (password == search_user.password_login):
                    print(f"Welcome {search_user.first_name} {search_user.last_name}")
                else:
                    print("Sorry, wrong password")
            else:
                print("Account does not exist")


        elif short_code == 'exa':
            print('Bye')
            break
        else:
            print("Please use one of the shortcodes provided")


if __name__ == '__main__':

    main()
