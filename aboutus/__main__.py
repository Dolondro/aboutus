import click
import os
from messenger.import_ import import_ as messenger_import

os.chdir(os.path.dirname(os.path.realpath(__file__ + "/..")))

# I think this is required here so we can successfully debug this
# Todo: Work out exactly what this is doing and whether it's needed.
# I think the reason that it's needed is because we're executing python on the directory (aboutus) and if we move to
# running the direct file it gets confused about what exactly it's meant to be executing
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
##cli.add_command(commands.parse.parse)


cli.add_command(messenger_import, "messenger:import")

if __name__ == '__main__':
    cli()