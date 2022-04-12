from datetime import date
from typing import List

from sqlalchemy import and_, delete, insert, select
from sqlalchemy.future import Engine

from src.database import tables
from src.user.models import (
    UserAddRequestV1, UserResponseV1, StatsResponseV1
    )


class UserService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def get_all_users(self) -> List[UserResponseV1]:
        query = select(tables.users)
        with self._engine.connect() as connection:
            users_data = connection.execute(query)
        users = []
        for user_data in users_data:
            user = UserResponseV1(
                id=user_data['id'],
                login=user_data['login'],
                name=user_data['name']
            )
            users.append(user)
        return users

    def get_user_by_id(self, id: int) -> UserResponseV1:
        query = select(tables.users).where(tables.users.c.id == id)
        with self._engine.connect() as connection:
            user_data = connection.execute(query)
        user = UserResponseV1(
            id=user_data['id'],
            login=user_data['login'],
            name=user_data['name']
        )
        return user

    def get_stats_by_user(self, id: int) -> List[StatsResponseV1]:
        query = select(tables.stats).where(
            tables.stats.c.user_id == id
            ).order_by(tables.stats.c.repo_id, tables.stats.c.date)
        with self._engine.connect() as connection:
            stats_data = connection.execute(query)
        stats = []
        for data in stats_data:
            stat = StatsResponseV1(
                user_id=data['user_id'],
                repo_id=data['repo_id'],
                date=data['date'],
                stargazers=data['stargazers'],
                forks=data['forks'],
                watchers=data['watchers'],
            )
            stats.append(stat)
        return stats

    def get_stats_by_user_and_period(
        self, id: int, date_from: date, date_to: date
    ) -> List[StatsResponseV1]:
        query = select(tables.stats).where(
            and_(
                tables.stats.c.user_id == id,
                tables.stats.c.date.between(date_from, date_to)
                )
            ).order_by(tables.stats.c.repo_id, tables.stats.c.date)
        with self._engine.connect() as connection:
            stats_data = connection.execute(query)
        stats = []
        for data in stats_data:
            stat = StatsResponseV1(
                user_id=data['user_id'],
                repo_id=data['repo_id'],
                date=data['date'],
                stargazers=data['stargazers'],
                forks=data['forks'],
                watchers=data['watchers'],
            )
            stats.append(stat)
        return stats

    def add_user(self, user: UserAddRequestV1) -> None:
        query = insert(tables.users).values(
            id=user.id,
            login=user.login,
            name=user.name
        )
        with self._engine.connect() as connection:
            connection.execute(query)
            connection.commit()

    def delete_user_by_id(self, id: int) -> None:
        query_1 = delete(tables.users).where(tables.users.c.id == id)
        query_2 = delete(tables.stats).where(tables.stats.c.user_id == id)
        with self._engine.connect() as connection:
            connection.execute(query_1)
            connection.execute(query_2)
            connection.commit()
