import sys 
import getopt 

## --- using getopt ---

## sys.argv[1:] -> removes the script name
## short_options and long_options can be combined in the same call 

try: 
  opts, args = getopt.getopt(sys.argv[1:], "f:o:", ["file=", "output="]) 
except getopt.GetoptError as err: 
  print(f"Error: {err}") 
  sys.exit(1) 

for opt, arg in opts: 
  if opt in ("-f", "--file"): 
    print(f"Input file: {arg}") 
  elif opt in ("-o", "--output"): 
    print(f"Output file: {arg}") 
