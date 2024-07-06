import re

# Sample string
text = "User UserInfo{11:Aurora:410}:"

# Define the regex pattern
accountNamePattern = r'UserInfo\{[^}]+\}'

# Search for the pattern in the text
if re.search(accountNamePattern, text):
    print("found you!")
else:
    print("not found")
