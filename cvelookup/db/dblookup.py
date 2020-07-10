"""
Fetch and return data from the CVE database
"""

import sqlite3
from cvelookup.db.dbutils import Dbutils
from colored import fg, attr
import re

class Database(Dbutils):
    def search(self, args):
        """Query the database for a particular string"""
        conn = super().establish_connection()
        cursor = conn.cursor()

        sqlqry = f'''
            SELECT cve_id, description
            FROM CVE
            WHERE cve_id LIKE '%{args[0]}%' OR description LIKE '%{args[0]}%';
        '''
        results = cursor.execute(sqlqry)

        search_str_len = len(args[0])
        for row in results:
            if args[0] in row[0]:
                search_start_pos = row[0].find(args[0])
                print(("%s"+row[0][:search_start_pos].ljust(14, " ")+"%s") % (fg(9),
                attr(0))+("%s"+row[0][search_start_pos:search_start_pos+search_str_len]+"%s") % (fg(49),
                attr(0))+row[0][search_start_pos+search_str_len:])
            else:
                print(("%s"+row[0].ljust(14, " ")+"%s") % (fg(9), attr(0)), end=" ")
            if args[0] in row[1]:
                search_start_pos = row[1].find(args[0])
                print("|", row[1][:search_start_pos],
                ("%s"+row[1][search_start_pos:search_start_pos+search_str_len]+"%s") % (fg(49),
                attr(0))+row[1][search_start_pos+search_str_len:])
            else:
                print(row[1])
        conn.close()
        
    def search_year(self, args):
        """Fetches cve's from a particular year or a range of years"""
        conn = super().establish_connection()
        cursor = conn.cursor()

        sqlqry = f'''
            SELECT cve_id, description
            FROM CVE
            WHERE CAST(SUBSTR(cve_id, 5, 4) AS INT) {args[0]} {args[1]};
        '''
        results = cursor.execute(sqlqry)

        for row in results:
            print(("%s"+row[0]+"%s") % (fg(9), attr(0)), "|", row[1][1:])
        conn.close()

    def show_all(self):
        """Retrieves both CVE id's and corresponding descriptions from CVE database"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        sqlqry = '''
            SELECT line, cve_id, description
            FROM CVE;
        '''
        results = cursor.execute(sqlqry)
        for row in results:
            print(("%s"+str(row[0])+"%s") % (fg(220), attr(0)), "|", ("%s"+row[1]+"%s") % (fg(196), attr(0)), "|", row[2][1:])
        conn.close()

