"""create admin

Revision ID: e73fbc74e0ef
Revises: 28174680d9ab
Create Date: 2020-11-06 15:23:35.353184

"""
import os

from alembic import op
import sqlalchemy as sa
from werkzeug.security import generate_password_hash

from app.models import User

# revision identifiers, used by Alembic.
revision = 'e73fbc74e0ef'
down_revision = '28174680d9ab'
branch_labels = None
depends_on = None

app_admin_user = User(username=os.environ['APP_USER'],
                      password=generate_password_hash(os.environ['APP_PASSWORD'], method='sha256', salt_length=8),
                      firstname=os.environ['APP_USER'][:2],
                      lastname=os.environ['APP_USER'][2:],
                      admin=True,
                      id=1)

user = sa.sql.table('user',
                    sa.sql.column('id', sa.Integer),
                    sa.sql.column('username', sa.String),
                    sa.sql.column('password', sa.String),
                    sa.sql.column('firstname', sa.String),
                    sa.sql.column('lastname', sa.String),
                    sa.sql.column('admin', sa.Boolean)
                    )


def upgrade():
    op.bulk_insert(user,
                   [{'id': app_admin_user.id,
                     'firstname': app_admin_user.firstname,
                     'lastname': app_admin_user.lastname,
                     'username': app_admin_user.username,
                     'password': app_admin_user.password,
                     'admin': True}]
                   )


def downgrade():
    query = '''
    DELETE FROM user WHERE username = 'admin';
    '''
    op.execute(query)

    # query = '''
    # DELETE FROM user WHERE username = ?;
    # '''
    # param = app_admin_user.username
    # op.execute(query, param)
