# myDiary

[![Build Status](https://travis-ci.org/kdaglas/myDiary.svg?branch=myDiary-api)](https://travis-ci.org/kdaglas/myDiary)
[![Coverage Status](https://coveralls.io/repos/github/kdaglas/myDiary/badge.svg)](https://coveralls.io/github/kdaglas/myDiary)
[![Maintainability](https://api.codeclimate.com/v1/badges/09c2196156b65f05827c/maintainability)](https://codeclimate.com/github/kdaglas/myDiary/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/09c2196156b65f05827c/test_coverage)](https://codeclimate.com/github/kdaglas/myDiary/test_coverage)

An online journal where users can pen down their thoughts and feelings

https://kdaglas.github.io/myDiary/UI/signup_page.html
This is the link to the demo

## myDiary-api

This api allows the diary users to add an entry, modify an entry, view a single entry and view all entries.

### Feautures

- Register a user
- Login a user
- View all entries to the diary
- View contents of an entry
- Add an entry
- Modify an entry

### Requirements

Python 2.7.x and above
Note: Python needs to be installed globally (not in the virtual environment)

### How to use:

Begin by cloning the repository:
```
https://github.com/kdaglas/myDiary.git
```
Go into the folder, create a virtual environment, activate it and then use a pip command to install the requirements and run the app; below are the steps to take:
```
    $ cd myDiary-api
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
```

### Final result:
API is being hosted by heroku at:
https://douglas-mydiary.herokuapp.com/api/v1/diaries

### Built with and by:

[Flask](https://flask.pocoo.org/) - Python webframework
