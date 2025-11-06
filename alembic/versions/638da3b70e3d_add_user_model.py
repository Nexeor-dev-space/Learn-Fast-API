"""Add user model

Revision ID: 638da3b70e3d
Revises: 2406a6d9bf01
Create Date: 2025-11-06 20:40:47.638122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '638da3b70e3d'
down_revision: Union[str, Sequence[str], None] = '2406a6d9bf01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
