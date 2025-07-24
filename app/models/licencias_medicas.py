from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .beneficiarios import Beneficiario

class LicenciaMedica(SQLModel, table=True):
    """Modelo para la tabla de licencias médicas"""
    
    __tablename__:str = "licencias_medicas"
    
    licencia_id: int = Field(primary_key=True, description="ID único de la licencia")
    beneficiario_id: int = Field(foreign_key="beneficiarios.beneficiario_id", description="ID del beneficiario")
    ccaf: str = Field(description="Caja de Compensación de Asignación Familiar")
    fecha_emision: date = Field(description="Fecha de emisión de la licencia")
    dias_licencia: int = Field(description="Número de días de licencia")
    causa: str = Field(description="Causa de la licencia médica")
    emisor_rut: str = Field(description="RUT del médico emisor")
    region: str = Field(description="Región donde se emitió la licencia")
    monto_subsidio_clp: int = Field(description="Monto del subsidio en pesos chilenos")
    estado_pago: str = Field(description="Estado del pago (Pagado, Pendiente, etc.)")
    fecha_pago: Optional[date] = Field(default=None, description="Fecha de pago del subsidio")
    
    # Relación con beneficiario
    #beneficiario: Optional["Beneficiario"] = Relationship(back_populates="licencias", sa_relationship_kwargs={"lazy": "selectin"})
    
    class Config:
        json_schema_extra = {
            "example": {
                "licencia_id": 1,
                "beneficiario_id": 1,
                "ccaf": "Los Héroes",
                "fecha_emision": "2025-01-12",
                "dias_licencia": 14,
                "causa": "COVID-19",
                "emisor_rut": "10433218-1",
                "region": "Los Lagos",
                "monto_subsidio_clp": 528724,
                "estado_pago": "Pagado",
                "fecha_pago": "2025-02-05"
            }
        }
    