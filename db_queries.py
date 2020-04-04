import sqlite3
import json


def query_read_db(query_file, db="CV_Editor.db", table="basic_table"):

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query)

    json_str = [dict(row) for row in c.fetchall()]

    conn.close()

    return json.dumps(json_str)


def query_read_one_from_db(query_file, id=None, db="CV_Editor.db", table="basic_table"):

    params = {"id": id}
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    json_str = [dict(row) for row in c.fetchall()] # to jest kalka z query_read_db - pewnie do uproszczenia

    conn.close()

    return json.dumps(json_str)


def query_insert_db(query_file, params=None, db="CV_Editor.db", table="basic_table"):

    if params is None:
        params = insert_dummy_cv_params = {'firstname': 'Dummy', 'lastname': 'Dummer', 'python': 2, 'javascript': 0, 'sql': 1,
                              'english': 0}

    conn = sqlite3.connect(db)
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    conn.commit()
    conn.close()

    return f"query {query} with params {params} inserted"
    # return


def query_remove_from_db(query_file, id=None, db="CV_Editor.db", table="basic_table"):

    params = {"id": id}
    conn = sqlite3.connect(db)
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    conn.commit()
    conn.close()

    return f"record {id} deleted (if existed)"


if __name__ == '__main__':
    pass
    # print(query_read_db("select_all.sql"))
    # print(query_read_one_from_db("select_one.sql", 7))
    query_insert_db("insert_cv.sql", {'firstname': 'Dummy', 'lastname': 'Dummer', 'python': 2, 'javascript': 0, 'sql': 1,
                              'english': 666})
    # print(query_remove_from_db("delete_one.sql", 5))
