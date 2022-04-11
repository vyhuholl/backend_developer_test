import sqlalchemy as sa

metadata = sa.MetaData()

users = sa.Table(
    'user',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('login', sa.String, nullable=False),
    sa.Column('name', sa.String, nullable=False)
)

repositories = sa.Table(
    'repository',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    sa.Column('date', sa.Date, nullable=False, index=True),
    sa.Column('stargazers', sa.Integer, nullable=False),
    sa.Column('forks', sa.Integer, nullable=False),
    sa.Column('watchers', sa.Integer, nullable=False),
)
