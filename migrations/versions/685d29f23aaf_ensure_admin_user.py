"""ensure_admin_user

Revision ID: 685d29f23aaf
Revises: 1334a6d546c5
Create Date: 2023-10-11 18:14:20.447448

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel

from dundie.models.user import User
from sqlmodel import Session

# revision identifiers, used by Alembic.
revision = '685d29f23aaf'
down_revision = '1334a6d546c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    admin = User(
        name="Admin",
        username="admin",
        email="admin@mail.com",
        dept="management",
        password="admin",
        currency="USD",
    )

    try:
        session.add(admin)
        session.commit()
    except sa.exc.IntegrityError:
        session.rollback()


def downgrade() -> None:
    pass
