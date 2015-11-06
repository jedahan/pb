#!/usr/bin/env bash

source assert.sh

rm hsphonebook.pb > /dev/null &2>1

assert "./pb.py lookup Sarah hsphonebook.pb" "no such phonebook 'hsphonebook.pb'"

assert './pb.py create hsphonebook.pb' "created phonebook 'hsphonebook.pb' in the current directory"

assert './pb.py create hsphonebook.pb' "phonebook 'hsphonebook.pb' already exists"

assert './pb.py lookup Sarah hsphonebook.pb' "0 results found"

assert './pb.py add "Sarah Ahmed" "432 123 4321" hsphonebook.pb' "added 'Sarah Ahmed (432 123 4321)' to 'hsphonebook.pb'"

assert './pb.py add "Sarah Apple" "509 123 4567" hsphonebook.pb' "added 'Sarah Apple (509 123 4567)' to 'hsphonebook.pb'"

assert './pb.py lookup Sarah hsphonebook.pb' "Sarah Ahmed (432 123 4321)
Sarah Apple (509 123 4567)"

assert './pb.py add "Sarah Ahmed" "123 456 7890" hsphonebook.pb' "'Sarah Ahmed' already in 'hsphonebook.pb'"

assert './pb.py change "Haras Ahmed" "123 432 1234" hsphonebook.pb' "no such person 'Haras Ahmed' in 'hsphonebook.pb'"

assert './pb.py remove "Haras Ahmed" "123 432 1234" hsphonebook.pb' "no such person 'Haras Ahmed' in 'hsphonebook.pb'"

assert './pb.py change "Sarah Ahmed" "123 432 1234" hsphonebook.pb' "Sarah Ahmed number changed to '123 432 1234'"

assert './pb.py reverse-lookup "312 432 5432" hsphonebook.pb' "no one found with number '312 432 5432'"

assert './pb.py reverse-lookup "123 432 1234" hsphonebook.pb' "Sarah Ahmed (123 432 1234)"

assert_end
