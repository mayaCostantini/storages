"""Added new table to link adviser run and python package version entity

Revision ID: 74254b596f00
Revises: ed56455efd82
Create Date: 2020-03-20 15:31:37.608247+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74254b596f00"
down_revision = "ed56455efd82"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "has_unresolved",
        sa.Column("adviser_run_id", sa.Integer(), nullable=False),
        sa.Column("python_package_version_entity_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["adviser_run_id"], ["adviser_run.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["python_package_version_entity_id"], ["python_package_version_entity.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("adviser_run_id", "python_package_version_entity_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("has_unresolved")
    # ### end Alembic commands ###
