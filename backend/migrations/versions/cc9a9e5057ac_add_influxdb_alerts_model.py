"""Add Influxdb Alerts Model.

Revision ID: cc9a9e5057ac
Revises: 16a3bb6544b1
Create Date: 2023-07-13 19:52:44.366350

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "cc9a9e5057ac"
down_revision = "16a3bb6544b1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "influx_db_alerts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("check_name", sa.String(length=1000), nullable=True),
        sa.Column("message", sa.String(length=1000), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("influx_db_alerts")
    # ### end Alembic commands ###
