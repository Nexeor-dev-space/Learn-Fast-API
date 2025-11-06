"""Add user model

Revision ID: 2406a6d9bf01
Revises: c8aecc428917
Create Date: 2025-11-06 20:40:41.874821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2406a6d9bf01'
down_revision: Union[str, Sequence[str], None] = 'c8aecc428917'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
