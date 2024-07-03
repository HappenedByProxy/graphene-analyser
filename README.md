WIP.

# DEVELOPMENT NOTES
Confidential data gathered from my personal phone is to never be committed to the repo. When it is being used to test scripts, it ends with the `.priv` extension, which is `.gitignore`d.

# HOW 2 ADB ON WSL1
* Windows: adb tcpip 5555
* WSL: adb connect <phone ip>:5555

# HOW DO I GET DATA
* adb devices
* adb bugreport

or

* adb shell dumpsys `<service>`