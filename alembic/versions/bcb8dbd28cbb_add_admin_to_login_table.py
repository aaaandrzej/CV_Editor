"""add admin to login_table

Revision ID: bcb8dbd28cbb
Revises: 0151e5487080
Create Date: 2020-08-06 14:10:45.138106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcb8dbd28cbb'
down_revision = '0151e5487080'
branch_labels = None
depends_on = None


def upgrade():
    query = """
    INSERT INTO "login_table"
    VALUES (NULL, 'admin', 'pbkdf2:sha256:150000$n23PJTaW$50d6b61dde7f70d616679064b8857d037ded291d71979408889f08b813f7f6e3'
    );
    """

    op.execute(query)


def downgrade():
    query = """
        DELETE FROM main."login_table" WHERE "username" = "admin"
        """

    op.execute(query)