import cmd
import shlex
import readline


class MyCmdCowsay(cmd.Cmd):
    def do_exit(self, arg):
        return True

    # implement list_cows, make_bubble, cowsay и cowthink
    
    
if __name__ == "__main__":
    MyCmdCowsay().cmdloop()