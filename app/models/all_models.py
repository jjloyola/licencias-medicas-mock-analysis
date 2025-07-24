# Importar todos los modelos para que SQLModel los reconozca
from .beneficiarios import Beneficiario
from .licencias_medicas import LicenciaMedica
from .beneficio_logs import BeneficioLog

__all__ = ["Beneficiario", "LicenciaMedica", "BeneficioLog"] 