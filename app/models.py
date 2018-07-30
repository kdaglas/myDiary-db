"""  Object classes for the User """


class User(object):

    """ constructor to initialise all params """

    def __init__(self, id, username, emailaddress, password):
        self.id = id
        self.username = username
        self.emailaddress = emailaddress
        self.password = password


class DiaryEntry():

    """ constructor to initialise all params """

    def __init__(self, id, today, title, content):
        self.id = id
        self.today = today
        self.title = title
        self.content = content
        
