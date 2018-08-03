# myDiary

[![Build Status](https://travis-ci.org/kdaglas/myDiary-db.svg?branch=develop)](https://travis-ci.org/kdaglas/myDiary-db)

## myDiary-db

This api allows the diary users to register and access their accounts.

### Features

- Register a user
- Login a user
- View all entries from the database
- View contents of an entry
- Add an entry
- Modify an entry
- Delete an entry

### Requirements

Python 2.7.x and above
Note: Python needs to be installed globally (not in the virtual environment)
pip: A python package used to install modules specified in the requirements text file.

### Getting started:

Begin by cloning the repository:
```
https://github.com/kdaglas/myDiary-db.git
```
Install postgreSQL on your machine
Create a database by typing this in your postgres shell
```
    CREATE DATABASE mydiary;
    CREATE DATABASE testdb;
```
Go into the parent directory, create a virtual environment, activate it and then use a pip command to install the requirements, below are the steps to take:
```
    $ cd myDiary-db
    $ virtualenv envn
    $ source envn/bin/activate
    $ pip install -r requirements.txt
```
Run the app by running the line below in your shell;
```
    $ python run.py
```

### Testing

To run tests, activate your virtual environment and in the commandline shell, run:
```
    $ nosetests
```
#### Endpoints to create a user account and login into the application
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/register | True | Create a user account
POST | /api/v1/login | True | Login a user

#### Endpoints to add, view and modify user entries
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/v1/diaries | False | Add an entry
GET | /api/v1/diaries | False | View all entries for a logged in user
GET | /api/v1/diaries/<entry_id> | False | View a single entry for a logged in user
PUT | /api/v1/diaries/<entry_id> | False | Modify a single entry for a logged in user
DELETE | /api/v1/diaries/<entry_id> | False | Delete a single entry for a logged in user

### Built with and by:

- [Flask](https://flask.pocoo.org/) - Python webframework
- [PostgreSQL](https://www.postgresql.org/)- Open source relational database

Author: Douglas Kato.