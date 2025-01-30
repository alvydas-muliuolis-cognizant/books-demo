"""update length of title column in book table

Revision ID: 207c0596251b
Revises: 0a83a37adb49
Create Date: 2025-01-30 17:32:19.882772

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "207c0596251b"
down_revision: Union[str, None] = "0a83a37adb49"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "book",
        "title",
        existing_type=sa.String(),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "book",
        "title",
        existing_type=sa.VARCHAR(length=100),
        type_=sa.String(),
        existing_nullable=False,
    )
