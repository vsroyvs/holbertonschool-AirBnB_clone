#!/usr/bin/python3
"""module console that contains the entry point
of the command interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit Command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def emptyline(self):
        """Empty lines are ignored"""
    pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
