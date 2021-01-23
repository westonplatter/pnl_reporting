"""add trades.notes field

Revision ID: e9cb4d259d26
Revises: ef127d43de9e
Create Date: 2021-01-22 20:58:08.662996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e9cb4d259d26"
down_revision = "ef127d43de9e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("trades", sa.Column("notes", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("trades", "notes")
    # ### end Alembic commands ###
