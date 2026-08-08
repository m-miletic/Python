import sys
import getopt

## --- using getopt ---

try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        "n:m:",
        ["number1=", "number2="]
    )
except getopt.GetoptError as err:
    print(f"Error: {err}")
    sys.exit(1)

if len(opts) < 2:
    print("Warning: Both numbers must be provided!")
    print("Correct usage: python script.py -n [number1] -m [number2]")
    sys.exit(1)

number1 = None
number2 = None

for opt, value in opts:
    if opt in ("-n", "--number1"):
        number1 = float(value)

    elif opt in ("-m", "--number2"):
        number2 = float(value)

product = number1 * number2

print(f"Number 1: {number1}")
print(f"Number 2: {number2}")
print(f"Product: {product}")


## Better usage example:

## backup example TODO