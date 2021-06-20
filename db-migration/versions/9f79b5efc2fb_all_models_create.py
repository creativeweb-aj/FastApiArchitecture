"""all models create

Revision ID: 9f79b5efc2fb
Revises: 
Create Date: 2021-06-20 10:53:55.934718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f79b5efc2fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.Column('created_on', sa.String(length=100), nullable=True),
    sa.Column('updated_on', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_verify', sa.Boolean(), nullable=False),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.Column('created_on', sa.String(length=100), nullable=True),
    sa.Column('updated_on', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('detail', sa.String(length=100), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.Column('created_on', sa.String(length=100), nullable=True),
    sa.Column('updated_on', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('users')
    op.drop_table('category')
    # ### end Alembic commands ###