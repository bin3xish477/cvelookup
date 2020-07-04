#!/usr/bin/env python3

try:
    from cvelookup.db.dbutils import Dbutils
    from cvelookup.db.db_lookup import Database
    from colored import fg, attr
    import subprocess
    import sys
    import os
    if os.name != 'nt':
        import readline
except ImportError as err:
    print(err)

class CveLookup:
    def __init__(self):
        """Creates a `Dbutils` objects and a dictionary
        containing all valid commands and there corresponding
        functions.
        """
        self.utilobj = Dbutils()
        self.command_dict = {
            'help': self.get_help,
           #'showcve': self.showcve,
           #'showall': self.showall,
           #'search': self.search,
           #'year': self.year,
           'update': self.update,
           'exec': self.exec,
           'exit': self.exit,
           'cls': self.clear
        }

    def initiate(self):
        """Displays prompt and handles all commands"""
        while True:
            user_input = input(("%scvelookup%s" % (fg(99), attr(0))) + " > ").strip().split()
            if user_input[0] in self.command_dict.keys():
                self.command_dict[user_input[0]](*user_input[1:])
            else:
                print("%s[!] Invalid command%s" % (fg(9), attr(0)))

    def update(self):
        """Calls `updatedb` from `dbutils.py` to update the CVE database"""
        print("\n[+] --------------------------- %sUpdating database%s ---------------------------" % (fg(49), attr(0)))
        self.utilobj.updatedb()
        print("%s[*] Database has been succesfully updated!%s" % (fg(218), attr(0)))

    def exec(self, *args):
        """Execute system commands"""
        try:
            subprocess.run([*args])
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
        year     (>|<|=|>=|<=) [year] : get CVE's for a particular year or range of years
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
