### SO WHAT ARE WE EVEN MAKING?

We are making a tool to parse Android dumpsys logs into a readable format. This is specifically for use with GrapheneOS, but can also work with any Android phone.

### WHY?

Because all forensic tools we tested failed to extract much useful information from GrapheneOS, especialyl with the presence of profiles. However, we found that doing a dumpsys with ADB shows a lot of very useful information about the phone without needing the password for any other profiles, provided we have the primary profile unlocked.

### HOW?

We run the command, `adb shell dumpsys <service>`. We have determined the most valuable services to be account, wifi, storaged, usagestats, perhaps others.

Then, we parse the information through our software. 


### PREQUISITES
1. The phone must be unlocked. This is a standard for all forensic tools.
2. The primary profile must be the unlocked profile. It does not matter if you have no access to other profiles.
3. Developer options must be active, and USB debugging to be enabled.
4. The commands can be ran in any profile as long as the computer was authorized and the cable does not get disconnected, but this will not change the outcome (I think).

### WHAT INFO CAN I GET?

1. List of all installed applications, even if they were uninstalled. We are unable to provide installation or uninstallation times, however.
2. Almost all accounts used on apps on the device, including connected Twitter accounts. 
3. Recent app usage history.
4. WiFi history.

### WHAT INFO CAN I NOT GET?

1. Media. We are analysing logfiles, we do not extract any media from the device.
2. Browser history.
3. SMS.
4. If the phone has rebooted, then information on deleted profiles will be incredibly limited, along with other data possibly.

### HOW DO I IDENTIFY A GRAPHENEOS DEVICE?
1. Go into the guest profile if it's enabled.