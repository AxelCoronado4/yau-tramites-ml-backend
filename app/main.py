from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import health

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description=(
        "API REST con Machine Learning para la gestión de trámites municipales "
        "y selección automatizada de currículos en la Municipalidad Provincial de Yau."
    ),
)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix=settings.API_V1_PREFIX)


@app.get("/", tags=["Raíz"], summary="Información básica del servicio")
def root():
    return {
        "message": "API operativa - Municipalidad Provincial de Yau",
        "docs": "/docs",
        "health": f"{settings.API_V1_PREFIX}/health",
    }