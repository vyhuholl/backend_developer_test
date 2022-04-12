import sqlalchemy as sa
from fastapi import FastAPI
from fastapi_utils.session import FastAPISessionMaker  # type: ignore
from fastapi_utils.tasks import repeat_every  # type: ignore

from src.api import users
from src.api.protocols import UserServiceProtocol
from src.database import DatabaseSettings, create_database_url
from src.user.service import UserService

db_settings = DatabaseSettings()
db_url = create_database_url(db_settings)


def get_application() -> FastAPI:
    application = FastAPI(
        title='GitHub Repo Stats',
        description='Сервис сбора статистических данных \
            о популярности репозиториев на GitHub.',
        version='1.0.0'
    )

    application.include_router(users.router)

    engine = sa.create_engine(db_url, future=True)
    user_service = UserService(engine)
    protocol = UserServiceProtocol
    application.dependency_overrides[protocol] = lambda: user_service
    return application


app = get_application()
sessionmaker = FastAPISessionMaker(db_url)


def scan_repos(db: sa.orm.Session) -> None:
    pass


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24)  # 1 day
def scan_repos_task() -> None:
    with sessionmaker.context_session() as db:
        scan_repos(db=db)
