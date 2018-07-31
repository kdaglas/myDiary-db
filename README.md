# myDiary

## myDiary-db

This api allows the diary users to register and access their accounts.

### Feautures

- Register a user
- Login a user

### Requirements

Python 2.7.x and above
Note: Python needs to be installed globally (not in the virtual environment)

### How to use:

Begin by cloning the repository:
```
https://github.com/kdaglas/myDiary-db.git
```
Go into the folder, create a virtual environment, activate it and then use a pip command to install the requirements and run the app; below are the steps to take:
```
    $ cd myDiary-db
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```
Install postgreSQL on your machine
Create a database by typing this in your postgres shell
```
    CREATE DATABASE your_own_db;
```


### Built with and by:

- [Flask](https://flask.pocoo.org/) - Python webframework
- [PostgreSQL](https://www.postgresql.org/)- Open source relational database