import re

# Input string for testing
testString="""
      AppSettings: com.twitter.android (1110131) importance=DEFAULT userSet=true
        NotificationChannelGroup{mId='123456789', mName=@redacted, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
        NotificationChannelGroup{mId='987654321', mName=@R3dacted, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
        NotificationChannelGroup{mId='11223344556677', mName=@otherRedac, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
      AppSettings: app.grapheneos.camera (1110165) importance=DEFAULT userSet=false
"""

# packageList = list variable to fill with dicts
# packageDict = dict is a set of keys and values
# packageName = one of the keys in the dict
# a dict is a set of keys (values on the left) with values. You can reference a value by its key

# Regex patterns
twitterNamePattern = r'\s*AppSettings:\s'

regexes = {
    'twitterID': r"\s*mId='(\d{3,24})'",
    # Usernames are 4-15 characters.
    # https://help.x.com/en/managing-your-account/x-username-rules
    'twitterHandle': r'mName=@\S{4,15}',
}
names = {
    'twitterID': 'Install time',
    'twitterHandle': 'Last updated',
}

# Process the file
packageList = []

# Simulating file read with testString split into lines
fileTest = testString.strip().split('\n')

packageDict = {}
for line in fileTest:
    match = re.match(twitterNamePattern, line)
    if match:
        print(f"Processing line: {line.strip()}")  # Debug print
        if len(packageList) > 0:  # Current package has data, but we've run into a new Package [...] line
            print(f"Adding to dict...")
            packageList.append(packageDict)  # So add it to the list of packages
            packageList = {}  # And clear the package, ready for next round

        print("Regex match for twitterNamePattern found.")  # Debug print
        # No capturing group here, so just indicating a match is found
        continue

    if len(packageList) > 0:  # Are we filling in a package? (It's > 0 if packageName is set)
        for k, v in regexes.items():  # Keys and values from dict
            match = re.search(v, line)
            if match:
                print(f"Match found for {k} in line: {line.strip()}")  # Debug print
                print(f"Captured group: {match.group(1)}")  # Debug print
                packageList[k] = match.group(1)  # Key has the same name as in package dictionary
                break

# After the last iteration, include the resulting package if it has data
if len(PackageDict) > 0:
    packageList.append(PackageDict)

# Output the packages
for packageList in packageDict:
    print(f"Package: {packageList.get('packageName', 'Unknown')}")
    for k, v in names.items():
        if k in packageList:
            print(f'{v}: {packageList[k]}')
    print()
