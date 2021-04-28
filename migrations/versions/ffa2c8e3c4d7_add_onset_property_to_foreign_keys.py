"""Add onset property to foreign keys

Revision ID: ffa2c8e3c4d7
Revises: 4fa61d986eb3
Create Date: 2021-04-28 09:48:24.204607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa2c8e3c4d7'
down_revision = '4fa61d986eb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint('downvotes_pitch_id_fkey', 'downvotes', type_='foreignkey')
    op.drop_constraint('downvotes_user_id_fkey', 'downvotes', type_='foreignkey')
    op.create_foreign_key(None, 'downvotes', 'pitches', ['pitch_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'downvotes', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint('pitches_user_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint('upvotes_pitch_id_fkey', 'upvotes', type_='foreignkey')
    op.drop_constraint('upvotes_user_id_fkey', 'upvotes', type_='foreignkey')
    op.create_foreign_key(None, 'upvotes', 'pitches', ['pitch_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'upvotes', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.create_foreign_key('upvotes_user_id_fkey', 'upvotes', 'users', ['user_id'], ['id'])
    op.create_foreign_key('upvotes_pitch_id_fkey', 'upvotes', 'pitches', ['pitch_id'], ['id'])
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_user_id_fkey', 'pitches', 'users', ['user_id'], ['id'])
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.create_foreign_key('downvotes_user_id_fkey', 'downvotes', 'users', ['user_id'], ['id'])
    op.create_foreign_key('downvotes_pitch_id_fkey', 'downvotes', 'pitches', ['pitch_id'], ['id'])
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'pitches', ['pitch_id'], ['id'])
    op.alter_column('comments', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
