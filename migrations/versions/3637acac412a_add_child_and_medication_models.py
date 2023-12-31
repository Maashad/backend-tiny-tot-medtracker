"""add child and medication models

Revision ID: 3637acac412a
Revises: 
Create Date: 2023-08-07 16:21:35.425671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3637acac412a'
down_revision = None
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
