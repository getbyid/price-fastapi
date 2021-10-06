"""init

Revision ID: acc8b8a37ccd
Revises: 
Create Date: 2021-10-06 08:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "acc8b8a37ccd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "offer",
        sa.Column("id", sa.INTEGER(), nullable=True),
        sa.Column("product_id", sa.INTEGER(), nullable=True),
        sa.Column("check_interval", sa.INTEGER(), nullable=True),
        sa.Column("url", sa.VARCHAR(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_offer_url", "offer", ["url"], unique=False)
    op.create_index("ix_offer_product_id", "offer", ["product_id"], unique=False)
    op.create_index("ix_offer_id", "offer", ["id"], unique=False)
    op.create_index(
        "ix_offer_check_interval", "offer", ["check_interval"], unique=False
    )
    op.create_table(
        "product",
        sa.Column("id", sa.INTEGER(), nullable=True),
        sa.Column("category", sa.VARCHAR(), nullable=False),
        sa.Column("name", sa.VARCHAR(), nullable=False),
        sa.Column("image", sa.VARCHAR(), nullable=True),
        sa.Column("description", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_product_name", "product", ["name"], unique=False)
    op.create_index("ix_product_image", "product", ["image"], unique=False)
    op.create_index("ix_product_id", "product", ["id"], unique=False)
    op.create_index("ix_product_description", "product", ["description"], unique=False)
    op.create_index("ix_product_category", "product", ["category"], unique=False)
    op.create_table(
        "history",
        sa.Column("id", sa.INTEGER(), nullable=True),
        sa.Column("offer_id", sa.INTEGER(), nullable=True),
        sa.Column("datetime", sa.INTEGER(), nullable=False),
        sa.Column("availability", sa.INTEGER(), nullable=False),
        sa.Column("price", sa.INTEGER(), nullable=False),
        sa.Column("price_currency", sa.VARCHAR(), nullable=False),
        sa.ForeignKeyConstraint(
            ["offer_id"],
            ["offer.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_history_price_currency", "history", ["price_currency"], unique=False
    )
    op.create_index("ix_history_price", "history", ["price"], unique=False)
    op.create_index("ix_history_offer_id", "history", ["offer_id"], unique=False)
    op.create_index("ix_history_id", "history", ["id"], unique=False)
    op.create_index("ix_history_datetime", "history", ["datetime"], unique=False)
    op.create_index(
        "ix_history_availability", "history", ["availability"], unique=False
    )


def downgrade():
    op.drop_index("ix_history_availability", table_name="history")
    op.drop_index("ix_history_datetime", table_name="history")
    op.drop_index("ix_history_id", table_name="history")
    op.drop_index("ix_history_offer_id", table_name="history")
    op.drop_index("ix_history_price", table_name="history")
    op.drop_index("ix_history_price_currency", table_name="history")
    op.drop_table("history")
    op.drop_index("ix_product_category", table_name="product")
    op.drop_index("ix_product_description", table_name="product")
    op.drop_index("ix_product_id", table_name="product")
    op.drop_index("ix_product_image", table_name="product")
    op.drop_index("ix_product_name", table_name="product")
    op.drop_table("product")
    op.drop_index("ix_offer_check_interval", table_name="offer")
    op.drop_index("ix_offer_id", table_name="offer")
    op.drop_index("ix_offer_product_id", table_name="offer")
    op.drop_index("ix_offer_url", table_name="offer")
    op.drop_table("offer")
