from pydantic import BaseSettings, Field


class DatabaseSettings(BaseSettings):
    host: str = Field(..., env='DB_HOST')
    port: str = Field(..., env='DB_PORT')
    username: str = Field(..., env='DB_USERNAME')
    password: str = Field(..., env='DB_PASSWORD')
    database: str = Field(..., env='DB_DATABASE')
