#!/usr/local/bin/env python
import os
import sys


#############
# Variables #
#############
cwd = os.getcwd()
args = sys.argv[1:]


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
    # functions["version"] = print_version
    # functions["new"] = new_save
    # functions["swap"] = swap_save
    return functions

#########################
# Execute Script (Main) #
#########################
def main():
    parse_args(args)

if __name__ == '__main__':
    sys.exit(main())