import click
import os
import re
import datetime
import io
from shutil import copyfile
from bs4 import BeautifulSoup, NavigableString
from conversation import Conversation, message #participants
from messenger.Message import Message
# Freaking yuck, but BS4 parsing seems to be the slow thing in this affair, so start simple and build up to good code
cache = dict ()

# Set the EXIF data with https://github.com/hMatoba/Piexif

@click.command()
def import_():
    dir = "import/messenger/messages"
    conversations = os.listdir(dir)

    for file in conversations:
        if not file.endswith(".html"):
            continue

        filename = dir + "/" + file
        print("Dealing with "+filename)

        # Sometimes PHP got naming conventions right...
        contents = __get_file_contents(filename)
        parsed_page = BeautifulSoup(contents, "html.parser")

        participant_list = __get_participants(parsed_page)

        # The participant has deleted their account or similar
        if len(participant_list) == 0 or participant_list[0] == "Facebook User":
            continue



        folder = "data/"
        # There's a ternary operator in Python, but it may not be best practice, see the readme
        if (len(participant_list) > 1): # Then it's a group!
            folder = folder + "group/"
        else:
            folder = folder + "individual/"

        messages = __get_messages(parsed_page)
        for message in messages:
            #print(message.name + ": "+message.text)
            if message.image is not None:
                print("There was an image" + message.image)

        # Now, we


        exit(0)
        #print(messages)
        #exit(0)
        #participant_dict = dict()






        """
        print("Participants: ", participants)
        if len(participants) > 1:
            print("Copying to group folder")
            copyfile(filename, "data/group/" + file)
        elif len(participants) == 0 or participants[0] == "Facebook User":
            print("Skipping Facebook User")
        else:
            print("Copying to individual folder")

            name = participants[0].replace(" ", "")
            images = __get_images(filename)

            if len(images) > 0:
                    print(images)
                    exit(0)
                #exit(0)
                #os.mkdir("data/individual/" + name)

                #copyfile(filename, "data/individual/" + name + "/index.html")
                #return
        """
    #print(conversations)

def __get_participants(parsed_page: BeautifulSoup):
    content = parsed_page.find("div", class_='thread')
    for line in content:
        if isinstance(line, NavigableString):
            strip_prefix_re = re.compile(': ?(.*)')
            participant_string = strip_prefix_re.search(line).group(1)
            participants = participant_string.split(",")
            return list(map(lambda participant: participant.strip(), participants))

    return list()


def __get_messages(parsed_page: BeautifulSoup):
    messages = list()
    matches = parsed_page.find_all(class_='message')
    for match in matches:
        user = match.find(class_='user').contents[0]
        date_text = match.find(class_='meta').contents[0]

        """
        I really want to just use something like this, but I'm not sure that strptime is powerful enough
        This is pretty gross, but we can get data in one of two formats:
        Monday, 14 May 2012 at 19:28 UTC OR
        Monday, 14 May 2012 at 19:28 UTC+01
        There's an external dateparser class that can be used, but it's slow as anything and this gets run a *lot*
        As Python doesn't acknowledge any other +format other than +0100, we manually add the 00 to the end. Sick right?
        """
        try:
            date = datetime.datetime.strptime(date_text, '%A, %d %B %Y at %H:%M %Z')
        except ValueError:
            date = datetime.datetime.strptime(date_text + "00", '%A, %d %B %Y at %H:%M %Z%z')

        sibling = match.find_next_sibling("p")

        # If there was no contents... then I'm not sure what happened but we don't particularly care about the line
        if len(sibling.contents) == 0:
            continue

        # Todo: Messages will need an idea of where they were attached to.
        img = sibling.find("img")
        if img is not None and img.has_attr("src"):
            messages.append(Message(date, user, "", img.attrs["src"]))
        else:
            messages.append(Message(date, user, sibling.contents[0]))

    # We reverse it, as Facebook brings it back to us in inverted order atm
    messages.reverse()
    return messages


def __get_images(parsed_page: BeautifulSoup):
    images = parsed_page.find_all("img")
    image_filenames = list(map(lambda image: image.get("src"), images))
    return list(filter(lambda image_filename: "/stickers/" not in image_filename, image_filenames))


def __get_file_contents(filename):
    with open(filename, encoding="utf8") as f:
        return f.read()