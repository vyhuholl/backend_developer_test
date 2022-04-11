"""
Create database

Revision ID: 6a1405601356
Revises: 
Create Date: 2022-04-11 22:20:00.372234
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '6a1405601356'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('login', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'repository',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('stargazers', sa.Integer(), nullable=False),
        sa.Column('forks', sa.Integer(), nullable=False),
        sa.Column('watchers', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_repository_date'), 'repository', ['date'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_repository_date'), table_name='repository')
    op.drop_table('repository')
    op.drop_table('user')
