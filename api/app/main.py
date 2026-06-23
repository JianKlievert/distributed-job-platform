from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.auth import router as auth_router
from app.routes.jobs import router as jobs_router

app = FastAPI(
	title="Distributed Job Platform API",
	version="1.0.0"
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(jobs_router)
