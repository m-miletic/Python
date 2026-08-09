import sys
import getopt
## 1) sys.argv
## --- accesing command line arguments using sys.argv ---

arguments = sys.argv # List of command line arguments passed to the script
print(f"sys.argv: {arguments}")
script_name = arguments[0] # The name of the script being executed

if len(arguments) > 0:
    first_argument = arguments[0]
else:
    first_argument = None



opts, args = getopt.getopt(sys.argv[1:], "v:", ["file="])
print(f"opts: {opts}")
print(f"args: {args}")