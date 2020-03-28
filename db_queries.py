import sqlite3
import json


def query_read_db(query, db="CV_Editor.db", table="basic_table"):

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    c = conn.cursor()
    c.execute(query)

    json_str = [dict(row) for row in c.fetchall()]

    conn.close()

    return json.dumps(json_str)


def query_read_one_from_db(query, id=None, db="CV_Editor.db", table="basic_table"):

    params = {"id": id}
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    c = conn.cursor()
    c.execute(query, params)

    json_str = [dict(row) for row in c.fetchall()] # to jest kalka z query_read_db - pewnie do uproszczenia

    conn.close()

    return json.dumps(json_str)


def query_insert_db(query, params, db="CV_Editor.db", table="basic_table"):

    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(query, params)

    conn.commit()
    conn.close()

    return f"query {query} with params {params} inserted"
    # return


# queries
select_all = """
SELECT * FROM "basic_table";
"""

select_one = """
SELECT * FROM "basic_table" WHERE "id" = :id;
"""


# instert queries & params
insert_dummy_cv = """
INSERT INTO "basic_table" ('firstname', 'lastname', 'python', 'javascript', 'sql', 'english')
VALUES (:firstname, :lastname, :python, :javascript, :sql, :english);
"""

insert_dummy_cv_params = {'firstname': 'Dummy', 'lastname': 'Dummer', 'python': 2, 'javascript': 0, 'sql': 1, 'english': 0}


if __name__ == '__main__':
    # query_db(select_all)
    # print(query_read_db(select_all))
    print(query_read_one_from_db(select_one, 5))
    # query_insert_db(insert_dummy_cv, insert_dummy_cv_params)