"""create phone number for user table

Revision ID: 8ebb4fb07f1c
Revises: 
Create Date: 2024-02-26 16:01:55.658904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ebb4fb07f1c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = inspector.get_columns('courses')
    column_names = [column['name'] for column in columns]

    if 'price' not in column_names:
        op.add_column("courses", sa.Column('price', sa.Float, nullable=True))


def downgrade() -> None:
    op.drop_column('courses', 'price')