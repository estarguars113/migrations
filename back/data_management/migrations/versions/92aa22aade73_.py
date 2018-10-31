"""empty message

Revision ID: 92aa22aade73
Revises: 
Create Date: 2018-10-29 15:32:57.988271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92aa22aade73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('short_name', sa.String(length=3), nullable=True),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('migrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dest_country', sa.Integer(), nullable=True),
    sa.Column('source_country', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dest_country'], ['country.id'], ),
    sa.ForeignKeyConstraint(['source_country'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('migrations')
    op.drop_table('country')
    # ### end Alembic commands ###
