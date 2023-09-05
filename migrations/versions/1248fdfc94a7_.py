"""empty message

Revision ID: 1248fdfc94a7
Revises: 3637acac412a
Create Date: 2023-08-07 16:30:14.143748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1248fdfc94a7'
down_revision = '3637acac412a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('child',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('dose', sa.String(length=200), nullable=True),
    sa.Column('frequency', sa.Integer(), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['child.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medication')
    op.drop_table('child')
    # ### end Alembic commands ###