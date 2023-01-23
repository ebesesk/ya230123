from fastapi import FastAPI, Request

from api.db.session import engine
from api.db.base import Base
from api.routes.base import router as api_routers

from config import settings

app = FastAPI()


def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_routers)

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
    return app

app = start_application()

# @app.on_event("startup")
# def startup():
#     engine.connect()

# @app.on_event("shutdown")
# def shutdown():
#     engine.disconnect()
    
# @app.middleware("http")
# def state_insert(request: Request, call_next):
#     request.state.db_conn = engine
#     response = call_next(request)