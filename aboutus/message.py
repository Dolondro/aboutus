class Message:
    def __init__(self, datetime, user, message, image = None):
        self.datetime = datetime
        self.user = user
        self.message = message
        self.image = image