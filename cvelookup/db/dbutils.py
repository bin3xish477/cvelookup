'''
Create database from csv file
'''

import sqlite3
import os
import requests

absolute = os.path.dirname(os.path.abspath(__file__))

class Dbutils:
    def establish_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(absolute+"/cve.db")
        except sqlite3.Error as err:
            print(err)
        return conn

    def createdb(self):
        """Creates the CVE database if one does not already exists"""
        conn = self.establish_connection()
        c = conn.cursor()
        create_table = '''CREATE TABLE CVE
        (
            line int,
            cve_id varchar(20),
            description varchar(5000)
        )
        '''
        try:
            c.execute(create_table)
            with open(absolute+"/allitems.csv", 'rb') as f:
                [next(f) for i in range(11)]
                for i, line in enumerate(f):
                    sqlqry = '''INSERT INTO CVE VALUES (?,?,?)'''
                    line = str(line)
                    line = line.split(',')
                    c.execute(sqlqry, (i, line[0][1:], line[2],))
            conn.commit()
            conn.close()
        except sqlite3.OperationalError:
            pass

    def updatedb(self):
        """Updates the database by removing the current one,
        downloading the newer of the csv containing the cve data,
        and creating a new CVE database with the newly fetched data.

        Data obtained from: https://cve.mitre.org/data/downloads/allitems.csv
        """
        allitems = requests.get("https://cve.mitre.org/data/downloads/allitems.csv")
        print(allitems.text[:50])
        # with open('allitems.csv', 'w') as f:
        #     f.write(allitems.text)
        # self.createdb()