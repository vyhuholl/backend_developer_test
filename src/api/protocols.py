from datetime import date
from typing import List

from src.user.models import (StatsAddRequestV1, StatsResponseV1,
                             UserAddRequestV1, UserResponseV1)


class UserServiceProtocol:
    def get_all_users(self) -> List[UserResponseV1]:
        raise NotImplementedError

    def get_user_by_id(self, id: int) -> UserResponseV1:
        raise NotImplementedError

    def get_stats_by_user(self, id: int) -> List[StatsResponseV1]:
        raise NotImplementedError

    def get_stats_by_user_and_period(
        self, id: int, date_from: date, date_to: date
            ) -> List[StatsResponseV1]:
        raise NotImplementedError

    def add_user(self, user: UserAddRequestV1) -> None:
        raise NotImplementedError

    def add_stats(self, stats: StatsAddRequestV1) -> None:
        raise NotImplementedError

    def delete_user_by_id(self, id: int) -> None:
        raise NotImplementedError
