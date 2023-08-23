"""add_default_elo_rating_in_lesson

Revision ID: 4a18edf22b41
Revises: 5c6c8cba6173
Create Date: 2018-05-13 18:43:35.743090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a18edf22b41'
down_revision = '5c6c8cba6173'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE LESSON ADD COLUMN DEFAULT_ELO_RATING FLOAT')


def downgrade():
    pass
