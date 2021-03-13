"""change flag to 'provides_source_distro'

Revision ID: b9f960cdd223
Revises: cd34fd8a5a90
Create Date: 2020-09-29 17:50:13.094530+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b9f960cdd223"
down_revision = "cd34fd8a5a90"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("python_package_version", "is_si_analyzable", new_column_name="provides_source_distro")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("python_package_version", "provides_source_distro", new_column_name="is_si_analyzable")
    # ### end Alembic commands ###
