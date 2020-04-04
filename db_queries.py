import sqlite3
import json


def query_read_db(db="CV_Editor.db", table="basic_table"):

    query_file = "select_all.sql"

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # stackoverflow: This enables column access by name: row['column_name']
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query)

    json_str = [dict(row) for row in c.fetchall()]

    conn.close()

    return json.dumps(json_str)


def query_read_one_from_db(id=None, db="CV_Editor.db", table="basic_table"):

    query_file = "select_one.sql"

    params = {"id": id}
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # stackoverflow: This enables column access by name: row['column_name']
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    json_str = [dict(row) for row in c.fetchall()]  # TODO to jest result i to powinienem zwrócić jako obiekt a dopiero w main.py zamienić to na json

    conn.close()

    return json.dumps(json_str)  # TODO ta cala funkcja jest do przerobienia, to byla kopia read all


def query_insert_db(params, db="CV_Editor.db", table="basic_table"):

    query_file = "insert_cv.sql"

    conn = sqlite3.connect(db)
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    conn.commit()
    conn.close()

    # return f"query {query} with params {params} inserted"
    return


def query_update_db(id, cv_params, db="CV_Editor.db", table="basic_table"):

    query_file="update_cv.sql"

    params = {
            'id': id,
            'firstname': cv_params["firstname"],
            'lastname': cv_params["lastname"],
            'python': cv_params["python"],
            'javascript': cv_params["javascript"],
            'sql': cv_params["sql"],
            'english': cv_params["english"],
             }

    # print(params)  # TODO jak zrobić aby nadpisywać tylko uzupełnione wartości, a puste pomijać?

    conn = sqlite3.connect(db)
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    conn.commit()
    conn.close()

    return f"query {query} with params {params} updated"
    # return


def query_remove_from_db(id=None, db="CV_Editor.db", table="basic_table"):

    query_file = "delete_one.sql"

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
    # pass
    # print(query_read_db("select_all.sql"))
    # print(query_read_one_from_db("select_one.sql", 7))
    # query_insert_db("insert_cv.sql", {'firstname': 'Dummy', 'lastname': 'Dummer', 'python': 2, 'javascript': 0, 'sql': 1,
    #                           'english': 666})
    # print(query_remove_from_db("delete_one.sql", 5))
    dummy_cv_params = {'firstname': 'Błażej', 'lastname': 'Od roweru', 'python': 7, 'javascript': 0, 'sql': 1,
                              'english': 20}
    query_update_db(9, dummy_cv_params)
