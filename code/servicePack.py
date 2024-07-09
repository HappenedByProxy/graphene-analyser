import re

# Patterns
installTime = r'\s*timeStamp=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
lastUpdated = r'\s*lastUpdateTime=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
installerOrigin = r'\s*originatingPackageName=([^\n]+)'
installerOriginOther = r'\s*installerPackageName=([^\n]+)'

groupList = []

with open('packages.txt.priv', 'r') as file:
    fileContent = file.readlines()
    for line in fileContent:
        id_match = re.search(mIdPattern, line)
        name_match = re.search(handlePattern, line)
        if id_match and name_match:
            groupDict = {
                'mId': id_match[1],
                'mName': name_match[1]
            }
            groupList.append(groupDict)

# Print results
for groupDict in groupList:
    print(f"Twitter ID: {groupDict['mId']}")
    print(f"Twitter Handle: {groupDict['mName']}")
    print()
