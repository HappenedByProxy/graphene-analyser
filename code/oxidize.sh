#!/bin/sh
# Finally, my native language.
# A demo of what oxidize.py would look like.
# Files made with this script are called .oxidize to remind me where they came from.

if [ -z "$1" ]
then
	printf "OXIDIZE - TESTING\n"
	printf "list - List possible services.\n"
	printf "get <service> - Get service files.\n"
	printf "run <service> - Run that service parser.\n"
	printf "view <service> - Fetch & view the service file without parsing it, and also without saving it.\n" 
fi

# List running services we can dump.
if [ "$1" = "list" ]
then
	adb shell dumpsys -l | less
fi

# If gather is ran but a second argument isn't, exit.
if [ "$1" = "get" ] && [ -z "$2" ]
then
	printf "You gotta pick a service first!\n"
	exit
fi

# If gather is set, and somehow the last check wasn't bypassed, then do the thingy.
if [ "$1" = "get" ]
then
	adb shell dumpsys "$2" > "$2".oxidize.priv
	printf "Saved as $2.oxidize.priv\n"
fi

if [ "$1" = "run" ] && [ -z "$2" ]
then
	printf "You gotta pick a service first!\n"
	exit
fi

# Because of camelCase, capitalise the start of the given service.
if [ "$1" = "run" ]
then
	prep=$(echo "$2" | sed 's/./\U&/; s/\(.\)\(.*\)/\1\L\2/')
	python3 service$prep.py
fi

# If gather is set, and somehow the last check wasn't bypassed, then do the thingy.
if [ "$1" = "view" ]
then
	adb shell dumpsys "$2" | less
fi
