import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import quotes, tasks
from app.core.config import settings
from app.core.database import init_db
from app.utils.logging import setup_logging

setup_logging(debug=settings.debug)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    logger.info(f"{settings.app_name} v{settings.app_version} started.")
    yield
    logger.info("Application shutdown.")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description="Sistema de gerenciamento de tarefas e produtividade pessoal.",
        version=settings.app_version,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(tasks.router, prefix="/api/v1")
    app.include_router(quotes.router, prefix="/api/v1")

    @app.get("/health", tags=["Health"])
    def health_check():
        return {"status": "ok", "version": settings.app_version}

    try:
        if os.path.exists("frontend"):
            app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
    except Exception:
        logger.warning("Frontend static files not mounted.")

    return app


app = create_app()
