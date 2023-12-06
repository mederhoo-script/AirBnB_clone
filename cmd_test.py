#!/usr/bin/python3

import cmd

class MyCmdInterpreter(cmd.Cmd):
    prompt = ">>> "

    def do_hello(self, arg):
        """Print a greeting. Usage: hello [name]"""
        if arg:
            print(f"Hello, {arg}!")
        else:
            print("Hello!")

    def do_exit(self, arg):
        """Exit the command interpreter."""
        print("Exiting...")
        return True  # This will exit the command loop

    # You can define more commands by adding additional methods here

if __name__ == "__main__":
    my_cmd = MyCmdInterpreter()
    my_cmd.cmdloop("Welcome to MyCmdInterpreter. Type 'help' for a list of commands.")
