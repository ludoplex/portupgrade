import sqlite3

class PkgDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def query(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()

    def insert(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()

    def update(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()

    def delete(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()

if __name__ == "__main__":
    import sys
    db = PkgDB(sys.argv[1])
    # Call db methods based on command-line arguments
