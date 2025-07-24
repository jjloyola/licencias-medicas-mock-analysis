from sqlmodel import SQLModel, create_engine, Session
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv("config.env")

class Settings(BaseSettings):
    database_url: str = "postgresql://jloyola@localhost/suseso_beneficios"
    
    class Config:
        env_file = "config.env"
        extra = "ignore"

settings = Settings()

# Crear el motor de la base de datos
engine = create_engine(
    settings.database_url,
    echo=False,  # Mostrar las consultas SQL en la consola
    pool_pre_ping=True
)

def create_db_and_tables():
    """Crear todas las tablas en la base de datos"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Obtener una sesión de la base de datos"""
    with Session(engine) as session:
        yield session 