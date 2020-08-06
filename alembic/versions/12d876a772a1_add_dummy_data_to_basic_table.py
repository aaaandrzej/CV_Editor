"""add dummy data to basic_table

Revision ID: 12d876a772a1
Revises: bcb8dbd28cbb
Create Date: 2020-08-06 15:24:51.976100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12d876a772a1'
down_revision = 'bcb8dbd28cbb'
branch_labels = None
depends_on = None


def upgrade():
    query = """
    INSERT INTO basic_table VALUES(1,'Pan','Admin',0,0,0,0), 
                                  (9,'Błażej','Od roweru',7,0,1,20),
                                  (10,'Dummy','Dummer',2,0,1,6666666),
                                  (12,'King','Schultz',7,1,2,500),
                                  (13,'Dummmmy','Dummmer',7,5,4,3),
                                  (14,'King','Schultz II',7,1,2,500),
                                  (15,'Placek','Placcekk',0,0,0,0),
                                  (16,'Jacek','Placek',6,3,0,1),
                                  (17,'Dssdf','fdsfs',0,0,0,0),
                                  (18,'Antoni','Tak',0,0,0,1),
                                  (994,'Aaaantoni','Tak',0,0,0,0),
                                  (995,'Tik','Tak',0,0,0,0),
                                  (996,'Tik','Tak2',0,0,0,0),
                                  (997,'Tik','Tok',9,9,9,9),
                                  (999,'Tik2','Tak2',0,0,0,0),
                                  (1000,'Tik22','Tak2',0,0,0,0),
                                  (1001,'DSDFsdsd','sdad',8,8,8,8),
                                  (1002,'Dummy','Dummer',2,0,1,666),
                                  (1003,'d','e',2,'','',''),
                                  (1004,'Jababi','Du',6,5,4,3),
                                  (1005,'Nie','Nie','','','',''),
                                  (1006,'Tak','Tik','','','',''),
                                  (1007,'Juz','Nie chce',5,5,5,5),
                                  (1008,'Nadal','nie chce nie nie',1,1,1,1),
                                  (1009,'Ostatnie','CV',1,1,1,1),
                                  (1010,'Tik666','Tak666',0,0,0,77232387),
                                  (1011,'fsfsdf','fssdff',2,22,2,2),
                                  (1012,'no','debil',0,0,0,0),
                                  (1013,'Didi','Dada',2,0,1,1),
                                  (1014,'DFdfsdf','dsdfsdf',8,8,8,8),
                                  (1015,'ddsdsdsssss','ww',1,1,1,1),
                                  (1016,'Aleksander','Gruszczynski',8,8,8,10),
                                  (1017,'test2134','12',7,7,76,12),
                                  (1018,'xxx','xxx',2,0,1,1),
                                  (1019,'test11','test',8,5,43,3),
                                  (1020,'tessststststsst','testesest00',88,55,44,33),
                                  (1021,'xxx','xxx',2,0,1,1),
                                  (1023,'xx','xx',2,0,1,1);
"""

    op.execute(query)


def downgrade():
    query = """
        DELETE FROM "basic_table" WHERE "id" = 1 OR
                                        "id" = 9 OR
                                        "id" = 10 OR
                                        "id" = 12 OR
                                        "id" = 13 OR
                                        "id" = 14 OR
                                        "id" = 15 OR
                                        "id" = 16 OR
                                        "id" = 17 OR
                                        "id" = 18 OR
                                        "id" = 994 OR
                                        "id" = 995 OR
                                        "id" = 996 OR
                                        "id" = 997 OR
                                        "id" = 999 OR
                                        "id" = 1000 OR
                                        "id" = 1001 OR
                                        "id" = 1002 OR
                                        "id" = 1003 OR
                                        "id" = 1004 OR
                                        "id" = 1005 OR
                                        "id" = 1006 OR
                                        "id" = 1007 OR
                                        "id" = 1008 OR
                                        "id" = 1009 OR
                                        "id" = 1010 OR
                                        "id" = 1011 OR
                                        "id" = 1012 OR
                                        "id" = 1013 OR
                                        "id" = 1014 OR
                                        "id" = 1015 OR
                                        "id" = 1016 OR
                                        "id" = 1017 OR
                                        "id" = 1018 OR
                                        "id" = 1019 OR
                                        "id" = 1020 OR
                                        "id" = 1021 OR
                                        "id" = 1023;
    """

    op.execute(query)
