import click
from .image import resize, tspncy

@click.group()
def cli():
    """Main CLI entrypoint"""
    pass

""" config command """
cli.add_command(resize)
cli.add_command(tspncy)
