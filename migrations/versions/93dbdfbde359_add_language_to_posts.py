"""add language to posts

Revision ID: 93dbdfbde359
Revises: 023fe4dac389
Create Date: 2023-04-21 18:33:49.335219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93dbdfbde359'
down_revision = '023fe4dac389'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
