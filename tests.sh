#!/usr/bin/env bash

source assert.sh

assert "./pb.py lookup Sarah hsphonebook.pb" "no such phonebook 'hsphonebook.pb'"

assert 'pb create hsphonebook.pb' 'created phonebook hsphonebook.pb in the current directory'

assert 'pb lookup Sarah hsphonebook.pb' '0 results found'

assert 'pb add "Sarah Ahmed" "432 123 4321"' 'added "Sarah Ahmed (432 123 4321)"'

assert 'pb add "Sarah Apple" "509 123 4567"' 'added "Sarah Apple (509 123 4567)"'

assert 'pb lookup Sarah hsphonebook.pb' 'Sarah Ahmed 432 123 4321\nSarah Orange 123 456 7890'

assert 'pb add "Sarah Ahmed" "123 456 7890" hsphonebook.pb' '"Sarah Ahmed" already in hsphonebook.pb'

assert 'pb change "Haras Ahmed" "123 432 1234" hsphonebook.pb' 'no such person "Haras Ahmed" in hsphonebook.pb'

assert 'pb remove "Haras Ahmed" "123 432 1234" hsphonebook.pb' 'no such person "Haras Ahmed" in hsphonebook.pb'

assert 'pb change "Sarah Ahmed" "123 432 1234" hsphonebook.pb' '"Sarah Ahmed" number changed to "123 432 1234"'

assert 'pb reverse-lookup "312 432 5432" hsphonebook.pb' 'no one found with number "312 432 5432"'

assert 'pb reverse-lookup "123 432 1234" hsphonebook.pb' 'Sarah Ahmed 123 432 1234'

assert_end
