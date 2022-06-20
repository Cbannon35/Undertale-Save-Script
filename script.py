#!/usr/local/bin/env python

import os
import sys


#############
# Variables #
#############
cwd = os.getcwd()
args = sys.argv[1:]
version = "0.2.0"
# Folder undertale stuff lives in (specifically on macOS + Steam)
undertale_dir = os.path.expanduser("~/Library/Application Support/com.tobyfox.undertale/")
if not os.path.isdir(undertale_dir):
    print("Could not locate undertale directory. Please make sure you are using macOS and playing undertale on Steam.")
    sys.exit(1)

#############
# Functions #
#############
def parse_args(args):
    """ Parses the arguments passed to the script. 
    Handles the cases of incorrect arg length and invalid args. 
    Otherwise, calls the appropriate function. """
    if len(args) == 0:
        print_all_help()
        sys.exit(1)
    else:
        # parse function and its arguments
        command = args[0]
        args = args[1:]
        # fetch function 
        commands = fetch_functions()
        command_func = commands[command]
        # call function
        command_func(args)

def print_all_help():
    """ Prints all commands and their descriptions. """
    commands = fetch_commands_help()
    print("List of valid commands:")
    for command in commands:
        print("\n{}:\n{}".format(command, commands[command]))
    sys.exit(1)

###########################
# Functions in "commands" #
###########################
def help(args=[]):
    """ Prints the help for a command. Depends on the command passed. """
    commands = fetch_commands_help()
    if args:
        for arg in args:
            if arg == "help":
                #TODO: print randomized funny stuff ?? audio files ? outputs slowly ?
                print("lol")
            elif arg in commands:
                print("Argument: {}\n--Description:--\n {}".format(arg, commands[arg]))
            else:
                print("Invalid command: {}".format(arg))
    else:
        # print all commands and their descriptions
        print_all_help()

def print_version(args=[]):
    """ Prints the version of this script. """
    if args:
        print("You passed in too many arguments but this function still works anyways :p\n\n")
    #TODO: funny stuff depending on num args ?
    print("Undertale Save Swapper v{}".format(version))

def new_save(args):
    """ Creates a new save file. """
    if len(args) == 1:
        save_name = args[0]
        save_path = os.path.join(cwd, save_name)
        if os.path.exists(save_path):
            print("File already exists: {}".format(save_path))
            sys.exit(1)
        else:
            with open(save_path, "w") as f:
                f.write("")
            print("Created file: {}".format(save_path))
    else:
        print("Invalid number of arguments: {}".format(len(args)))
        sys.exit(1)

def swap_save(args):
    """ Swaps the save file of undertale. """
    if len(args) == 2:
        save_name = args[0]
        save_path = os.path.join(cwd, save_name)
        if os.path.exists(save_path):
            with open(save_path, "w") as f:
                f.write("")
            print("Created file: {}".format(save_path))
        else:
            print("File does not exist: {}".format(save_path))
            sys.exit(1)
####################
# Helper Functions #
####################
def fetch_commands_help():
    """ Returns a dictionary of commands and their descriptions. 
    For use in print_help(). """
    commands = {}
    # commands['command'] = 'description'
    # help
    commands["help"] = "!!Optional!! <arg1> <arg2> ...\nPrints a list of all commands and their discriptions.\nOr as many commands the user inputs."
    # version
    commands["version"] = "Takes no arguments.\nPrints the version of this script."
    # new
    commands["new"] = "<arg1>\n1. The name of the file in which to store the current session of undertale."
    # swap
    commands["swap"] = "<arg1> <arg2>\n1. The name of the file storing the save of undertale you want to load\n2. The name of the file in which you want to save the current session of undertale."
    return commands

def fetch_functions():
    """ Returns a dictionary of commands and their functions. 
    For use in parse_args(). """
    functions = {}
    # functions['command'] = function
    functions["help"] = help
    functions["version"] = print_version
    functions["new"] = new_save
    functions["swap"] = swap_save
    return functions

#########################
# Execute Script (Main) #
#########################
def main():
    parse_args(args)

if __name__ == '__main__':
    sys.exit(main())