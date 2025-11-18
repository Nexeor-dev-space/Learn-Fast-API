"""merge heads

Revision ID: 9b88039b4e98
Revises: 7e7ae80fbf3c, fb87f0c5bde5
Create Date: 2025-11-18 13:01:43.728937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b88039b4e98'
down_revision: Union[str, Sequence[str], None] = ('7e7ae80fbf3c', 'fb87f0c5bde5')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
