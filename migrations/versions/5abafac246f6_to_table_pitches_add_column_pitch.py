"""To table pitches, add column pitch

Revision ID: 5abafac246f6
Revises: c231d7b9bc87
Create Date: 2021-04-26 11:50:30.011740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5abafac246f6'
down_revision = 'c231d7b9bc87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###
