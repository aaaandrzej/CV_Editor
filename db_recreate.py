# create or re-create db using this script

import sqlite3

conn = sqlite3.connect('CV_Editor.db')
c = conn.cursor()

query = """
DROP TABLE IF EXISTS "basic_table";

CREATE TABLE "basic_table" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "firstname"	TEXT NOT NULL,
    "lastname"	TEXT NOT NULL,
    "python"	INTEGER DEFAULT 0,
    "javascript"	INTEGER DEFAULT 0,
    "sql"	INTEGER DEFAULT 0,
    "english"	INTEGER DEFAULT 0
);
"""

c.executescript(query)

conn.commit()
conn.close()
