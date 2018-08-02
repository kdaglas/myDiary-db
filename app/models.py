"""  Object class for the User """


class User(object):

    """ Constructor to initialise all parameters for the user object """

    def __init__(self, username, emailaddress, password):
        self.username = username
        self.emailaddress = emailaddress
        self.password = password


"""  Object class for the Entry """


class DiaryEntry():

    """ this one is to initialise all parameters for the entry class """

    def __init__(self, id, day, title, content):
        self.id = id
        self.day = day
        self.title = title
        self.content = content

        