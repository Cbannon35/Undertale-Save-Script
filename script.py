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
def parse_args():
    if len(args) == 0:
        # send help message if no arguments are given
        print_help()
        sys.exit(1)
    elif len(args) == 1:
        print_help(args[0])
        sys.exit(1)
    else:
        pass

def print_help(command=None):
    """ Prints a list of all commands and their descriptions.
    Or just a singular command dependent upon user input. """
    commands = retrieve_commands()
    if command is not None:
        # print help for specific command (if valid)
        if command in commands:
            print(commands[command])
        else:
            print("Please enter a valid command.")
    else:
        print("List of valid commands:")
        for command in commands:
            print("\n")
            print(command + ":\n " + commands[command])

def retrieve_commands():
    """ Returns a dictionary of commands and their descriptions. """
    commands = {}
    # commands['command'] = 'description'
    # help
    commands["help"] = "Takes no arguments.\nPrints a list of all commands and their discriptions."
    # version
    commands["version"] = "Takes no arguments.\nPrints the version of this script."
    # new
    commands["new"] = "Takes 1 argument:\n 1. The name of the file in which to store the current session of undertale."
    # swap
    commands["swap"] = "Takes 2 arguments:\n1. The name of the file storing the save of undertale you want to load\n2. The name of the file in which you want to save the current session of undertale."
    return commands

#########################
# Execute Script (Main) #
#########################
def main():
    parse_args()

if __name__ == '__main__':
    sys.exit(main())