#!/usr/local/bin/env python

import os
import sys


#############
# Variables #
#############


cwd = os.getcwd()
args = sys.argv[1:]
version = "1.0.0-Beta"
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
        #TODO: print random funny stuff ?
        print_all_help()
        sys.exit(1)
    else:
        # parse function and its arguments
        command = args[0]
        args = args[1:]
        # fetch function 
        commands = fetch_functions()
        if command in commands.keys():
            command_func = commands[command]
            # call function
            command_func(args)
        else:
            print("Invalid command: {}".format(command))
            sys.exit(1)

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

def save(args):
    """ Creates a new save file. """
    if len(args) == 1:
        save_name = args[0]
        save_path = os.path.join(cwd, save_name)
        # undertale_dir --> save_path
        #            d1 --> d2
        # move all files from undertale to new save directory
        transfer(undertale_dir, save_path)
    else:
        print("Invalid number of arguments: {}".format(len(args)))
        sys.exit(1)

def load(args):
    """ Loads a save file. """
    if len(args) == 1:
        load_name = args[0]
        load_path = os.path.join(cwd, load_name)
        # undertale_dir --> save_path
        #            d1 --> d2
        # move all files from undertale to new save directory
        if is_valid_undertale_dir(load_path):
            transfer(load_path, undertale_dir)
        else:
            sys.exit(1)
    else:
        print("Invalid number of arguments: {}".format(len(args)))
        sys.exit(1)

def swap_save(args):
    """ Swaps the save file of undertale. """
    if len(args) == 2:
        load_name, save_name = args[0], args[1]
        load_path, save_path = os.path.join(cwd, load_name), os.path.join(cwd, save_name)
        # Check if you are loading a valid file 
        if not os.path.exists(load_path):
            print("Invalid load file: {}".format(load_name))
            sys.exit(1)

        # move all files from undertale to new or existing save directory
        transfer(undertale_dir, save_path)

        # move all files from load_path to undertale
        transfer(load_path, undertale_dir)
    else:
        print("Invalid number of arguments: {}".format(len(args)))
        sys.exit(1)

def play(args):
    """ Starts undertale. """
    if len(args) == 0:
        undertale = os.path.expanduser("/Applications/Undertale.app")
        if not os.path.exists(undertale):
            print("Could not find undertale. Please make Undertale is in your applications folder.")
            sys.exit(1) 
        else:
            os.system("open {}".format(undertale))
    else:
        print("Invalid number of arguments: {}".format(len(args)))
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
    functions["save"] = save
    functions["load"] = load
    functions["swap"] = swap_save
    functions["play"] = play
    return functions

def transfer(d1, d2):
    """ Moves the contents of d1 to d2. (Ignoring config file) """
    if is_valid_undertale_dir(d1):
        if not os.path.exists(d2):
            # make d2 if it doesn't exist
            os.makedirs(d2)
        elif len(os.listdir(d2)) == 1 and os.listdir(d2)[0] == "config.ini":
            pass # handle the case where undertale_dir should always have config.ini
        elif len(os.listdir(d2)) > 0:
             # if d2 exists and is not empty, ask user if they want to overwrite
            warning_overwrite(d2)
        # Move files over
        for file in os.listdir(d1):
            if file == "config.ini": # ignore config file --> should this be toggle-able?
                continue
            os.rename(os.path.join(d1, file), os.path.join(d2, file))
    else:
        print("Invalid directory: {}".format(d1))
        sys.exit(1)

def is_valid_undertale_dir(d):
    """ Checks if d is a valid undertale directory. """
    files = {"undertale.ini": 3, "file0": 17, "file9": 27}
    if os.path.exists(d) and os.path.isdir(d):
        d_as_list = os.listdir(d)
        if len(d_as_list) >= 3: # should only have 3 files in undertale directory
            #TODO: make a better file validity check
            test = 0 # if 3 files are found test will add up to the correct number
            for file in os.listdir(d):
                if file in files:
                    test += files[file]
            if test == 47:
                return True
            else:
                print("Invalid files in directory: {}\n{}".format(d, d_as_list))
                return False
        else:
            print("Incorrect number of files in directory: {}".format(d))
            return False
    return False

def warning_overwrite(d):
    """ Prints a warning that the save directory is not empty. """
    print("Warning: {} isn't empty. Potentially overwriting existing data.".format(d))
    def wait_for_input():
        """ Waits for user input. """
        y_or_n = input("Continue? (y/n): ")
        if y_or_n == "y":
            print("Overwriting...")
            return
        elif y_or_n == "n":
            print("Aborting...")
            sys.exit(1)
        else:
            print("Invalid input: {}".format(y_or_n))
            wait_for_input()
    wait_for_input()


#########################
# Execute Script (Main) #
#########################
def main():
    parse_args(args)

if __name__ == '__main__':
    sys.exit(main())