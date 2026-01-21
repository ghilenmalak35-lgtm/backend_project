"""add audit fields to clients

Revision ID: 3f2a1c9b7e12
Revises: 1a2b3c4d5e6f
Create Date: 2026-01-21 09:10:00
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f2a1c9b7e12'
down_revision = '1a2b3c4d5e6f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'clients',
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('1'))
    )
    op.add_column(
        'clients',
        sa.Column('last_login', sa.DateTime(), nullable=True)
    )
    op.add_column(
        'clients',
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )
    op.add_column(
        'clients',
        sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now())
    )
    op.add_column(
        'clients',
        sa.Column('deleted_at', sa.DateTime(), nullable=True)
    )


def downgrade():
    op.drop_column('clients', 'deleted_at')
    op.drop_column('clients', 'updated_at')
    op.drop_column('clients', 'created_at')
    op.drop_column('clients', 'last_login')
    op.drop_column('clients', 'is_active')
