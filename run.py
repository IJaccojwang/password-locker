#!/usr/bin/env python3.6
from user import User
from cred import Cred
import string
import random

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

def create_cred(username, accnt, uname, pword):
    '''
    Function to create new credentials
    '''
    new_cred = Cred(username, accnt, uname, pword)
    return new_cred

def save_cred(cred):
    '''
    Function to save cred
    '''
    cred.save_cred()

def delete_cred(cred):
    '''
    Function to delete cred
    '''
    cred.delete_cred()

def find_cred(username_login, account):
    '''
    Function that finds a cred by number and returns the cred
    '''
    return Cred.find_by_account(username_login, account)

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

def generate_password(length):
    pwd = []
    count = 0
    while (count < length/3):
        pwd.append(random.choice(string.ascii_lowercase))
        pwd.append(random.choice(string.ascii_uppercase))
        pwd.append(str(random.randint(0,9)))
        count = count + 1
    random.shuffle(pwd)
    return ''.join(pwd)



def main():
    print("Hello, welcome to Password Locker.")

    while True:
        print("Use the following short codes for navigation: ca - create a new account, da - delete your account, li - log in to your account, exa - exit application")
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
                print("Enter your password")
                password = input()
                if password == search_user.password_login:
                    print(f"Are you sure you want to delete {search_user.first_name} {search_user.last_name}")
                    print("y - yes, n - no")
                    yesNo = input().lower()
                    if yesNo == 'y':
                        delete_user(search_user)
                        print(f"{search_user.first_name} {search_user.last_name} has been deleted")
                    elif yesNo == 'n':
                        print("User still present")
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

                    while True:
                        print("What would you like to do: cc - create a new credential, dc - delete credential, vc - view credential, va - view all credentials, lo - log out")
                        acc_nav = input()

                        if acc_nav == 'cc':
                            print ("Account type eg. Faceook ....")
                            account = input()

                            print("Account username ...")
                            uname = input()

                            print("Account password...")
                            print("Would you like an auto generated Password?")
                            print("y - Yes, n - No")
                            decision = input().lower()
                            if decision == 'y':
                                print("Please enter desired password length")
                                length = int(input())
                                pword = generate_password(length)
                                print(f"Your new password for {account} is {pword}. Don't forget.")
                            elif decision == 'n':
                                print("Please enter your new password")
                                pword = input()
                            else:
                                print("Use either y or n")

                            print('\n')
                            save_cred(create_cred(username, account, uname, pword))
                            print('\n')

                            print('\n')
                            print(f"New Credentials for {account} created")
                            print('\n')

                        elif acc_nav == 'dc':
                            print('Enter the account name of the credential you would like to delete')
                            delete_name = input()
                            if check_existing_creds(delete_name):
                                search_cred = find_cred(delete_name)
                                if search_cred.username_login == username:
                                    delete_cred(search_cred)
                                    print(f"{search_cred.account} credentails have been deleted")
                                else:
                                    print ("The credential does not exist")
                                    break
                            else:
                                print("Account does not exist")

                        elif acc_nav == 'vc':
                            print("Enter the account you want to search for")
                            find_name = input()
                            search_cred = find_cred(username, find_name)
                            if check_existing_creds(find_name):
                                print(f"{search_cred.account}")
                                print('-'*20)
                                print(f"Username.......{search_cred.username_cred}")
                                print(f"Password.......{search_cred.password_cred}")
                            else:
                                print("That contact does not exist")

                        elif acc_nav == 'va':
                            if display_creds():
                                print("Here are your credentials:")
                                print('\n')

                                for cred in display_creds():
                                    if cred.username_login == username:
                                        print(f"{cred.account} -- Username: {cred.username_cred} | Password: {cred.password_cred}")
                                        print('\n')
                            else:
                                print("No credentials available")

                        elif acc_nav == 'lo':
                            print("You have successfully logged out of your account. See you next time!")
                            break

                        else:
                            print("Please use one of the navigation shortcodes provided")


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
