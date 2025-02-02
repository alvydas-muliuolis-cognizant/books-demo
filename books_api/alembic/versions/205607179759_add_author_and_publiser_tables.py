"""add author and publiser tables

Revision ID: 205607179759
Revises: 207c0596251b
Create Date: 2025-01-30 17:58:43.396310

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "205607179759"
down_revision: Union[str, None] = "207c0596251b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "author",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "publisher",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "book_author",
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
        ),
        sa.ForeignKeyConstraint(
            ["book_id"],
            ["book.id"],
        ),
        sa.PrimaryKeyConstraint("book_id", "author_id"),
    )
    op.add_column("book", sa.Column("isbn13", sa.String(length=13), nullable=False))
    op.add_column("book", sa.Column("pages", sa.Integer(), nullable=False))
    op.add_column("book", sa.Column("overview", sa.String(length=1000), nullable=False))
    op.add_column("book", sa.Column("publisher_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "book", "publisher", ["publisher_id"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "book", type_="foreignkey")
    op.drop_column("book", "publisher_id")
    op.drop_column("book", "overview")
    op.drop_column("book", "pages")
    op.drop_column("book", "isbn13")
    op.drop_table("book_author")
    op.drop_table("publisher")
    op.drop_table("author")
    # ### end Alembic commands ###
