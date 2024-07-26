import re

testString = "Last logged in: +17d2h32m27s216ms ago"

# Split this string down.
# The + is our "meeting point".
indexPlus = testString.index('+')
# Store everything before the : as the "prefix" var.
prefix = testString[:indexPlus]
# Store everything after the + as our strippedString.
strippedString = testString[indexPlus:].split('+', 1)[-1]
# Remove the "ago"
strippedString = strippedString.split(' ago', 1)[0]
# Now we need to split this into an array. Easy enough thanks to the markers.
days = hours = minutes = seconds = milliseconds = 0
# Use regex (my beloved) to find the markers.
matches = re.findall(r'(\d+)([dhms]*)', strippedString)
# Here comes the yandere dev moment
for num, unit in matches:
    if unit == 'd':
        days = int(num)
    elif unit == 'h':
        hours = int(num)
    elif unit == 'm':
        minutes = int(num)
    elif unit == 's':
        seconds = int(num)
    elif unit == 'ms':
        milliseconds = int(num)

print(f"{prefix}")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
print(f"Milliseconds: {milliseconds}")

# 17d2h32m27s216ms
print(strippedString)
