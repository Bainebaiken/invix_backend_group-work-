"""upgrade

Revision ID: b2e5b8376b5b
Revises: cadd74eec521
Create Date: 2024-07-16 17:56:09.955133

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b2e5b8376b5b'
down_revision = 'cadd74eec521'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)
        batch_op.alter_column('text',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.alter_column('text',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###
