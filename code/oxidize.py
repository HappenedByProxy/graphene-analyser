import sys
import subprocess
import serviceAccount
import importlib
import shutil

try:
    import pypager
    pagerAvailable = True
except ImportError:
    pagerAvailable = False

# Three ways to use this program.
# One is automatic ADB collection, more guided.
# Second is you insert a service file yourself.
# Third is you throw a whole bugreport in there.

def main():
    
    if len(sys.argv) < 2:
        print("""OXIDIZE V1.0
list - List possible services.
get <service>  - Write service file to disk.
run <service>  - Run a service parser.
view <service>  - Fetch & view the service log without parsing or saving. 
setup - Set up OXIDIZE.
opt - Optional Python modules that you could use.""")
        sys.exit(1)

    # $1
    arg1 = sys.argv[1]

    # $2
    arg2 = sys.argv[2] if len(sys.argv) > 2 else None
    # We use camelCase. Capitalise the start of whatever arg2 is given.
    arg2 = arg2.capitalize() if len(sys.argv) > 2 else None



    # Gets the service file.
    if arg1 == "get":

        # To prevent YandereDev-type code, lets dynamically change the name of the module we use.
        #module_name = f"service{arg2}"
        #module = importlib.import_module(module_name)
        # It's really dumb, but we need to actually lowercase this or it won't work.
        arg2 = arg2.lower()

        # Get the diagnostic log for the service specified. Techncially, yes, if you mispell a service, you get nothing
        # There is probably a way to prevent this.
        result = subprocess.run(["adb", "shell", "dumpsys", arg2], capture_output=True)
        output = result.stdout
        
        output_file = f"{arg2}.oxidize"
        with open(output_file, "wb") as f:
            f.write(output)
        print("Written to",output_file)

    elif arg1 == "list":
        # Run dumpsys -l, aka "show us packages".
        result = subprocess.run(["adb", "shell", "dumpsys", "-l"], capture_output=True)
        output = result.stdout.decode('utf-8')  # Decode the byte output to a string. This makes newliens (\n) actually work as intended.
        print(output)

    elif arg1 == "run":
        # Run the right script.
        module_name = f"service{arg2}"
        module = importlib.import_module(module_name)
        module.main()

    elif arg1 == "view":
        arg2 = arg2.lower()
        result = subprocess.run(["adb", "shell", "dumpsys", arg2], capture_output=True)
        output = result.stdout.decode('utf-8')
        # for later
        if pagerAvailable == True:
            #pager.add_source(output)
            #p.run()
            print(output)
        else:
            print(output)
    elif arg1 == "opt":
        print(f"pypager:",pagerAvailable)

    # Time for if statement hell.
    elif arg1 == "setup":
        print("Checking if ADB is installed...")
        # Run "adb" as a command. If its present? Carry on.
        checkADB = shutil.which("adb")
        if checkADB:
            print(f"ADB in path.")
        # adb isn't in path? Exit, no point in continuing.
        else:
            print("ADB is not in the path. ADB is a requirement for this script to work.")
            print("Not written by me, but will help you on Windows:")
            print("https://medium.com/@yadav-ajay/a-step-by-step-guide-to-setting-up-adb-path-on-windows-0b833faebf18")
            sys.exit()
        
        # ADB in path? Let's make sure we are authorized.
        print("Connect the device to the computer with a USB cable.")
        input("When connected, press any key to continue.")

# Suddenly, ADB is like "well I don't wanna be authorised anymore!!"
# So instead of saying its authorised when it is authorised, it instead says:
# List of devices attached
# 09091JECB09613         device product:bramble model:Pixel_4a__5G_ device:bramble transport_id:1
# WHY???
        while True:
            result = subprocess.run(['adb', 'devices', '-l'], capture_output=True, text=True)
            output = result.stdout
    
            # Not authorized? Look at the phone.
            if 'unauthorized' in output:
                print("Allow USB debugging on the phone.")
                input("Press Enter to try again.")
                continue  # Retry the loop to check authorization again
    
            # Not authorized OR unauthorized? Device probably isn't plugged in.
            if "authorized" not in output and "unauthorized" not in output:
                if "model" not in output:
                    print("No devices found.")
                    input("Ensure the device is plugged in and press Enter to try again.")
    
            # Authorized? Let them know they can use the rest of the script now.
            elif 'authorized' or 'device' in output:
                print("Device authorized.")
                break  # Exit the loop since the device is authorized


    
if __name__ == "__main__":
    main()