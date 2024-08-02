import sys
import subprocess
import importlib
import shutil
import os
import traceback
import io
import contextlib
import platform
osDetect = platform.system()
import pydoc 

sys.path.append("services") # Adds the "services" folder to path.
import services # Imports the service folder.

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
view <service>  - Fetch & view the service log without parsing or saving.""")
        sys.exit(1)

    # $1
    arg1 = sys.argv[1]

    # $2
    arg2 = sys.argv[2] if len(sys.argv) > 2 else None
    # We use camelCase. Capitalise the start of whatever arg2 is given.
    arg2 = arg2.capitalize() if len(sys.argv) > 2 else None

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

        # If user forgot to give a second arg, remind them.
        if not arg2: 
            print("get <service>")
            sys.exit()

        # It's really dumb, but we need to actually lowercase this or it won't work.
        arg2 = arg2.lower()

        # First, we get the list of processes.
        result = subprocess.run(["adb", "shell", "dumpsys", arg2], capture_output=True)
        output = result.stdout.decode('utf-8')  # Decode the byte output to a string. This makes newliens (\n) actually work as intended.
        
        index = output.find(arg2) # Look for arg2 in output.
        if index != -1: # If its there, then do the stuff. Write output to file.
            try:
                output_file = f"{arg2}.oxidize"
                with open(output_file, "wb") as f:
                    output = output.encode('utf-8')  # I will be honest, I don't know why I suddenly have to re-encode back to bytes. 
                    f.write(output)
                print("Written to",output_file)
            except Exception as e:
                print("Unexpected exception!")
                print(traceback.format_exc())
        else:
            print("Can't find service OR device not connected!")

    elif arg1 == "list":
        # Run dumpsys -l, aka "show us packages".
        result = subprocess.run(["adb", "shell", "dumpsys", "-l"], capture_output=True)
        output = result.stdout.decode('utf-8')  # Decode the byte output to a string. This makes newliens (\n) actually work as intended.
        print(output)

    elif arg1 == "run":

        if not arg2: 
            print("run <service>")
            sys.exit()
        # To prevent YandereDev-type code, lets dynamically change the name of the module we use.
        # Run the right script.
        try:
            moduleName = f"service{arg2}"
            module = importlib.import_module(moduleName)
            
            # String buffer to capture stdout.
            buffer = io.StringIO()

            # Direct stdout to buffer.
            with contextlib.redirect_stdout(buffer):
                module.main()

            # Actually getting the results from the buffer
            bufferOutput = buffer.getvalue()

            # Print the captured output to the terminal.
            print(bufferOutput)
        
            # Write the captured output to a file
            with open(f"parsed{arg2}.oxidize", "w") as file:
                file.write(bufferOutput)
            print(f"Written to parsed{arg2}.oxidize.")
        except ModuleNotFoundError:
            print("Can't find script! Check your spelling or if it even exists.")
        except AttributeError:
            print("Script is missing main func! It probably ran anyway.")
        except Exception as e:
            print("Unexpected exception!")
            print(traceback.format_exc())

    elif arg1 == "view":

        if not arg2: 
            print("view <service>")
            sys.exit()

        arg2 = arg2.lower()
        result = subprocess.run(["adb", "shell", "dumpsys", arg2], capture_output=True)
        output = result.stdout.decode('utf-8')
        
        index = output.find(arg2) # Look for arg2 in output.
        if index != -1: # If its there, then do the stuffs  
            if osDetect == "Linux": # Are we running Linux? If so, pipe it into "less" instead.
                try:
                    subprocess.run(['less'], input=output, text=True)
                except Exception as e:
                    print("Unexpected exception!")
                    print(traceback.format_exc())
            else: # If we aren't on Linux, then use pydoc. Which is basically "more".
                pydoc.pager(output)
        else:   
            print("Can't find service OR device not connected!")

    elif arg1 == "opt":
        print(f"pypager:",pagerAvailable)
    else:
        print("Invalid argument.")
if __name__ == "__main__":
    main()