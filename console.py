#!/usr/bin/python3

""" The console program implementation """


import cmd

class HBNBCommand(cmd.Cmd):
    """ Implements the cmd feature of the console """

    ##############################
    # class attributes overrides #
    ##############################
    prompt = "(hbnb) "

    ###############################
    # instance methods ovverrides #
    ###############################
    def postloop(self):
        print("")

    #####################
    # Commands handlers #
    #####################
    def emptyline(self):
        return False

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True
    
    ################
    # command help #
    ################
    def help_quit(self):
        print("Quit command to exit program\n")
    def help_EOF(self):
        print("Ctrl + D (EOF) to exit program\n")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
