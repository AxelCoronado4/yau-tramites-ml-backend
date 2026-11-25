# yau-tramites-ml-backend
# Backend – Sistema Automatizado de Gestión de Trámites y Selección de Currículos (Municipalidad Provincial de Yau)

API REST con Machine Learning integrado para modernizar la gestión documental administrativa y la evaluación de currículos en la Municipalidad Provincial de Yau.

## Módulos principales
1. **Gestión Documental y Trámites Ciudadanos:** Registro de expedientes, control de estados con auditoría, priorización predictiva de trámites críticos mediante Machine Learning, alertas en tiempo real y métricas de cuellos de botella.
2. **Selección de Currículos (RR.HH.):** Gestión de convocatorias laborales municipales, carga y extracción de texto de CVs en formato PDF y ranking automático de afinidad mediante procesamiento de lenguaje natural (NLP).

## Stack tecnológico
- **Lenguaje:** Python 3.12
- **Framework API:** FastAPI + Pydantic v2
- **Base de Datos:** PostgreSQL 16 (SQLAlchemy 2.0 + Alembic)
- **Machine Learning:** Scikit-learn, Pandas, Joblib
- **Seguridad:** JWT + Hashing seguro de contraseñas + RBAC
- **Infraestructura:** Docker & Docker Compose
- **Documentación API:** OpenAPI 3 / Swagger UI (`/docs`)

## Requisitos previos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)
- Python 3.11+ (opcional para ejecución local fuera de Docker)

## Configuración inicial
1. Clonar el repositorio.
2. Copiar el archivo de variables de entorno:
   ```bash
   cp .env.example .env