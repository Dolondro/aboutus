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

    print(messages)

def __get_file_contents(filename):
    with open(filename, encoding="utf8") as f:
        return f.read()