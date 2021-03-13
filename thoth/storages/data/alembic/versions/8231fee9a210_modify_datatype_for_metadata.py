"""Modify datatype for metadata

Revision ID: 8231fee9a210
Revises: 3dce903da79a
Create Date: 2019-11-25 10:32:29.831130+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8231fee9a210"
down_revision = "3dce903da79a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("python_package_metadata", "author", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "author_email", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "download_url", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "home_page", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "keywords", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "license", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "maintainer", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "maintainer_email", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "metadata_version", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "name", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "summary", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "version", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "requires_python", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "description", type_=sa.Text, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "description_content_type", type_=sa.Text, existing_type=sa.VARCHAR)

    op.alter_column("python_package_metadata_classifier", "classifier", type_=sa.Text, existing_type=sa.VARCHAR)

    op.alter_column("python_package_metadata_platform", "platform", type_=sa.Text, existing_type=sa.VARCHAR)

    op.alter_column(
        "python_package_metadata_supported_platform", "supported_platform", type_=sa.Text, existing_type=sa.VARCHAR
    )

    op.alter_column("python_package_metadata_requires_external", "dependency", type_=sa.Text, existing_type=sa.VARCHAR)

    op.alter_column("python_package_metadata_project_url", "project_url", type_=sa.Text, existing_type=sa.VARCHAR)

    op.alter_column(
        "python_package_metadata_provides_extra", "optional_feature", type_=sa.Text, existing_type=sa.VARCHAR
    )

    op.alter_column("python_package_metadata_distutils", "distutils", type_=sa.Text, existing_type=sa.VARCHAR)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("python_package_metadata", "author", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "author_email", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "download_url", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "home_page", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "keywords", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "license", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "maintainer", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "maintainer_email", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "metadata_version", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "name", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "summary", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "version", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "requires_python", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "description", type_=sa.String, existing_type=sa.VARCHAR)
    op.alter_column("python_package_metadata", "description_content_type", type_=sa.String, existing_type=sa.VARCHAR)

    op.alter_column("python_package_metadata_classifier", "classifier", type_=sa.String, existing_type=sa.VARCHAR)

    op.alter_column("python_package_metadata_platform", "platform", type_=sa.String, existing_type=sa.VARCHAR)

    op.alter_column(
        "python_package_metadata_supported_platform", "supported_platform", type_=sa.String, existing_type=sa.VARCHAR
    )

    op.alter_column(
        "python_package_metadata_requires_external", "dependency", type_=sa.String, existing_type=sa.VARCHAR
    )

    op.alter_column("python_package_metadata_project_url", "project_url", type_=sa.String, existing_type=sa.VARCHAR)

    op.alter_column(
        "python_package_metadata_provides_extra", "optional_feature", type_=sa.String, existing_type=sa.VARCHAR
    )

    op.alter_column("python_package_metadata_distutils", "distutils", type_=sa.String, existing_type=sa.VARCHAR)
    # ### end Alembic commands ###
