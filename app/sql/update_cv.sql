UPDATE "basic_table"
SET 'firstname' = :firstname, 'lastname' = :lastname, 'python' = :python, 'javascript' = :javascript, 'sql' = :sql, 'english' = :english
WHERE "id" = :id;