#!/usr/bin/env python3

import sys
import click

def load(ctx, param, db):
    try:
        data = open(db)
    except FileNotFoundError:
        print("no such phonebook %r" % db)
        sys.exit(-1)
    return data

@click.group()
def cli():
    """pb: a phone book manager """
    pass

@cli.command()
@click.argument('name')
@click.argument('db', callback=load)
def lookup(name):
    """ lookup all phone numbers that match name """
    print(name)

if __name__ == '__main__':
    cli()
