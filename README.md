# myDiary

## myDiary-db

This api allows the diary users to register and access their accounts.

### Features

- Register a user
- Login a user

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

### Built with and by:

- [Flask](https://flask.pocoo.org/) - Python webframework
- [PostgreSQL](https://www.postgresql.org/)- Open source relational database

Author: Douglas Kato.