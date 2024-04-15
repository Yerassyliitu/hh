"""feat: ResumeOffer

Revision ID: 42c1024d0d23
Revises: 8642a894bbfc
Create Date: 2024-04-14 22:31:54.373667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42c1024d0d23'
down_revision: Union[str, None] = '8642a894bbfc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ResumeOffer',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('resume_id', sa.BigInteger(), nullable=True),
    sa.Column('offer_id', sa.BigInteger(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['offer_id'], ['Offer.id'], ),
    sa.ForeignKeyConstraint(['resume_id'], ['Resume.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ResumeOffer')
    # ### end Alembic commands ###
