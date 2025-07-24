from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .beneficiarios import Beneficiario

class BeneficioLog(SQLModel, table=True):
    """Modelo para la tabla de logs de beneficios"""
    
    __tablename__:str = "beneficio_logs"
    
    id: Optional[int] = Field(default=None, primary_key=True, description="ID único del log")
    beneficiario_id: int = Field(foreign_key="beneficiarios.beneficiario_id", description="ID del beneficiario")
    fecha: date = Field(description="Fecha del beneficio", index=True)
    beneficio: str = Field(description="Tipo de beneficio")
    monto: int = Field(description="Monto del beneficio en pesos chilenos")
    
    # Relación con beneficiario
    beneficiario: Optional["Beneficiario"] = Relationship(back_populates="beneficios", sa_relationship_kwargs={"lazy": "selectin"})
    
    class Config:
        json_schema_extra = {
            "example": {
                "beneficiario_id": 1,
                "fecha": "2024-05-16",
                "beneficio": "Postnatal",
                "monto": 417716
            }
        } 