"""link login_table and basic_table - step2

Revision ID: 7ee68741df55
Revises: 906d64bdc953
Create Date: 2020-08-06 18:06:22.116905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ee68741df55'
down_revision = '906d64bdc953'
branch_labels = None
depends_on = None


def upgrade():
    query = """
    INSERT INTO "basic_table_to_login_table"
    VALUES (NULL, 1, 1);
        """

    op.execute(query)


def downgrade():
    query = """
    DELETE FROM "basic_table_to_login_table" WHERE "id_basic_table" = 1;
        """

    op.execute(query)
