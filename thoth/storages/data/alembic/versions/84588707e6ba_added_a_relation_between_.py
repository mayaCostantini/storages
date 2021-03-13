"""Added a relation between PythonPackageVersion and SIAggregated

Revision ID: 84588707e6ba
Revises: 83e2900c3721
Create Date: 2020-08-26 18:55:20.736024+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "84588707e6ba"
down_revision = "83e2900c3721"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("si_aggregated", sa.Column("python_package_version_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        None, "si_aggregated", "python_package_version", ["python_package_version_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "si_aggregated", type_="foreignkey")
    op.drop_column("si_aggregated", "python_package_version_id")
    # ### end Alembic commands ###
