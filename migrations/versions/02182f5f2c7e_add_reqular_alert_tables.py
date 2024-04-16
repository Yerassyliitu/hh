"""add_reqular_alert_tables

Revision ID: 02182f5f2c7e
Revises: 6f664a0c526d
Create Date: 2024-04-16 18:39:32.919010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02182f5f2c7e'
down_revision: Union[str, None] = '6f664a0c526d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('RegularAlert',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('period', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('WorkerRegularAlert',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('WorkerRegularAlert')
    op.drop_table('RegularAlert')
    # ### end Alembic commands ###