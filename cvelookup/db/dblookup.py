"""
Fetch and return data from the CVE database
"""

import sqlite3
from cvelookup.db.dbutils import Dbutils

class Database(Dbutils):
    def __init__(self):
        self.conn = establish_connection()

    def search_year(self, *args):
        """Fetches cve's from a particular year or a range of years"""
        cursor = self.conn.cursor()
        sqlqry = '''

        '''

    def showcve(self):
        """Retrieve all CVE id's from CVE database"""
        sqlqry = '''

        '''

    def showall(self):
        """Retrieves both CVE id's and corresponding descriptions from CVE database"""
        sqlqry = '''

        '''

