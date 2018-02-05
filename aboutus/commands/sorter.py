# The role of organise is going to be to grok the directory, work out if it's a group chat or a non-group chat then move the raw data appropriately
# This is more of a group initial

import click
import os
import re
import io
from shutil import copyfile
from bs4 import BeautifulSoup, NavigableString

cache = dict()

# Set the EXIF data with https://github.com/hMatoba/Piexif

@click.command()
def sorter():
    dir = "import/messenger/messages"
    conversations = os.listdir(dir)

    for file in conversations:
        filename = dir + "/" + file
        if filename.endswith(".html"):
            print("Dealing with "+filename)
            participants = __get_participants(filename)
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

    #print(conversations)

def __get_soup(filename):
    if not cache.get(filename):
        contents = __get_file_contents(filename)
        cache[filename] = BeautifulSoup(contents, "html.parser")

    return cache[filename]


def __get_participants(filename):
    content = __get_soup(filename).find("div", class_='thread')
    for line in content:
        if isinstance(line, NavigableString):
            strip_prefix_re = re.compile(': ?(.*)')
            participant_string = strip_prefix_re.search(line).group(1)
            participants = participant_string.split(",")
            return list(map(lambda participant: participant.strip(), participants))

    return list()

def __get_images(filename: str):
    images = __get_soup(filename).find_all("img")
    image_filenames = list(map(lambda image: image.get("src"), images))
    return list(filter(lambda image_filename: "/stickers/" not in image_filename, image_filenames))

def __get_file_contents(filename):
    with open(filename, encoding="utf8") as f:
        return f.read()