import os
import socket
import sys
import time

# Get the machine type
print("Machine type:", os.uname().machine)

# Get the processor type (for Linux, macOS)
if os.name == 'posix':
    try:
        if 'Linux' in os.uname().sysname:
            # For Linux, read processor info from /proc/cpuinfo
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        print("Processor type (Linux):", line.split(":")[1].strip())
                        break
        elif 'Darwin' in os.uname().sysname:
            # For macOS, use sysctl to get processor info
            processor = os.popen('sysctl -n machdep.cpu.brand_string').read().strip()
            print("Processor type (macOS):", processor)
    except Exception as e:
        print("Error retrieving processor info:", e)

# Set the default timeout for a socket (in seconds) to 50 seconds
socket.setdefaulttimeout(50)
print("Default socket timeout:", socket.getdefaulttimeout())

# Get the operating system name
print("Operating system name:", os.name)

# Get the current process ID
print("Current process ID:", os.getpid())

# Fork a new process (Unix-based systems only)
pid = os.fork()

if pid == 0:
    # This is the child process
    print(f"Child Process ID: {os.getpid()}")

    # Ensure the file path is valid and accessible (create it in the current directory)
    file_path = os.path.join(os.getcwd(), 'fdpractice.txt')

    try:
        # Open (or create) a file named fdpractice.txt
        with open(file_path, 'w+') as file:
            # Write the current process id to the file
            file.write(f"Process ID from Child: {os.getpid()}\n")

            # Move the file pointer back to the beginning
            file.seek(0)

            # Read and print the first 100 bytes from the file
            contents = file.read(100)
            print("Child reads from file:", contents)
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

    # Exit the child process
    os._exit(0)

else:
    # This is the parent process
    print(f"Parent Process ID: {os.getpid()}")

    # Wait for the child process to finish
    os.wait()

    # Ensure the file path is valid and accessible (create it in the current directory)
    file_path = os.path.join(os.getcwd(), 'fdpractice.txt')

    try:
        # Open the file again for reading and writing
        with open(file_path, 'r') as file:
            # Read and print the file's contents in the parent process
            contents = file.read()
            print("Parent reads from file:", contents)

        # Close the file
        file.close()
    except Exception as e:
        print(f"Error reading from file {file_path}: {e}")
