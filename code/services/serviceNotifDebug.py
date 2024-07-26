import re

# Input string for testing
testString="""
      AppSettings: com.twitter.android (1110131) importance=DEFAULT userSet=true
        NotificationChannelGroup{mId='123456789', mName=@redacted, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
        NotificationChannelGroup{mId='987654321', mName=@R3dacted, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
        NotificationChannelGroup{mId='11223344556677', mName=@otherRedac, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
      AppSettings: app.grapheneos.camera (1110165) importance=DEFAULT userSet=false
"""

# packageList = list variable to fill with dicts. a list is just an array. which is [1, 2, 3]
# packageDict = dict is a set of keys and values. dicts are like json. {"age": 22}
# packageName = one of the keys in the dict
# a dict is a set of keys (values on the left) with values. You can reference a value by its key
#

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

with open('notification.txt.priv', 'r') as file:
    fileContent = file.readlines()
    packageDict = {}
    for line in fileContent:
        match = re.match(twitterNamePattern, line)
        if not match == None:
            print(f"Processing line: {line.strip()}")  # Debug print
            if len(packageDict) > 0:  # Current package has data, but we've run into a new Package [...] line
                print(f"Adding to dict...")
                packageList.append(packageDict)  # So add it to the list of packages
                #packageDict = {}  # And clear the package, ready for next round

            print("Regex match for twitterNamePattern found.")  # Debug print
            package['packageName'] = match[1]
            continue

    if len(packageDict) > 0:  # Are we filling in a package? (It's > 0 if packageName is set)
        for k, v in regexes.items():  # Keys and values from dict
            match = re.search(v, line)
            if match:
                print(f"Match found for {k} in line: {line.strip()}")  # Debug print
                print(f"Captured group: {match.group(1)}")  # Debug print
                packageDict[k] = match.group(1)  # Key has the same name as in package dictionary
                break

# After the last iteration, include the resulting package if it has data
if len(packageDict) > 0:
    packageList.append(packageDict)

# Output the packages
for packageDict in packageList:
    print(f"Package: {packageDict.get('packageName', 'Unknown')}")
    for k, v in names.items():
        if k in packageDict:
            print(f'{v}: {packageDict[k]}')
    print()
