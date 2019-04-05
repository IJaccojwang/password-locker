#!/usr/bin/env python3.6
from user import User
from cred import Cred

def create_user(fname, lname, phone, email):
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

def delete_user():
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user():
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)

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
    return Cred.find_by_number(number)

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
