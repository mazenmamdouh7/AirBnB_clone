#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""
    
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit command on EOF."""
        print()
        return True

    def help_quit(self):
        """Help information for the quit command."""
        print("Quit command to exit the program.")

    def help_EOF(self):
        """Help information for the EOF command."""
        print("Exit command on End Of File (Ctrl+D).")

    def emptyline(self):
        """Override emptyline method to
        not execute anything on an empty line."""
        pass

    def do_help(self, line):
        """Display help information."""
        if not line:
            cmd.Cmd.do_help(self, line)
        else:
            try:
                func = getattr(self, 'help_' + line)
                func()
            except AttributeError:
                print(f"No help on '{line}'")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
