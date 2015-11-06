#!/usr/bin/env python3

import sys
import click
import pickle
from os.path import exists

def load(db):
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
@click.argument('db')
def lookup(name, db):
    """ lookup all phone numbers that match name """
    database = load(db)
    matches = [ key for key in database if name in key ]
    if len(matches):
        for name in matches:
            print("%s (%s)" % (name, database[name]))
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

@cli.command()
@click.argument('name')
@click.argument('phone')
@click.argument('db')
def add(name, phone, db):
    """ add a new person to the phonebook """
    database = load(db)
    if name in database:
        print("%r already in %r" % (name, db))
        sys.exit(-1)
    else:
        database[name] = phone
        pickle.dump(database, open(db, 'wb'))
        print("added '%s (%s)' to %r" % (name, phone, db))

if __name__ == '__main__':
    cli()
