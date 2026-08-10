import argparse

## initialization of ArgumentParser object
parser = argparse.ArgumentParser(
    description="A script that takes an input file and output file."
)

## defining the input argument
parser.add_argument("input", help="The input file to proces.")


## defining the output argument
parser.add_argument(
    "-o", "--output", help="The output file to save the results", required=True
)

## parse command-line arguments
args = parser.parse_args()

## example processing
with open(args.input, "r") as infile:
    data = infile.read()

## writing data to output file
with open(args.output, "w") as outfile:
    outfile.write(data)


print(f"Data form {args.input} has been written to {args.output}")