#!env python

import click

@click.group()
def cli():
    """pb: a phone book manager """
    pass

@cli.command()
@click.argument('name')
def lookup(name):
    """ lookup all phone numbers that match name """
    print(name)

if __name__ == '__main__':
    cli()
