"""Delete Position

Revision ID: c5339ffb1dd5
Revises: 35cb6f1fbb28
Create Date: 2020-05-25 14:05:54.017677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5339ffb1dd5'
down_revision = '35cb6f1fbb28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_index('ix_message_timestamp', table_name='message')
    op.drop_table('message')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=200), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('userID', sa.INTEGER(), nullable=True),
    sa.Column('candidateID', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['candidateID'], ['candidate.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_message_timestamp', 'message', ['timestamp'], unique=False)
    op.drop_table('group')
    # ### end Alembic commands ###
