import re

# Patterns
userInfoPattern = r'User UserInfo\{(\d+):([^:]+):([^}]+)\}:'
accountPattern = r'\s*Account \{name=([^,]+), type=([^\}]+)\}'

profileList = []

with open('account.oxidize.priv', 'r') as file:
    fileContent = file.readlines()
    profileDict = {}
    for line in fileContent:
        user_match = re.match(userInfoPattern, line)
        if user_match:
            if profileDict:  # If there is already a profileDict, save it before starting a new one
                profileList.append(profileDict)
            profileDict = {
                'userId': user_match[1],
                'userName': user_match[2],
                'userNumber': user_match[3],
                'accounts': []
            }
        else:
            account_match = re.match(accountPattern, line)
            if account_match and profileDict:
                accountDict = {
                    'name': account_match[1],
                    'type': account_match[2]
                }
                profileDict['accounts'].append(accountDict)
    
    if profileDict:
        profileList.append(profileDict)

# Print results
for profileDict in profileList:
    print(f"ID: {profileDict['userId']}")
    print(f"Profile: {profileDict['userName']}")
    print(f"UID: {profileDict['userNumber']}")
    for account in profileDict['accounts']:
        print(f"  - Name: {account['name']}, App: {account['type']}")
    print()
