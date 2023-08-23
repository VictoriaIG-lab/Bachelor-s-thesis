"""add_completed_column_in_user_lesson_difficulty

Revision ID: 5c6c8cba6173
Revises: 
Create Date: 2018-05-13 16:09:12.199176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c6c8cba6173'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE user_lesson_difficulty ADD COLUMN COMPLETED BOOLEAN DEFAULT FALSE ')


def downgrade():
    pass
