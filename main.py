#!/usr/bin/env python3

try:
    from cvelookup.db.dblookup import Database
    from colored import fg, attr
    import subprocess
    import sys
    import os
    if os.name != 'nt':
        import readline
except ImportError as err:
    print(err)

VALID_OPERATORS = (">", "<", "=" , ">=", "<=")

class CveLookup:
    def __init__(self):
        """Creates a `Dbutils` objects and a dictionary
        containing all valid commands and there corresponding
        functions.
        """
        self.database_obj = Database()
        self.command_dict = {
           'showcve': self.showcve,
           'showall': self.showall,
           'search': self.search,
           'year': self.year,
           'update': self.update,
           'exec': self.exec,
           'exit': self.exit,
           'cls': self.clear,
           'help': self.get_help
        }

    def initiate(self):
        """Displays prompt and handles all commands"""
        while True:
            user_input = input(("%scvelookup%s" % (fg(99), attr(0))) + " > ").strip().split()
            cmd = user_input[0].strip()
            if cmd in self.command_dict.keys():
                args = [arg.strip() for arg in user_input[1:]]
                if len(args) == 0:
                    self.command_dict[cmd]()
                    continue
                self.command_dict[cmd](args)
            else:
                print("%s[!] Invalid command%s" % (fg(9), attr(0)))

    def year(self, args):
        """Returns the CVE by year or range of years"""
        if args[0] not in VALID_OPERATORS:
            print("\n%s[-] Invalid operator... see help menu by typing `help` %s" % (fg(9), attr(0)))
            return
        print("\n%s[*] Performing search for CVE where year is%s" % (fg(49), attr(0)), args[0], args[1])
        self.database_obj.search_year(args)

    def update(self):
        """Calls `updatedb` from `dbutils.py` to update the CVE database"""
        print("\n[+] --------------------------- %sUpdating database%s ---------------------------" % (fg(49), attr(0)))
        self.database_obj.updatedb()
        print("%s[*] Database has been succesfully updated!%s" % (fg(218), attr(0)))

    def exec(self, args):
        """Execute system commands"""
        try:
            subprocess.run(args)
        except:
            print("\n%s[*] Could not execute command: %s" % (fg(9), attr(0)), *args)
    
    def exit(self):
        """Exit program"""
        print("%s[*] Exiting Program...%s" % (fg(9), attr(0)))
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def get_help(self):
        """Print help message"""
        print(
        """
        Command  Arguments             Description
        ------   ---------             -----------
        help                          : display this help message
        showcve                       : show all CVE id's
        showall                       : show CVE id's and descriptions
        search   [string]             : search CVE database for specific string
        year     >|<|=|>=|<= [year]   : get CVE's for a particular year or range of years
        update                        : update the cve database (will take a couple of seconds)
        exec     [command]            : execute system command
        exit                          : exit the program
        cls                           : clear screen
        """
        )

def main():
    obj = CveLookup()
    obj.initiate()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n%s[*] Exiting Program...%s" % (fg(9), attr(0)))
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
