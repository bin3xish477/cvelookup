'''
Create, update, and connect to database
'''

import sqlite3
import os
import requests
from colored import fg, attr
from time import sleep

absolute = os.path.dirname(os.path.abspath(__file__))

class Dbutils:
    def establish_connection(self):
        """Connects to the CVE database"""
        self.conn = None
        try:
            self.conn = sqlite3.connect(absolute+"/cve.db")
        except sqlite3.Error as err:
            print(err)

    def createdb(self):
        """Creates the CVE database if one does not already exists"""
        self.establish_connection()
        self.cursor = self.conn.cursor()
        create_table = '''CREATE TABLE CVE
        (
            line int,
            cve_id varchar(20),
            description varchar(5000)
        )
        '''
        try:
            self.cursor.execute(create_table)
            with open(absolute+"/allitems.csv", 'rb') as f:
                [next(f) for i in range(11)]
                print("%s[+] Extracting data from new csv and converting into database%s" % (fg(130), attr(0)))
                for i, line in enumerate(f):
                    sqlqry = '''INSERT INTO CVE VALUES (?,?,?)'''
                    line = str(line)
                    line = line.split(',')
                    self.cursor.execute(sqlqry, (i, line[0][2:], line[2],))
            self.conn.commit()
            self.conn.close()
            print("%s[+] Database created%s" % (fg(142), attr(0)))
        except sqlite3.OperationalError as err:
            print("\n%s[!] An error has occured: %s" % (fg(9), attr(0)), err)
            print("\n%s[*] Exiting Program...%s" % (fg(9), attr(0)))



    def updatedb(self):
        """Updates the database by removing the current one,
        downloading the newer of the csv containing the cve data,
        and creating a new CVE database with the newly fetched data.

        Data obtained from: https://cve.mitre.org/data/downloads/allitems.csv
        """
        print("%s[+] Obtaining csv file from https://cve.mitre.org/data/downloads/allitems.csv %s" % (fg(163), attr(0)))
        allitems = requests.get("https://cve.mitre.org/data/downloads/allitems.csv")
        
        self.deletedb()
        sleep(1)
        with open(absolute+'/allitems.csv', 'wb') as f:
            f.write(bytes(allitems.text, "utf-8"))
        self.createdb()

    def deletedb(self):
        """Removes both csv file and database file for re-downloading"""
        if os.path.exists(absolute+"/allitems.csv") or os.path.exists(absolute+"/cve.db"):
            print("%s[+] Deleting old database files:%s" % (fg(105), attr(0)))
            if os.path.exists(absolute+"/allitems.csv"):
                print("\t- allitems.csv")
                os.remove(absolute+"/allitems.csv")

            if os.path.exists(absolute+"/cve.db"):
                print("\t- cve.db")
                os.remove(absolute+"/cve.db")
        else: print("%s[+] No database files to delete%s" % (fg(105), attr(0)))

    def exists(self):
        """Check if the database exists. Will be utilized at installation because
        database file will not have been created until running the `update` command.
        """
        if not os.path.exists(absolute+"/cve.db"):
            print("%s[!] Must run `update` command to fetch and create database%s" % (fg(11), attr(0)))
            pass