from sqlmodel import SQLModel, Field, Relationship, Session, select
from datetime import date
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .licencias_medicas import LicenciaMedica
    from .beneficio_logs import BeneficioLog

class Beneficiario(SQLModel, table=True):
    """Modelo para la tabla de beneficiarios"""
    
    __tablename__: str = "beneficiarios"
    
    beneficiario_id: int = Field(primary_key=True, description="ID único del beneficiario")
    ccaf: str = Field(description="Caja de Compensación de Asignación Familiar")
    fecha_nacimiento: date = Field(description="Fecha de nacimiento del beneficiario")
    sexo: str = Field(max_length=1, description="Sexo del beneficiario (M/F)")
    
    # Relaciones
    licencias: List["LicenciaMedica"] = Relationship(back_populates="beneficiario", sa_relationship_kwargs={"lazy": "selectin"})
    #beneficios: List["BeneficioLog"] = Relationship(back_populates="beneficiario", sa_relationship_kwargs={"lazy": "selectin"})
    
    @classmethod
    def get_all_beneficiaries_by_ccaf(cls, session: Session, ccaf: str, limit: int = 10) -> List["Beneficiario"]:
        """Obtener beneficiarios por CCAF"""
        statement = select(cls).where(cls.ccaf == ccaf).order_by(cls.fecha_nacimiento.asc()).limit(limit) # type: ignore
        return list(session.exec(statement).all())

    
    class Config:
        json_schema_extra = {
            "example": {
                "beneficiario_id": 1,
                "ccaf": "Los Héroes",
                "fecha_nacimiento": "1947-09-15",
                "sexo": "M"
            }
        } 