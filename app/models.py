"""  Object class for the User """
class User(object):

    """ this constructor is to initialise all parameters for the user object """

    def __init__(self, id, username, emailaddress, password):
        self.id = id
        self.username = username
        self.emailaddress = emailaddress
        self.password = password

"""  Object class for the Entry """
class DiaryEntry():

    """ this one is to initialise all parameters for the entry class """

    def __init__(self, id, date, title, content):
        self.id = id
        self.date = date
        self.title = title
        self.content = content
        
