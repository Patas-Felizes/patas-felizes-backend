"""Removendo id_procedimento em despesa

Revision ID: b72d72797061
Revises: 77e8e1eacf24
Create Date: 2025-02-25 08:32:57.862161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b72d72797061'
down_revision = '77e8e1eacf24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tab_despesa', schema=None) as batch_op:
        batch_op.drop_column('procedimento_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tab_despesa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('procedimento_id', sa.INTEGER(), nullable=False))

    # ### end Alembic commands ###
