#!/usr/bin/env python3

'''
CVE-csv file location: https://cve.mitre.org/data/downloads/index.html
Objectives:
    - perform cve, keyword lookup's on cve database
    - search cve based on year
    - update db
'''

try:
    from cvelookup.db.dbutils import Dbutils
    from cvelookup.db.db_lookup import Database
    from colored import fg, attr
    import sqlite3
    import subprocess
    import sys
    import os
except ImportError as err:
    print(err)

class CveLookup:
    def __init__(self):
        """
        """
        #self.utilobj = Dbutils()
        self.command_dict = {
            'help': self.get_help
           #'showcve': showcve,
           #'showall': showall,
           #'search': search,
           #'year': year,
           #'update': update,
           #'exit': exit,
           #'cls': clear
        }

    def prompt(self):
        """Displays prompt and handles all commands"""
        while True:
            user_input = input(("%scvelookup%s" % (fg(99), attr(0))) + " > ").strip()
            if user_input in self.command_dict.keys():
                self.command_dict[user_input]()

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
        help     None                 : display this help message
        showcve  None                 : show all CVE id's
        showall  None                 : show CVE id's and descriptions
        search   [string]             : search CVE database for specific string
        year     (>|<|=|>=|<=) [year] : get CVE's for a particular year or range of years
        update   None                 : update the cve database (will take a couple of seconds)
        exit     None                 : exit the program
        cls      None                 : clear screen
        """
        )

def main():
    obj = CveLookup()
    obj.prompt()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n%sExiting Program...%s" % (fg(9), attr(0))
        sys.exit()
