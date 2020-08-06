"""create login_table table

Revision ID: 0151e5487080
Revises: cd8f311a34e5
Create Date: 2020-08-06 14:06:35.892152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0151e5487080'
down_revision = 'cd8f311a34e5'
branch_labels = None
depends_on = None


def upgrade():
    query = """
    CREATE TABLE "login_table" (
        "id"       INTEGER PRIMARY KEY AUTOINCREMENT,
        "username" TEXT    NOT NULL,
        "password" TEXT    NOT NULL);
    """

    op.execute(query)


def downgrade():
    query = """
    DROP TABLE "login_table";
    """

    op.execute(query)
