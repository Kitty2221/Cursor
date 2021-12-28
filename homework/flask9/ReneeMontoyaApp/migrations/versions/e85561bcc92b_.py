"""empty message

Revision ID: e85561bcc92b
Revises: 
Create Date: 2021-11-16 14:02:19.985009

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e85561bcc92b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salons')
    op.add_column('plants', sa.Column('director_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'plants', 'employees', ['director_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'plants', type_='foreignkey')
    op.drop_column('plants', 'director_id')
    op.create_table('salons',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('city', mysql.VARCHAR(length=140), nullable=False),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
