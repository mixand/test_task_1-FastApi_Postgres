"""create table

Revision ID: c6bdf98a6f43
Revises: 
Create Date: 2023-05-21 00:44:47.801258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6bdf98a6f43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions_db',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_question', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('data_created', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_question')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions_db')
    # ### end Alembic commands ###