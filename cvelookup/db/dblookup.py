"""
Fetch and return data from the CVE database
"""

import sqlite3
from cvelookup.db.dbutils import Dbutils
from colored import fg, attr

class Database(Dbutils):
    def search(self, args):
        """Query the database for a particular string"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        # This SQL query is vulnerable to sql injection
        # but because this data is public there is no need to worry!
        # It was used because the sqlite3 parameterized queries was
        # not doing what I wanted it to do! :(
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
                print(row[0][:search_start_pos].ljust(14, " "), ("%s"+row[0][search_start_pos:search_start_pos+search_str_len]+"%s") % (fg(9), attr(0))+
                    row[0][search_start_pos+search_str_len:])
            else:
                print(row[0].ljust(14, " "), end=" ")
            if args[0] in row[1]:
                search_start_pos = row[1].find(args[0])
                print("|", row[1][:search_start_pos]+("%s"+row[1][search_start_pos:search_start_pos+search_str_len]+"%s") % (fg(9), attr(0))+
                    row[1][search_start_pos+search_str_len:])
            else:
                print(row[1])
        conn.close()
        
    def search_year(self, args):
        """Fetches cve's from a particular year or a range of years"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        # This SQL query is vulnerable to sql injection
        # but because this data is public there is no need to worry!
        # It was used because the sqlite3 parameterized queries was
        # not doing what I wanted it to do! :(
        sqlqry = '''
            SELECT cve_id, description
            FROM CVE
            WHERE CAST(SUBSTR(cve_id, 5, 4) AS INT) %s %s;
        ''' % (args[0], args[1])
        results = cursor.execute(sqlqry)
        for row in results:
            print(("%s"+row[0]+"%s") % (fg(9), attr(0)), "|", row[1][1:])
        conn.close()

    def show_cve(self):
        """Retrieve all CVE id's from CVE database"""
        conn = super().establish_connection()
        cursor = conn.cursor()
        sqlqry = '''
            SELECT cve_id
            FROM CVE;
        '''
        results = cursor.execute(sqlqry)
        i = 0
        for row in results:
            current_year = row[0][3:7]
            if i % 15 == 0:
                print("\n")
            print(row[0], end=" ")
            i += 1
        print("\n")
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

# 22 - first the columns
