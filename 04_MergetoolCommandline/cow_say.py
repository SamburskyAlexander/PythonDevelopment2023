import cmd
import shlex
import readline

import cowsay


def make_bubble_dict(opts):
    opt_dict = {
        'wrap_text': True,
        'width': 40,
        'brackets': cowsay.THOUGHT_OPTIONS['cowsay']
    } 
    if opts:
        if opts[0]:
            opt_dict['wrap_text'] = bool(opts[0] == 'True')
        if len(opts) > 1 and opts[1]:
            opt_dict['width'] = int(opts[1])
        if len(opts) > 2 and opts[2]:
            opt_dict['brackets'] = cowsay.THOUGHT_OPTIONS[opts[2]]
    return opt_dict


def make_cow_dict(opts):
    opt_dict = {
        'eyes': 'oo',
        'tongue': '  ',
        'cow': 'default'
    }
    if opts:
        if opts[0]:
            opt_dict['cow'] = opts[0]
        if (len(opts) > 1 and opts[1]):
            opt_dict['eyes'] = opts[1]
        if (len(opts) > 2 and opts[2]):
            opt_dict['tongue'] = opts[2]
    return opt_dict


def complete_cowact(text, line, begidx, endidx):
    args = shlex.split(line)
    if text == args[-1]:
        n_args = len(args) - 1
    else:
        n_args = len(args)
    
    eyes = ["OO", "XX", "DD", "YY", "QQ", "TT", "UU", "CC", "oo"]
    tongues = ["II", "VV", "U ", "WW", "UU"]
        
    if n_args == 2:
        cmplt_res = []
        for cow in cowsay.list_cows():
            if cow.startswith(text):
                cmplt_res.append(cow)
    elif n_args == 3:
        cmplt_res = []
        for eye in eyes:
            if eye.startswith(text):
                cmplt_res.append(eye)
    elif n_args == 4:
        cmplt_res = []
        for tongue in tongues:
            if tongue.startswith(text):
                cmplt_res.append(tongue)
    
    return cmplt_res


class MyCmdCowsay(cmd.Cmd):
    intro = "> Started cowsay cmd..."
    prompt = "(cowsay) >>> "
    
    
    def do_exit(self, arg):
        print("> Finished cowsay cmd...")
        return True

    
    def do_list_cows(self, arg):
        """
        list_cows [cowfiles_dir]
        Show all cow file names in the given directory or default cow list
        """
        if arg:
            cowfiles_dir = shlex.split(arg)
            cowlist = cowsay.list_cows(cowfiles_dir[0])
        else:
            cowlist = cowsay.list_cows()
            
        print(*cowlist)
    
    
    def do_make_bubble(self, arg):
        '''
        make_buble [text [width [brackets]]]
        Text that say cows
        '''
        msg, *opts = shlex.split(arg)
        opt_dict = make_bubble_dict(opts)
        print(cowsay.make_bubble(msg, 
                                 brackets=opt_dict['brackets'], 
                                 width=opt_dict['width'], 
                                 wrap_text=opt_dict['wrap_text'])
             )

        
    def complete_make_bubble(self, text, line, begidx, endidx):
        line_args = shlex.split(line)
        n_args = len(line_args)

        cmplt_3args_flg = n_args == 3 and line_args[-1] == text
        cmplt_2args_flg = n_args == 2 and line_args[-1] != text
        if (cmplt_3args_flg or cmplt_2args_flg):
            cmplt_result = []
            for res_comp in ['True', 'False']:
                if res_comp.lower().startswith(text.lower()):
                    cmplt_result.append(res_comp)
            return cmplt_result
    
    
    def do_cowsay(self, arg):
        """
        cowsay message [cow [eyes [tongue]]]
        Show cow say
        """
        msg, *opts = shlex.split(arg)
        opt_dict = make_cow_dict(opts)
        print(cowsay.cowsay(msg, 
                              eyes=opt_dict['eyes'], 
                              tongue=opt_dict['tongue'], 
                              cow=opt_dict['cow'])
             )
    
    
    def complete_cowsay(self, text, line, begidx, endidx):
        return complete_cowact(text, line, begidx, endidx)
    
    
    def do_cowthink(self, arg):
        """
        cowthink message [cow [eyes [tongue]]]
        Show cow think
        """
        msg, *opts = shlex.split(arg)
        opt_dict = make_cow_dict(opts)
        print(cowsay.cowthink(msg, 
                            eyes=opt_dict['eyes'], 
                            tongue=opt_dict['tongue'], 
                            cow=opt_dict['cow'])
             )
    
    
    def complete_cowthink(self, text, line, begidx, endidx):
        return complete_cowact(text, line, begidx, endidx)
    
    
if __name__ == "__main__":
    MyCmdCowsay().cmdloop()