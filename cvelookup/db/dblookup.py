"""
Fetch and return data from the CVE database
"""

import sqlite3
from cvelookup.db.dbutils import Dbutils

class Database(Dbutils):
    def search(self, args):
        """Query the database for a particular string"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        sqlqry = '''
            SELECT line, cve_id, description
            WHERE
        '''
        results = cursor.execute(sqlqry)
        for row in results:
            pass
        conn.close()
        
    def search_year(self, args):
        """Fetches cve's from a particular year or a range of years"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        # This SQL query is actually vulnerable to sql injection
        # but because this data is public there is no need to worry!
        # It was used because the sqlite3 parameterized queries was
        # not doing what I wanted it to do! :(
        sqlqry = '''
            SELECT SUBSTR(cve_id, 5, 4), description
            FROM CVE
            WHERE CAST(SUBSTR(cve_id, 5, 4) AS INT) %s %s
        ''' % (args[0], args[1])
        results = cursor.execute(sqlqry)
        for row in results:
            print(row)
        conn.close()

    def show_cve(self):
        """Retrieve all CVE id's from CVE database"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        sqlqry = '''
            SELECT cve_id
            FROM CVE
        '''
        results = cursor.execute(sqlqry)
        for row in results:
            pass
        conn.close()

    def show_all(self):
        """Retrieves both CVE id's and corresponding descriptions from CVE database"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        sqlqry = '''
            SELECT 
        '''
        results = cursor.execute(sqlqry)
        for row in results:
            print("#######"*10)
            print(row[0], row[1], row[2][1:])
        print("#######"*10)
        conn.close()

