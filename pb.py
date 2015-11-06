#!/usr/bin/env python3

import sys
import click
import pickle
from os.path import exists

def load(ctx, param, db):
    if exists(db):
        return pickle.load(open(db, 'rb'))
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
def lookup(name, db):
    """ lookup all phone numbers that match name """
    if len(db):
        print(db)
    else:
        print("0 results found")

@cli.command()
@click.argument('db')
def create(db):
    """ lookup all phone numbers that match name """
    if exists(db):
        print("phonebook %r already exists" % db)
        sys.exit(-1)
    else:
        database = {}
        pickle.dump(database, open(db, 'wb'))
        print("created phonebook %r in the current directory" % db)

if __name__ == '__main__':
    cli()
