"""Adjust types for conv PI

Revision ID: 1fbd52a03c73
Revises: d0ebc816243c
Create Date: 2020-01-10 18:35:09.115584+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1fbd52a03c73"
down_revision = "d0ebc816243c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "pi_conv1d",
        "padding",
        existing_type=sa.VARCHAR(length=256),
        type_=sa.Integer(),
        existing_nullable=False,
        postgresql_using="padding::integer",
    )
    op.alter_column(
        "pi_conv2d",
        "padding",
        existing_type=sa.VARCHAR(length=256),
        type_=sa.Integer(),
        existing_nullable=False,
        postgresql_using="padding::integer",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "pi_conv2d", "padding", existing_type=sa.Integer(), type_=sa.VARCHAR(length=256), existing_nullable=False
    )
    op.alter_column(
        "pi_conv1d", "padding", existing_type=sa.Integer(), type_=sa.VARCHAR(length=256), existing_nullable=False
    )
    # ### end Alembic commands ###
