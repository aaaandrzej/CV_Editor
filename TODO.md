10/04/2020

##### 1. put zamiast post do edycji cv
##### dodac baze do .gitignore

##### 2. layout/ uporzadkowanie plikow - sql do osobnego folderu, folder app - przy okazji sqlalchemy/ tutki flaskowe (flaskr)
##### przejsc na sql alchemy, zaorac db_queries

##### 3. alembic - migracje, db_recreate - flask_alembic do ogarnięcia

##### 4. potem rozbudowanie bazy o kolejne tabele

##### 5. skonczenie wymaganych funkcjonalnosci

##### 6. kiedyś potem autentykacja, za każdym razem jak ktoś uderza w endpoint mamy weryfikować czy on to może zrobić - uderzyć do bazy, sprawdzić ciastko, jeśli nie ma, to przekierować do loginu - a login sprawdza w bazie i ustawia ciastko - to jest ładnie opisane w tutorialu do flaska

##### + testy - pytest

<br><br>



27/03/2020

##### 1. update README.md

##### 2. stuby endpointów

hostname/cv 
- get - lista cv
- post - dorzucamy nowe cv

hostname/cv/1 - cv1
- get - pokaz cv1
- delete - usuwanie cv1
- put - modyfikuj cv1
- post - nadpisz cv1

##### 3. jedna tabela w bazie + metody do zapisania, odczytania - oddzielne skrypty

##### 4. połączenie baza <-> aplikacja - docelowo zwracanie jsona
- curl, postman

