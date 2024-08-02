import re

# Input string
testString = """"""

packageNamePattern = r'\s*mConnectionEvents:'

regexes = {
    'SSID': r'\s*timeStamp=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
    'BSSID': r'\s*lastUpdateTime=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
}

names = {
    'SSID': 'Network Name',
    'BSSID': 'BSSID',
}

packages = []

with open('wifi.oxidize', 'r') as file:
    fileContent = file.readlines()
    package = {}
    for line in fileContent:
        match = re.match(packageNamePattern, line)
        if not match == None:
            if len(package) > 0: # current package has data, but we've ran into a new Package [...] line
                packages.append(package) # so add it to the list of packages
                package = {} # and clear the package, ready for next round

<<<<<<< Updated upstream
            package['packageName'] = match[1]
=======
            package['SSID'] = match[1]
            package['BSSID'] = match[2]
>>>>>>> Stashed changes
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
