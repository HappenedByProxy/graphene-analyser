import re

def main():
  packageNamePattern = r'\s*Package \[([^\]]+)\] \(\w+\):'

  regexes = {
      'installTime': r'\s*timeStamp=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
      'lastUpdated': r'\s*lastUpdateTime=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
      'installerOrigin': r'\s*originatingPackageName=([^\n]+)',
      'installerOriginOther': r'\s*installerPackageName=([^\n]+)'
  }

  names = {
      'installTime': '- Install time',
      'lastUpdated': '- Last updated',
      'installerOrigin': '- Installer origin',
      'installerOriginOther': '- Installer origin (other)'
  }

  packageList = []

  with open('package.oxidize', 'r') as file:
      fileContent = file.readlines()
      packageDict = {}
      for line in fileContent:
          match = re.match(packageNamePattern, line)
          if not match == None:
              if len(packageDict) > 0: # current package has data, but we've ran into a new Package [...] line
                  packageList.append(packageDict) # so add it to the list of packages
                  packageDict = {} # and clear the package, ready for next round

              packageDict['packageName'] = match[1]
              continue

          if len(packageDict) > 0: # are we filling in a package? (it's > 0 if packageName is set)
              for k, v in regexes.items(): # keys and values from dict
                  match = re.match(v, line)
                  if match:
                      packageDict[k] = match[1] # key has the same name as in package dictionary
                      break

      # after the last iteration, include the resulting package if it has data
      if len(packageDict) > 0:
          packageList.append(packageDict)


  for packageDict in packageList:
      print(f"{packageDict['packageName']}")
      for k, v in names.items():
         if k in packageDict:
            print(f'{v}: {packageDict[k]}')
      print()
    
if __name__ == "__main__":
    main()
