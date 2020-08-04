# create or re-create db using this script

import sqlite3

conn = sqlite3.connect('../app/CV_Editor.db')
c = conn.cursor()

query_basic_table = """
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

query_login_table = """
DROP TABLE IF EXISTS "login_table";
CREATE TABLE "login_table" (
    "id"       INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL);
INSERT INTO "login_table"
VALUES (NULL, 'admin', 'pbkdf2:sha256:150000$n23PJTaW$50d6b61dde7f70d616679064b8857d037ded291d71979408889f08b813f7f6e3'
);
"""

# c.executescript(query_basic_table)
c.executescript(query_login_table)

conn.commit()
conn.close()
