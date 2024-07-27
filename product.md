### SO WHAT ARE WE EVEN MAKING?

We are making a tool to parse Android dumpsys logs into a readable format. This is specifically for use with GrapheneOS, but can also work with any Android phone.

### WHY?

Because all forensic tools we tested failed to extract much useful information from GrapheneOS, especialyl with the presence of profiles. However, we found that doing a dumpsys with ADB shows a lot of very useful information about the phone without needing the password for any other profiles, provided we have the primary profile unlocked.

### HOW?

We run the command, `adb shell dumpsys <service>`. We have determined the most valuable services to be account, wifi, storaged, usagestats, perhaps others.

Then, we parse the information through our software. 