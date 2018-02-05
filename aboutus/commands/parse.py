import click
import re
from bs4 import BeautifulSoup, NavigableString
from message import Message

@click.command()

#def parse(filename="/develop/aboutus/data/facebook-lolkek/messages/255.html"):
def parse(filename="/develop/aboutus/data/facebook-lolkek/messages/310.html"):
#def parse(filename="/develop/aboutus/data/facebook-lolkek/messages/67.html"):
#def parse(filename="data/facebook-lolkek/messages/338.html"):

    contents = __get_file_contents(filename)
    soup = BeautifulSoup(contents, "html.parser")

    messages = list()
    content = soup.find("div", class_='thread')
    for line in content:
        if isinstance(line, NavigableString):
            strip_prefix_re = re.compile(': ?(.*)')
            participant_string = strip_prefix_re.search(line).group(1)
            participants = participant_string.split(",")
            break

    matches = soup.find_all(class_='message')
    for match in matches:
        user = match.find(class_='user').contents[0]
        date = match.find(class_='meta').contents[0]
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

    print(messages)

def __get_file_contents(filename):
    with open(filename, encoding="utf8") as f:
        return f.read()