# Password Locker
#### This application allows users to securely store their usernames and passwords for various accounts such as social media accounts and email accounts,  03/2019
#### By **Ian Jaccojwang**
## Description
This is a terminal run application that allows the user to store login credentials for various accounts. It eliminates the trouble of memorising various passwords as the user only needs to remember one password to access all the credentials.
The user can:
* Create a secure account with login detaile: username and password.
* Store account login credentials
* Add login credentials
* View all login credentials
* Search for specific credentials
* Generate passwords for credentials
## Setup/Installation Requirements
### Prerequisites
* python3.6
* pip

### Cloning and running
* Clone the application using git clone(this copies the app onto your device). In terminal:

          $ git clone https://github.com/IJaccojwang/password-locker/
          $ cd Password-Locker

* Run the application:

          $ chmod +x run.py
          $ ./run.py

## Technologies Used
* Python 3.6
## Behaviour driven development/ input and output checking
The user will be able to log in and perform the following functions:
* Create an account with login details
* Store existing login credentials
* Add login credentials
* View all login credentials
* Search for specific credentials

| Behaviour |  Samlple Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| Create an account | Enter: ca | Enter your first name, last name, a username and password |
| Login in | Enter: li | Enter your usernamename and password |
| Navigate | Successful login | Choose an option: cc - Create Credential, vc - View Credential, va - View All Credentials, dc - Delete Credential, lo - log out |
| Creating a credential | Enter: cc | Enter the account name, username and password |
| View a credential | Enter: vc | Returns searched credential |
| View all credentials | Enter: va | Prints a list of saved credentials |
| Exit application | Enter: ex | Exit the current navigation stage |

## Support and contact details
For any questions, troubleshooting or contributions,  find me on:
* Mobile: +254702178825
* Email: danolago@gmail.com
### License
MIT License
Copyright (c) {2019} **Ian Olago Jaccojwang**
