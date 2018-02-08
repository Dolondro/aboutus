
class Conversation:
    ## def __init__(self):

    def __init__(self, folder, filename):
        print("Hello")


    #def create(self, folder):

    #def __init__(self, participants):
    #    self.participants = participants

def factory(type_, participants: list):
    folder = "data/"
    # There's a ternary operator in Python, but it may not be best practice, see the readme
    if len(participants) > 1:  # Then it's a group!
        folder = folder + "group/"
    else:
        folder = folder + "individual/"

    folder = folder + "-".join(participants[0:3]).replace(" ", "") + "/"
    return Conversation(folder, type_ + ".json")


def load(self, folder):
    print("Loading")


class Message:
    def __init__(self, date, name, text, image=None):
        self.name = name
        self.date = date
        self.text = text
        self.image = image
