from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from api.db.session import engine
from api.db.base import Base
from api.routes.base import router as api_routers
from webapps.routes.base import router as webapps_routers

from config import settings

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_routers)
    app.include_router(webapps_routers)

def start_application():
    app = FastAPI(
        title = settings.PROJECT_TITLE,
        version = settings.PROJECT_VERSION,
        description = settings.DESCRIPTION,
        contact={"name": settings.NAME, "email": settings.EMAIL},
        max_size=int(settings.MAX_SIZE),
    )
    create_tables()
    include_router(app)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app

app = start_application()