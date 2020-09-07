# Password_checker

#### Author: [Andiwo Edwin]

## Description

This project is a python application that manages  login, signup credentials and displaying accounts of a person i.e. social accounts and passwords for each account. It also stores the credentials of the user when they need it like password.


## User Stories
The user would like to.... :
* Create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Copy my credentials to clipboard.

## Installation / Setup instruction

**These Simple Instructions will get you a copy of the application running on your terminal.**

1. Get into the **Project Repository.**

2. Clone the project.

3. Get into project folder (cd into project).

4. If you have all the Pre-requisites you can run the application.

### Pre-requisites

**What things you need to install the application and how to install them.**

```
Python3.8
```

To Install **python 3.8** on terminal execute

```
apt-get install python3.8
```

```
apt-get install pip3
```

## Running the application

1. Navigate into the cloned folder using terminal and enter command `python3.8 Passwords.py` to run the app.
The app will open on terminal 

2. Follow and answer the prompts to use the application.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ python3.8 Password.py```|Hello! Welcome to your account list. What is your name?... | input your name and then it will give you the options bellow. <br>* cna ---  Create New Account * da ---  display accounts  * fa --- find accounts * ex --- exit the account|
|Select  can| input first name, last name, user account and password| f_name  + l_name  + " your account has been created |
|Select  da | This is to display accounts |  Enter ```fa```Abbreviations| This is to find account you just enter the account password and it will bring you the account<br>choose ```ex``` to exit your account|
|Display all stored credentials | Enter ```cna```|A list of all credentials that has been stored or will prompt user to fill. if you input wrong short code it will show you ```I really didn't get that. Please use the short codes``` |


## Built With

* [Python3.8](https://docs.python.org/3/)

## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :andiwoedwin@gmail.com

### License
*MIT licence*
Copyright (c) 2020 **Andiwo Edwin**