"""merge heads

Revision ID: a79abef1c43c
Revises: 9b88039b4e98
Create Date: 2025-11-18 13:01:56.352616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a79abef1c43c'
down_revision: Union[str, Sequence[str], None] = '9b88039b4e98'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
