#!/usr/bin/python3

""" The console program implementation """


import cmd

class HBNBCommand(cmd.Cmd):
    """ Implements the cmd feature of the console """


    prompt = "(hbnb) "
    def emptyline(self):
        """ executes when an empty line is entered """
        return ""


    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """ handle end-of-string charater
            ie. Ctrl+D
        """
        return True

    def postloop(self):
        """ run before cmdloop ends """
        print("")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
