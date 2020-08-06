"""create basic_table table

Revision ID: cd8f311a34e5
Revises: 
Create Date: 2020-08-06 12:55:01.312194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd8f311a34e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    query = """
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

    op.execute(query)


def downgrade():
    query = """
    DROP TABLE "basic_table";
    """

    op.execute(query)
