# pb

**pb** is a command line tool that manages phone books, via the interface below.

## Installation

Recommended is to use virtualenv and setuptools:

    virtualenv venv
    . venv/bin/activate
    pip install .

Simplest way is:

    pip3 install click
    alias pb='python pb.py'

## Tests

    ./tests.sh

## Help

    $ pb --help
    Usage: pb.py [OPTIONS] COMMAND [ARGS]...

      pb: a phone book manager

    Options:
      --help  Show this message and exit.

    Commands:
      add             add a new person to the phonebook
      change          change a person in the phonebook
      create          lookup all phone numbers that match name
      lookup          lookup all phone numbers that match name
      remove          change a person in the phonebook
      reverse-lookup  lookup a name by phone number

## Sample session

    $ pb lookup Sarah hsphonebook.pb 
    no such phonebook

    $ pb create hsphonebook.pb
    created phonebook hsphonebook.pb in the current directory

    $ pb lookup Sarah hsphonebook.pb 
    0 results found

    $ pb add 'Sarah Ahmed' '432 123 4321'
    added 'Sarah Ahmed (432 123 4321)'

    $ pb add 'Sarah Apple' '509 123 4567'
    added 'Sarah Apple (509 123 4567)'

    $ pb lookup Sarah hsphonebook.pb
    Sarah Ahmed 432 123 4321
    Sarah Orange 123 456 7890

    $ pb add 'Sarah Ahmed' '123 456 7890' hsphonebook.pb
    'Sarah Ahmed' already in 'hsphonebook.pb'

    $ pb change 'Haras Ahmed' '123 432 1234' hsphonebook.pb
    no such person 'Haras Ahmed' in 'hsphonebook.pb'

    $ pb remove 'Haras Ahmed' '123 432 1234' hsphonebook.pb
    no such person 'Haras Ahmed' in 'hsphonebook.pb'

    $ pb change 'Sarah Ahmed' '123 432 1234' hsphonebook.pb
    'Sarah Ahmed' number changed to '123 432 1234'

    $ pb reverse-lookup '312 432 5432' hsphonebook.pb
    no one found with number '312 432 5432'

    $ pb reverse-lookup '123 432 1234' hsphonebook.pb
    Sarah Ahmed 123 432 1234

