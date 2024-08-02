import re

def main():
    # Patterns
    handlePattern = r'mName=@(\S{4,15}),'
    mIdPattern = r"\s*mId='(\d{3,24})'"

    groupList = []

    with open('notification.oxidize', 'r') as file:
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

if __name__ == "__main__":
    main()