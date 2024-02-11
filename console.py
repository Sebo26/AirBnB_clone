#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Creates entry point of the command interpreter"""
    HBNBCommand().cmdloop()
    HBNBCommand().emptyline()
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Comaand to quit"""
        return True
    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
