"""empty message

Revision ID: 56b79ff5faaa
Revises: 3c4f77133fbe
Create Date: 2022-04-09 16:45:08.636992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b79ff5faaa'
down_revision = '3c4f77133fbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('post_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'post_id')
    # ### end Alembic commands ###