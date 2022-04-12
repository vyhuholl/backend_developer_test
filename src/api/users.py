from datetime import date
from typing import List

from fastapi import APIRouter, Depends, Path, status

from src.api.protocols import UserServiceProtocol
from src.user.models import (
    UserAddRequestV1, UserResponseV1, UserStatsResponseV1
    )

router = APIRouter(
    tags=['Users']
)


@router.get(
    path='/v1/users',
    response_model=List[UserResponseV1],
    summary='Список пользователей',
    description='Возвращает список всех пользователей.'
)
def get_all_users(
        user_service: UserServiceProtocol = Depends()
):
    return user_service.get_all_users()


@router.get(
    path='/v1/users/{id}',
    response_model=UserResponseV1,
    summary='Информация о пользователе',
    description='Возвращает информацию о пользователе.'
)
def get_user(
        id: int = Path(..., ge=1),
        user_service: UserServiceProtocol = Depends()
):
    return user_service.get_user_by_id(id)


@router.get(
    path='/v1/users/{id}/stats',
    response_model=UserResponseV1,
    summary='Информация о репозиториях пользователя.',
    description='Возвращает информацию о репозиториях пользователя.'
)
def get_stats_by_user(
        id: int = Path(..., ge=1),
        user_service: UserServiceProtocol = Depends()
):
    response = UserStatsResponseV1(
        user=user_service.get_user_by_id(id),
        stats=user_service.get_stats_by_user(id)
    )
    return response


@router.get(
    path='/v1/users/{id}/stats/from={date_from}&to={date_to}',
    response_model=UserResponseV1,
    summary='Информация о репозиториях пользователя за заданный период.',
    description='Возвращает информацию о репозиториях \
        пользователя за заданный период.'
)
def get_stats_by_user_and_period(
        id: int = Path(..., ge=1),
        date_from: date = Path(...),
        date_to: date = Path(...),
        user_service: UserServiceProtocol = Depends()
):
    response = UserStatsResponseV1(
        user=user_service.get_user_by_id(id),
        stats=user_service.get_stats_by_user_and_period(
            id, date_from, date_to
            )
    )
    return response


@router.put(
    path='/v1/users',
    status_code=status.HTTP_201_CREATED,
    summary='Добавить пользователя',
    description='Добавляет пользователя для отслеживания \
        популярности репозиториев.',
)
def add_user(
        user_data: UserAddRequestV1,
        user_service: UserServiceProtocol = Depends()
):
    user_service.add_user(user_data)


@router.delete(
    path='/v1/users/{id}',
    summary='Удалить пользователя',
    description='Удаляет пользователя.'
)
def delete_user(
        id: int = Path(..., ge=1),
        user_service: UserServiceProtocol = Depends()
):
    user_service.delete_user_by_id(id)
