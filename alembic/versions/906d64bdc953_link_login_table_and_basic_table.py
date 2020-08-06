"""link login_table and basic_table

Revision ID: 906d64bdc953
Revises: 12d876a772a1
Create Date: 2020-08-06 18:04:52.940312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '906d64bdc953'
down_revision = '12d876a772a1'
branch_labels = None
depends_on = None


def upgrade():
    query = """
    CREATE TABLE "basic_table_to_login_table"
(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id_basic_table" INTEGER,
    "id_login_table" INTEGER,
    FOREIGN KEY ("id_basic_table") REFERENCES "basic_table" ("id"),
    FOREIGN KEY ("id_login_table") REFERENCES "login_table" ("id")
);
    """

    op.execute(query)


def downgrade():
    query = """
        DROP TABLE "basic_table_to_login_table"
    """

    op.execute(query)
