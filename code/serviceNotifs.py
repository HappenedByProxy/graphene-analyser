import re

# Input string
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

# NotificationChannelGroup{
# \s*mId='
twitterNamePattern = r'\s*AppSettings: ([^\]]+)'

regexes = {
    'twitterID': r'\s*mId=(\d{3,24})',
    # https://help.x.com/en/managing-your-account/x-username-rules
    'twitterHandle': r'(?<=mName=@)\S{4,15}(?=,)',
}

names = {
    'twitterID': 'Install time',
    'twitterHandle': 'Last updated',
}

packages = []

with open('notification.txt.priv', 'r') as file:
    fileContent = file.readlines()
    package = {}
    for line in fileContent:
        match = re.match(twitterNamePattern, line)
        if not match == None:
            print(f"Processing line: {line}")  # Debug print
            if len(package) > 0: # current package has data, but we've ran into a new Package [...] line
                packages.append(package) # so add it to the list of packages
                package = {} # and clear the package, ready for next round

            package['packageName'] = match[1]
            continue

        if len(package) > 0: # are we filling in a package? (it's > 0 if packageName is set)
            for k, v in regexes.items(): # keys and values from dict
                match = re.match(v, line)
                if match:
                    package[k] = match[1] # key has the same name as in package dictionary
                    break

    # after the last iteration, include the resulting package if it has data
    if len(package) > 0:
        packages.append(package)


for package in packages:
    print(f"Package: {package['packageName']}")
    for k, v in names.items():
       if k in package:
          print(f'{v}: {package[k]}')
    print()
