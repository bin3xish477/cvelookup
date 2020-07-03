#!/usr/bin/env python3

'''
CVE-csv file location: https://cve.mitre.org/data/downloads/index.html
Objectives:
    - perform cve, keyword lookup's on cve database
    - search cve based on year
    - update db
'''

try:
    from cvelookup.db.functions import *
    from cvelookup.db.db_lookup import Database
    from cvelookup.src.colors import Color as col
    import sqlite3
    import subprocess
    import sys
    import os
    import readline
except ImportError as err:
    print(err)

def get_help():
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
    exit     None                 : exit the program
    cls      None                 : clear screen
    """
    )

class CveLookup:
    def get_help():
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
        exit     None                 : exit the program
        cls      None                 : clear screen
        """
        )
    
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    command_dict = {
        'help': get_help,
        'showcve': showcve,
        'showall': showall,
        'search': search,
        'year': year,
        'exit': exit,
        'cls': clear
    }

    def prompt(self):
        """Displays prompt and handles all commands"""
        while 1:
            user_input = input(col.m+"cvelookup"+col.re+"> ").strip()
            if user_input in self.command_dict.keys():
                self.command_dict[user_input]()

def main():
    obj = CveLookup()
    obj.prompt()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(col.r+"\nExiting Program..." + col.re)
        sys.exit()
