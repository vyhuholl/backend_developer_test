import datetime
from typing import List

from pydantic import BaseModel, Field


class UserResponseV1(BaseModel):
    id: int = Field(..., ge=1)
    login: str
    name: str


class UserAddRequestV1(BaseModel):
    id: int = Field(..., ge=1)
    login: str
    name: str


class StatsResponseV1(BaseModel):
    user_id: int = Field(..., ge=1)
    repo_id: int = Field(..., ge=1)
    date: datetime.date = Field(...)
    stargazers: int = Field(...)
    forks: int = Field(...)
    watchers: int = Field(...)


class StatsAddRequestV1(BaseModel):
    user_id: int = Field(..., ge=1)
    repo_id: int = Field(..., ge=1)
    date: datetime.date = Field(...)
    stargazers: int = Field(...)
    forks: int = Field(...)
    watchers: int = Field(...)


class UserStatsResponseV1(BaseModel):
    user: UserResponseV1 = Field(...)
    stats: List[StatsResponseV1] = Field(...)
