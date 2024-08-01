# Oxidize 1.0 - August 2nd
A tool for analysing GrapheneOS ADB logs.

# Install
`git clone https://github.com/HappenedByProxy/graphene-analyser`

`python code/oxidize.py`

# Requirements
ADB must be on path.

## PREQUISITES
1. The phone must be unlocked. This is a standard for all forensic tools.
2. The owner profile must be the unlocked profile. It does not matter if you have no access to other profiles.
3. Developer options must be active, and USB debugging to be enabled.
4. The commands can be ran in any profile as long as the computer was authorized in the owner profile, and the cable does not get disconnected, but this will not change the outcome (I think).

## WHAT INFO CAN I GET?
1. List of all installed applications, even if they were uninstalled. We are unable to provide installation or uninstallation times, however.
2. Almost all accounts used on apps on the device, including connected Twitter accounts. 
3. Recent app usage history.
4. WiFi history.

## WHAT INFO CAN I NOT GET?
1. Media. We are analysing logfiles, we do not extract any media from the device.
2. Browser history.
3. SMS.
4. If the phone has rebooted, then information on deleted profiles will be incredibly limited, along with other data possibly.

## Using ADB on WSL1
* Windows: adb tcpip 5555
* WSL: adb connect <phone ip>:5555

## Other useful things
* I suggest piping "view <service>" into a pager. On Linux, this is done with `| less` or your preferred pager. On Windows, you can do `| more`.