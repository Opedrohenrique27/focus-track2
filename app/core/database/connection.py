import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings

logger = logging.getLogger(__name__)

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
    echo=settings.debug,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        db.rollback()
        raise
    finally:
        db.close()


def init_db():
    from app.models import task  # noqa: F401

    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized successfully.")
