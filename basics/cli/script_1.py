import sys

## --- using sys.argv ---

if(len(sys.argv) < 3):
    print("Warning: Insufficient arguments provided!")
    print("Correct usage: python [script_name].py [arg1]<number> [arg2]<number>")
    sys.exit(1) # stop program with exit code 1 (error)
    # 0 → success
    # non-zero → something went wrong

script_name = sys.argv[0]
number1 = float(sys.argv[1])
number2 = float(sys.argv[2])

print(f"Script name: {script_name}")
print(f"Number 1: {number1}")
print(f"Number 2: {number2}")

product = number1 * number2
print(f"Product: {product}")