import click
import os
#import commands

import commands.parse
import commands.sorter

os.chdir(os.path.dirname(os.path.realpath(__file__ + "/..")))

if __name__ == '__main__' and __package__ is None:
    import os, sys, importlib
    parent_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(parent_dir))
    __package__ = os.path.basename(parent_dir)
    importlib.import_module(__package__)

@click.group()
def cli():
    pass

# cli.add_command(commands.greet.greet)
cli.add_command(commands.parse.parse)
cli.add_command(commands.sorter.sorter, "messenger:sorter")

if __name__ == '__main__':
    cli()