"""
    This file contains code that is used to pull hardware information from the system it runs on. It is being created off of the Python Institute course Python Essentials Module 2. It will be added to as the developer learns more about Python and how to interact with the system it runs on.

    Any function calls will have a comment below them explaining what they do and what they return. This will help the developer understand what is happening in the code and how to use it in the future. This information will primarily be sourced from docs.python.org/3/library/


"""

# Import the platform module, which contains functions to interact with the system
import platform
# Import the os module, which contains functions to interact with the operating system. Only functions to read the system information are used in this script. More complex functions will be explored in a future project.
import os


# Function to get the system information
# Only functions on Unix systems
# Un-comment to enable

# os.uname()

# os.uname()¶
# Returns information identifying the current operating system. The return value is an object with five attributes:

# sysname - operating system name

# nodename - name of machine on network(implementation-defined)

# release - operating system release

# version - operating system version

# machine - hardware identifier

# For backwards compatibility, this object is also iterable, behaving like a five-tuple containing sysname, nodename, release, version, and machine in that order.

# Some systems truncate nodename to 8 characters or to the leading component
# a better way to get the hostname is socket.gethostname() or even socket.gethostbyaddr(socket.gethostname()).

# On macOS, iOS and Android, this returns the kernel name and version(i.e., 'Darwin' on macOS and iOS
# 'Linux' on Android). platform.uname() can be used to get the user-facing operating system name and version on iOS and Android.

# Availability: Unix.


# -------------------------------------
# Cross platform specific functions
# -------------------------------------

# Function to get the OS name

system = platform.system()

# Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. An empty string is returned if the value cannot be determined.

# On iOS and Android, this returns the user-facing OS name(i.e, 'iOS, 'iPadOS' or 'Android'). To obtain the kernel name ('Darwin' or 'Linux'), use os.uname().


# Function to get the system release version

system_version = platform.version()

# Returns the system’s release version, e.g. '#3 on degas'. An empty string is returned if the value cannot be determined.

# On iOS and Android, this is the user-facing OS version. To obtain the Darwin or Linux kernel version, use os.uname().


# Function to get the system information

uname = platform.uname()

uname_system = uname.system
uname_node = uname.node
uname_release = uname.release
uname_version = uname.version
uname_machine = uname.machine
uname_processor = uname.processor

# Fairly portable uname interface. Returns a namedtuple() containing six attributes: system, node, release, version, machine, and processor.

# processor is resolved late, on demand.

# Note: the first two attribute names differ from the names presented by os.uname(), where they are named sysname and nodename.

# Entries which cannot be determined are set to ''.

# Changed in version 3.3: Result changed from a tuple to a namedtuple().

# Changed in version 3.9: processor is resolved late instead of immediately.


# Function to get the marketing name for the OS

system_alias = platform.system_alias(
    platform.system(), uname_release, platform.version())

# Returns(system, release, version) aliased to common marketing names used for some systems. It also does some reordering of the information in some cases where it would otherwise cause confusion.

# Function to get the system architecture information

arch = platform.architecture()

arch_bits = arch[0]
arch_linkage = arch[1]

# Queries the given executable(defaults to the Python interpreter binary) for various architecture information.

# Returns a tuple(bits, linkage) which contain information about the bit architecture and the linkage format used for the executable. Both values are returned as strings.

# Values that cannot be determined are returned as given by the parameter presets. If bits is given as '', the sizeof(pointer) ( or sizeof(long) on Python version < 1.5.2) is used as indicator for the supported pointer size.

# The function relies on the system’s file command to do the actual work. This is available on most if not all Unix platforms and some non-Unix platforms and then only if the executable points to the Python interpreter. Reasonable defaults are used when the above needs are not met.

# Note On macOS ( and perhaps other platforms), executable files may be universal files containing multiple architectures.
# To get at the “64-bitness” of the current interpreter, it is more reliable to query the sys.maxsize attribute:

# is_64bits = sys.maxsize > 2**32


# Function to get the processor type

processor = platform.processor()

# Returns the(real) processor name, e.g. 'amdk6'.

# An empty string is returned if the value cannot be determined. Note that many platforms do not provide this information or simply return the same value as for machine(). NetBSD does this.


# Function to get the machine type

machine = platform.machine()

# Returns the machine type, e.g. 'AMD64'. An empty string is returned if the value cannot be determined.


# Function to get the platform information

plat = platform.platform()

# Returns a single string identifying the underlying platform with as much useful information as possible.

# The output is intended to be human readable rather than machine parseable. It may look different on different platforms and this is intended.

# If aliased is true, the function will use aliases for various platforms that report system names which differ from their common names, for example SunOS will be reported as Solaris. The system_alias() function is used to implement this.

# Setting terse to true causes the function to return only the absolute minimum information needed to identify the platform.


# -------------------------------------
# Windows platform specific functions
# -------------------------------------


