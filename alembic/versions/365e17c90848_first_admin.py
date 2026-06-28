"""First admin

Revision ID: 365e17c90848
Revises: 6fbd274a2f37
Create Date: 2026-06-27 21:15:44.029842

"""
import datetime
from typing import Sequence, Union
from zoneinfo import ZoneInfo
from Auth.security.hashHelper import HashHelper
import os 
from dotenv import load_dotenv

from alembic import op
import sqlalchemy as sa

load_dotenv()

# revision identifiers, used by Alembic.
revision: str = '365e17c90848'
down_revision: Union[str, Sequence[str], None] = '6fbd274a2f37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    hashed_password = HashHelper.get_password_hash(os.getenv("ADMIN_PW"))
    op.get_bind().execute(
        sa.text("""
            INSERT INTO users(id, username, password, role, created_at, disabled) 
            SELECT gen_random_uuid(), :username , :password,
                (SELECT id FROM user_roles WHERE role='admin'),
                :created_at, false
            WHERE NOT EXISTS (SELECT 1 FROM users WHERE username = :username)
        """),
        {"username" : "UnmuktAdmin" , "password": hashed_password ,"created_at" : datetime.datetime.now(ZoneInfo("Asia/Kolkata")) }
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
