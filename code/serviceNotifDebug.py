import re

# Input string for testing
#testString = "  Package [com.android.adservices.api] (a37eabe)"
# vim: set fdm=marker fmr={{{,}}} fdl=0 :
# {{{ dummy data
testString="""
        NotificationChannel{mId='1468991407889256453-dms', mName=Dir..., mDescription=, mImportance=4, mBypassDnd=false, mLockscreenVisibility=-1000, mSound=content://settings/sys>
        NotificationChannel{mId='1370568081811079169-live_spaces', mName=Liv..., mDescription=, mImportance=4, mBypassDnd=false, mLockscreenVisibility=-1000, mSound=null, mLights=>
        NotificationChannelGroup{mId='123456789', mName=@redacted, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
        NotificationChannelGroup{mId='987654321', mName=@R3dacted, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
        NotificationChannelGroup{mId='11223344556677', mName=@otherRedac, mDescription=, mBlocked=false, mChannels=[], mUserLockedFields=0}
      AppSettings: app.grapheneos.camera (1110165) importance=DEFAULT userSet=false
"""

# Regex patterns
twitterNamePattern = r'\s*AppSettings: ([^\]]+)'

regexes = {
    'twitterID': r"\s*mId='(\d{3,24})'",
    # https://help.x.com/en/managing-your-account/x-username-rules
    'twitterHandle': r'(?<=mName=@)\S{4,15}(?=,)',
}
names = {
    'twitterID': 'Install time',
    'twitterHandle': 'Last updated',
}

# Process the file
packageDict = []

# Simulating file read with testString split into lines
fileTest = testString.strip().split('\n')

packageList = {}
for line in fileTest:
    match = re.match(twitterNamePattern, line)
    if match:
        print(f"Processing line: {line.strip()}")  # Debug print
        if len(packageList) > 0:  # Current package has data, but we've run into a new Package [...] line
            packageDict.append(packageList)  # So add it to the list of packages
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
if len(packageList) > 0:
    packageDict.append(packageList)

# Output the packages
for packageList in packageDict:
    print(f"Package: {packageList.get('packageName', 'Unknown')}")
    for k, v in names.items():
        if k in packageList:
            print(f'{v}: {packageList[k]}')
    print()
