# CLI and Comand line arguments

A command-line interface (CLI) is a text-based method of interacting with a program by typing commands into a terminal or console.

Command line arguments:
-> Command line arguments are parameters passed to a script when it’s executed from the command line interface. These arguments allow users to customize how a Python program runs without modifying the source code. 
By accepting command line arguments, Python scripts become more flexible, reusable, and suitable for automation.

Python provides three main ways to handle command-line arguments:
  1) sys.argv: A simple way to access command-line arguments as a list of strings.
  2) getopt: A built-in module for parsing command-line options and arguments in a structured way.
  3) argparse: An advanced and flexible module that provides built-in validation, help messages, and better argument handling.


## sys.argv 
### Check `script_1.py` for implementation example)
Run script using the following command:

`>> python script_name.py <number1> <number2>`

- `python` - run Python interpreter
- `script_name.py` - Python file
- `<number1>`, `<number2>` - command line arguments

### example

`>> python script.py 3.5 2`
