#!/usr/bin/env bash
#
# Run the project tests

# Change to directory of this script
cd "$( dirname "${BASH_SOURCE[0]}" )"

python manage.py test --settings=conf.settings_test --noinput $@

# Print out a nice colored message
if [ $? -eq 0 ]; then
    echo -e "\033[42;37mTests passed!\033[0m"
else
    echo -e "\033[41;37mTests failed!\033[0m"
fi
