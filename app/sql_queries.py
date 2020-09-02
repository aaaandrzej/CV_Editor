SQL_STATS = '''
    SELECT u.firstname, u.lastname
    FROM (
        SELECT q.user_id, COUNT(*) as count
        FROM (
            SELECT su.user_id, s.skill_name, su.skill_level
            FROM skill_user su
            JOIN skill s on su.skill_id = s.id
            WHERE (s.skill_name, su.skill_level) IN ({subs})
            ) q
            GROUP BY q.user_id
        ) r
    JOIN user u ON r.user_id = u.id
    WHERE r.count = :count'''


SQL_COUNT = '''
    SELECT COUNT(r.user_id)
    FROM (
        SELECT q.user_id, COUNT(*) as count
        FROM (
            SELECT su.user_id, s.skill_name, su.skill_level
            FROM skill_user su
            JOIN skill s on su.skill_id = s.id
            WHERE (s.skill_name, su.skill_level) IN ({subs})
        ) q
        GROUP BY q.user_id
    ) r
    WHERE r.count = :count
    '''
