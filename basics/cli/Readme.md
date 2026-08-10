# Command Line Interface & Command Line Arguments

A command-line interface (CLI) is a text-based method of interacting with a program by typing commands into a terminal or console.

Command line arguments:
-> Command line arguments are parameters passed to a script when it’s executed from the command line interface. These arguments allow users to customize how a Python program runs without modifying the source code. 
By accepting command line arguments, Python scripts become more flexible, reusable, and suitable for automation.

Python provides three main ways to handle command-line arguments:
  1) sys.argv: A simple way to access command-line arguments as a list of strings.
  2) getopt: A built-in module for parsing command-line options and arguments in a structured way.
  3) argparse: An advanced and flexible module that provides built-in validation, help messages, and better argument handling.


## sys.argv 
### Check `script_1.py` for implementation example
Run script using the following command:

`>> python script_name.py <number1> <number2>`

- `python` - run Python interpreter
- `script_name.py` - Python file
- `<number1>`, `<number2>` - command line arguments

### How to Execute the Script

`>> python script.py 3.5 2`

## getopt
### Check `script_2.py` for implementation example
While sys.argv works for basic argument handling, it lacks structure when handling optional arguments or flags. The getopt module helps by providing a more organized way to parse command-line arguments.
### Syntax for getopt in Python:
`>> getopt.getopt(args, short_options, long_options)`

- `args` - List of command-line arguments
- `short_options` - A string of single-character options
- `long_options` -  List of long-form options

In `short_options` a colon (`:`) indicates that a value is required. It doesn't mean that the option is mandatory but if option is used value needs to be given.
In `long_options` an equality sign (`=`) has the same functionality.

NOTE: How to distinguish option from an argument!?  

- option - an option is introduced by `-` for `short_options` or `--` for `long_options`  
- argument - positional value that isn't attached to an option (for the example below input.txt and result.py are options and there is no arguments).
#### The script performs the same task whether the value is provided as a positional argument or as an option value. The difference is only in the way the value is passed to the script!

### How to Execute the Script  
As it can be seen in the example below short and long options can be used together in the same command

`>> python script.py -f input.txt --output result.txt`

## argparse  
### Check `script_3.py` for implementation (and syntax) example  
The argparse module, simplifies command-line argument handling by offering built-in support for required and optional arguments, flags, automatic help messages, and type validation.  
### Syntax for argparse:  
```
>> parser = argparse.ArgumentParser(description="Script description here")
>> parser.add_argument("positional_arg", help="Description of positional argument")
>> parser.add_argument("-o", "--optional", help="Description of optional argument") 
>> parser.add_argument("-f", "--flag", action="store_true", help="Boolean flag argument")
>> args = parser.parse_args()
```

 - `argparse.ArgumentParser` Creates a new argument parser object.  
 - `add_argument` Defines the arguments the script accepts.
 - `parse_args` Parses the command-line arguments and returns a Namespace object with attributes.

### How to Execute the Script

`>> python argparse_output_example.py input.txt -o output.txt` 


 ### Common arguments used with argparse  

 <img width="660" height="386" alt="argparsePNG" src="https://github.com/user-attachments/assets/a24e6566-b6d4-4968-8c62-4dd876eff1f2" />

 
