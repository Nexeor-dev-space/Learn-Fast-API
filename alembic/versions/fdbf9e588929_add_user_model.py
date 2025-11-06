"""Add user model

Revision ID: fdbf9e588929
Revises: 638da3b70e3d
Create Date: 2025-11-06 20:41:07.358529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdbf9e588929'
down_revision: Union[str, Sequence[str], None] = '638da3b70e3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
