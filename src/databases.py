import urllib.parse as urlparse
from typing import AsyncGenerator
from .config import config
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

url: str = f"{config.DRIVER}://{config.DB_USER}:{config.DB_PASSWORD}@{config.HOST}:{config.PORT}/{config.NAME}"

if config.CONN == "socket":
    url: str = "{}://{}:{}@/{}?unix_socket={}&charset=utf8mb4".format(
        config.DRIVER,
        config.DB_USER,
        urlparse.quote_plus(config.DB_PASSWORD),
        config.NAME,
        config.HOST
    )

print(url)

engine = create_async_engine(url, pool_size=5, max_overflow=0, pool_timeout=30)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    try:
        db: AsyncSession = SessionLocal()
        yield db
    finally:
        await db.close()

class Schema():

    def delete(self):
        """ SoftDelete """
        self.enable = False

    def update_from_dict(self, data: dict):
        """ Update from dict the objects values """
        for key in data:
            setattr(self, key, data[key])
