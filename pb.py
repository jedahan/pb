#!/usr/bin/env python3

import sys
import click
from os.path import exists

def load(ctx, param, db):
    if exists(db):
        return open(db)
    else:
        print("no such phonebook %r" % db)
        sys.exit(-1)

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


@cli.command()
@click.argument('db')
def create(db):
    """ lookup all phone numbers that match name """
    if exists(db):
        print("phonebook %r already exists" % db)
        sys.exit(-1)
    else:
        open(db, 'w')
        print("created phonebook %r in the current directory" % db)

if __name__ == '__main__':
    cli()
