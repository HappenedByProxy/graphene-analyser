import re
import cProfile
from cProfile import run


# Compile the regex patterns. Why? Because.
# ChatGPT 3.5 has refactored the code with optimizations.
# We noticed from this stackoverflow comment by ShreevatsaR, claiming that re.compile improves speed by 10-50x. https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile/#comment31259630_452104
# I provided my code to ChatGPT 3.5, and told it to compile my regex patterns. Due to compiling them, it changed the rest of the code too to fit the changes.
testString = """
 Package [com.android.documentsui] (b501922):
    userId=10030
    pkg=Package{b0f3fb3 com.android.documentsui}
    codePath=/system/priv-app/DocumentsUI
    resourcePath=/system/priv-app/DocumentsUI
    legacyNativeLibraryDir=/system/priv-app/DocumentsUI/lib
    extractNativeLibs=true
    primaryCpuAbi=null
    secondaryCpuAbi=null
    cpuAbiOverride=null
    versionCode=33 minSdk=30 targetSdk=30
    minExtensionVersions=[]
    versionName=13
    usesNonSdkApi=false
    splits=[base]
    apkSigningVersion=3
    flags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP KILL_AFTER_RESTORE ]
    privateFlags=[ PRIVATE_FLAG_ACTIVITIES_RESIZE_MODE_RESIZEABLE_VIA_SDK_VERSION ALLOW_AUDIO_PLAYBACK_CAPTURE PRIVILEGED PRIVATE_FLAG_ALLOW_NATIVE_HEAP_POINTER_TAGGING ]
    forceQueryable=false
    dataDir=/data/user/0/com.android.documentsui
    supportsScreens=[small, medium, large, xlarge, resizeable, anyDensity]
    timeStamp=2009-01-01 00:00:00
    lastUpdateTime=2009-01-01 00:00:00
    packageSource=0
    signatures=PackageSignatures{258d970 version:3, signatures:[87e68668], past signatures:[]}
    installPermissionsFixed=true
    pkgFlags=[ SYSTEM HAS_CODE ALLOW_CLEAR_USER_DATA ALLOW_BACKUP KILL_AFTER_RESTORE ]
    declared permissions:
      com.android.documentsui.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: prot=signature, INSTALLED
    install permissions:
      android.permission.CHANGE_OVERLAY_PACKAGES: granted=true
      android.permission.FOREGROUND_SERVICE: granted=true
      android.permission.RECEIVE_BOOT_COMPLETED: granted=true
      android.permission.REMOVE_TASKS: granted=true
      android.permission.LOG_COMPAT_CHANGE: granted=true
      android.permission.INTERACT_ACROSS_USERS: granted=true
      android.permission.CACHE_CONTENT: granted=true
      com.android.documentsui.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION: granted=true
      android.permission.MODIFY_QUIET_MODE: granted=true
      android.permission.MANAGE_DOCUMENTS: granted=true
      android.permission.READ_COMPAT_CHANGE_CONFIG: granted=true
      android.permission.START_FOREGROUND_SERVICES_FROM_BACKGROUND: granted=true
      android.permission.QUERY_ALL_PACKAGES: granted=true
      android.permission.WAKE_LOCK: granted=true
    User 0: ceDataInode=1580 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=2009-01-01 00:00:00
      uninstallReason=0
      overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
        /data/resource-cache/com.android.systemui-neutral-LxaV.frro
        /data/resource-cache/com.android.systemui-accent-RVjK.frro
      legacy overlay paths:
        /product/overlay/NavigationBarMode3Button/NavigationBarMode3ButtonOverlay.apk
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
    User 10: ceDataInode=3262 installed=true hidden=false suspended=false distractionFlags=0 stopped=false notLaunched=false enabled=0 instant=false virtual=false
      installReason=0
      firstInstallTime=1970-01-01 01:00:00
      uninstallReason=0
      runtime permissions:
        android.permission.POST_NOTIFICATIONS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
        android.permission.OTHER_SENSORS: granted=true, flags=[ USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED]
 
"""

def main():

    # Read the input string from file
 #   packageFile = "packages.txt"
 #   with open(packageFile, 'r') as file:
 #       testString = file.read()


    packageNamePattern = re.compile(r'Package \[([^\]]+)\] \(\w+\):')
    installTimePattern = re.compile(r'timeStamp=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    lastUpdatedPattern = re.compile(r'lastUpdateTime=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    installerOriginPattern = re.compile(r'originatingPackageName=([^\n]+)')
    installerOriginOtherPattern = re.compile(r'installerPackageName=([^\n]+)')


    #
    # First, we get the package name.
    # Using regex (my sworn enemy) to find and store everything between square brackets as a package. Then, get the other stuff like install date and where the package was installed from. With regex. Why?
    # ChatGPT 3.5 assisted in modifying the regex to let it re-iterate through several blocks of text.
    # https://chatgpt.com/share/71617b5d-d4ec-4688-a2c7-12117cb2ad3a
    matches = []
    for match in re.findall(packageNamePattern.pattern + r'[\s\S]*?' +
                            installTimePattern.pattern + r'[\s\S]*?' +
                            lastUpdatedPattern.pattern + r'[\s\S]*?' +
                            installerOriginPattern.pattern + r'[\s\S]*?' +
                            installerOriginOtherPattern.pattern, testString):
        # Extract specific groups from the match
        packageName = match[0]
        installTime = match[1]
        lastUpdated = match[2]
        installerOrigin = match[3]
        installerOriginOther = match[4]

        # Append to matches as a tuple
        matches.append((packageName, installTime, lastUpdated, installerOrigin, installerOriginOther))

    # Process matches into a list of dictionaries
    packages = []
    for match in matches:
        package_info = {
            'packageName': match[0],
            'installTime': match[1],
            'lastUpdated': match[2],
            'installerOrigin': match[3],
            'installerOriginOther': match[4]
        }
        packages.append(package_info)

    # Output the packages
    for package in packages:
        print(f"Package Name: {package['packageName']}")
        print(f"Install Time: {package['installTime']}")
        print(f"Last Updated Time: {package['lastUpdated']}")
        print(f"Installer Origin: {package['installerOrigin']}")
        print(f"Installer Origin Other: {package['installerOriginOther']}")
        print()

if __name__ == '__main__':
    main()