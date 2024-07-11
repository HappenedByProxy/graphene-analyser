import re

# Patterns
userInfoPattern = r'User UserInfo\{(\d+):([^:]+):(\d+)\}:'
accountPattern = r'\s*Account \{name=([^,]+), type=([^\}]+)\}'

groupList = []

with open('account.oxidize', 'r') as file:
    fileContent = file.readlines()
    for line in fileContent:
        id_match = re.search(userInfoPattern, line)
        name_match = re.search(accountPattern, line)
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
