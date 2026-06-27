"""seed user roles

Revision ID: 6fbd274a2f37
Revises: 1acc9f20cdcf
Create Date: 2026-06-27 16:16:51.571304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fbd274a2f37'
down_revision: Union[str, Sequence[str], None] = '1acc9f20cdcf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(sa.text("""
        INSERT INTO user_roles(id,role) VALUES
            (gen_random_uuid() , 'admin'),
            (gen_random_uuid() , 'engineer'),
            (gen_random_uuid() , 'customer')
        ON CONFLICT (role) DO NOTHING
    """))


def downgrade() -> None:
    """Downgrade schema."""
    pass
