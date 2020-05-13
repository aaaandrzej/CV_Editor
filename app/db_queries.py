import sqlite3


def query_read_db(db="app/CV_Editor.db", table="basic_table"):  # TODO zrobić względne ścieżki zamiast tych

    query_file = "app/sql/select_all.sql"

    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # stackoverflow: This enables column access by name: row['column_name']
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query)

    db_list_of_dicts = [dict(row) for row in c.fetchall()]

    conn.close()

    return db_list_of_dicts


def query_read_one_from_db(id=None, db="app/CV_Editor.db", table="basic_table"):

    query_file = "app/sql/select_one.sql"

    params = {"id": id}
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row # stackoverflow: This enables column access by name: row['column_name']
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    result = dict(c.fetchone())

    conn.close()

    return result


def query_insert_db(params, db="app/CV_Editor.db", table="basic_table"):

    query_file = "app/sql/insert_cv.sql"

    conn = sqlite3.connect(db)
    c = conn.cursor()

    with open(query_file, encoding='utf-8') as file:
        query = file.read()

    c.execute(query, params)

    conn.commit()
    conn.close()

    # return f"query {query} with params {params} inserted"
    return


def query_update_db(id, cv_params, db="app/CV_Editor.db", table="basic_table"):

    query_file= "app/sql/update_cv.sql"

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


def query_remove_from_db(id=None, db="app/CV_Editor.db", table="basic_table"):

    query_file = "app/sql/delete_one.sql"

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
    # print(query_read_db())
    # print(query_read_one_from_db(999))
    # query_insert_db("insert_cv.sql", {'firstname': 'Dummy', 'lastname': 'Dummer', 'python': 2, 'javascript': 0, 'sql': 1, 'english': 666})
    # print(query_remove_from_db("delete_one.sql", 5))
    # dummy_cv_params = {'firstname': 'Błażej', 'lastname': 'Od roweru', 'python': 7, 'javascript': 0, 'sql': 1,
    #                           'english': 20}
    # query_update_db(9, dummy_cv_params)
