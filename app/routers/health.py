from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import settings
from app.core.database import check_database_connection

router = APIRouter(prefix="/health", tags=["Salud del Sistema"])


@router.get("", summary="Verificar estado de la API y la base de datos")
def health_check():
    try:
        check_database_connection()
        return {
            "status": "ok",
            "service": settings.APP_NAME,
            "environment": settings.APP_ENV,
            "database": "connected",
        }
    except SQLAlchemyError:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "error",
                "service": settings.APP_NAME,
                "environment": settings.APP_ENV,
                "database": "disconnected",
            },
        )