# Function to get the OS release information

win32_ver = platform.win32_ver()

w_release = win32_ver[0]
w_version = win32_ver[1]
w_csd = win32_ver[2]
w_ptype = win32_ver[3]

# platform.win32_ver(release='', version='', csd='', ptype='')
# Get additional version information from the Windows Registry and return a tuple(release, version, csd, ptype) referring to OS release, version number, CSD level(service pack) and OS type(multi/single processor). Values which cannot be determined are set to the defaults given as parameters(which all default to an empty string).

# As a hint: ptype is 'Uniprocessor Free' on single processor NT machines and 'Multiprocessor Free' on multi processor machines. The 'Free' refers to the OS version being free of debugging code. It could also state 'Checked' which means the OS version uses debugging code, i.e. code that checks arguments, ranges, etc.


# Function to check current Window edition information

win32_edition = platform.win32_edition()

# Returns a string representing the current Windows edition, or None if the value cannot be determined. Possible values include but are not limited to 'Enterprise', 'IoTUAP', 'ServerStandard', and 'nanoserver'.


# Function to check if Windows is an IoT edition

is_iot = platform.win32_is_iot()

# Returns True if the current Windows edition is an IoT edition, False otherwise.


# -------------------------------------
# Python information functions
# -------------------------------------


# Function to get the Python build

py_build = platform.python_build()

py_build_number = py_build[0]
py_build_date = py_build[1]

# Returns a tuple(buildno, builddate) stating the Python build number and date as strings.


# Function to get the Python compiler

py_compiler = platform.python_compiler()

# Returns a string identifying the compiler used for compiling Python.


# Frunction to get the Python branch

py_branch = platform.python_branch()

# Returns a string identifying the Python implementation SCM branch.


# Function to get the Python implementation

py_implementation = platform.python_implementation()

# Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.


# Function to get the Python revision

py_revision = platform.python_revision()

# Returns a string identifying the Python implementation SCM revision.


# Function to get the Python version

py_version = platform.python_version()

# Returns the Python version as string 'major.minor.patchlevel'.

# Note that unlike the Python sys.version, the returned value will always include the patchlevel(it defaults to 0).


# Function to get the Python version tuple

py_version_t = platform.python_version_tuple()

py_version_major = py_version_t[0]
py_version_minor = py_version_t[1]
py_version_patch = py_version_t[2]

# Returns the Python version as tuple(major, minor, patchlevel) of strings.

# Note that unlike the Python sys.version, the returned value will always include the patchlevel(it defaults to '0').


def sys_info():
    print("System Information: ")
    print("-------------------")
    print(f"Processor: {processor}")
    print(f"Machine: {machine}")
    print(f"System: {system}")
    print(f"System Alias: {system_alias}")
    print(f"System Version: {system_version}")
    print(f"Windows Edition: {win32_edition}")
    print(f"Is Windows an IoT Edition release?: {is_iot}")
    print()


def win_info():
    print("Windows Information: ")
    print("--------------------")
    print(f"Windows Release: {w_release}")
    print(f"Windows Version: {w_version}")
    print(f"Windows CSD: {w_csd}")
    print(f"Windows Processor Type: {w_ptype}")
    print()


def uname_info():
    print("Uname System Information: ")
    print("-------------------------")
    print(f"System: {uname_system}")
    print(f"Node: {uname_node}")
    print(f"Release: {uname_release}")
    print(f"Version: {uname_version}")
    print(f"Machine: {uname_machine}")
    print(f"Processor: {uname_processor}")
    print()


def arch_info():
    print("System Architecture Information: ")
    print("--------------------------------")
    print(f"Bits: {arch_bits}")
    print(f"Linkage: {arch_linkage}")
    print()


def plat_info():
    print("Platform Information: ")
    print("---------------------")
    print(f"Platform: {plat}")
    print()


def py_info():
    print("Python Information: ")
    print("-------------------")
    print(f"Python Build Number: {py_build_number}")
    print(f"Python Build Date: {py_build_date}")
    print(f"Python Compiler: {py_compiler}")
    print(f"Python Branch: {py_branch}")
    print(f"Python Implementation: {py_implementation}")
    print(f"Python Revision: {py_revision}")
    print(f"Python Version: {py_version}")
    print(f"Python Version - major: {py_version_major}")
    print(f"Python Version - minor: {py_version_minor}")
    print(f"Python Version - patch: {py_version_patch}")
    print()


def main():
    print()
    # Call the functions to get the system information
    sys_info()
    # Call the functions to get the Windows information
    win_info()
    # Call the functions to get the uname information
    uname_info()
    # Call the functions to get the architecture information
    arch_info()
    # Call the functions to get the platform information
    plat_info()
    # Call the functions to get the Python environment information
    py_info()
    print()
    close = input("Press Enter to close the program...")


main()
