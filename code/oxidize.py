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
    
    # There's a few ways users may try to get the help menu to appear. 
    if len(sys.argv) < 2 or sys.argv[1] == "-h" or sys.argv[1] == "help" or sys.argv[1] == "--help":
        print("""OXIDIZE V1.0
list - List possible services.
get <service>  - Write service file to disk.
run <service>  - Run a service parser.
view <service>  - Fetch & view the service log without parsing or saving.
opt - Optional Python modules that you could use.""")
        sys.exit(1)

    # $1
    arg1 = sys.argv[1]

    # $2
    arg2 = sys.argv[2] if len(sys.argv) > 2 else None
    # We use camelCase. Capitalise the start of whatever arg2 is given.
    arg2 = arg2.capitalize() if len(sys.argv) > 2 else None

    # $3
    arg3 = sys.argv[3] if len(sys.argv) > 3 else None

    # Run "adb" as a command. If its present? Carry on.
    checkADB = shutil.which("adb")
    if checkADB:
        adbStatus = True
    else:
     # adb isn't in path? Exit, no point in continuing.
        print("ADB is not in the path. ADB is a requirement for this script to work.")
        print("Not written by me, but will help you on Windows:")
        print("https://medium.com/@yadav-ajay/a-step-by-step-guide-to-setting-up-adb-path-on-windows-0b833faebf18")
        sys.exit()

    # Gets the service file.
    if arg1 == "get":

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
        # To prevent YandereDev-type code, lets dynamically change the name of the module we use.
        # Run the right script.
        module_name = f"service{arg2}"
        module = importlib.import_module(module_name)
        module.main()

        # Whatever arg2 is given will attempt to be imported as a module. Obviously this is bad because if the module doesnt exist then the script stops working.
        # Solution? Place all service scripts into service/. Uhh, then get a list of available scripts and check if the given arg2 matches.
        # Alternatively we could be really lazy and just manually add the scripts to the check, but come on, now.

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
    else:
        print("Invalid argument.")
if __name__ == "__main__":
    main()